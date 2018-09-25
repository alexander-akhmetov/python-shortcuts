import collections
import copy
import plistlib
from typing import TYPE_CHECKING, Any, Dict, List, TextIO, Tuple, Type, Union

import toml

from shortcuts.actions import ITYPE_TO_ACTION_MAP, KEYWORD_TO_ACTION_MAP


if TYPE_CHECKING:
    from shortcuts import Shortcut  # noqa
    from shortcuts.actions.base import BaseAction  # noqa


class BaseLoader:
    @classmethod
    def load(cls, file_obj: TextIO) -> 'Shortcut':
        content = file_obj.read()
        if isinstance(content, (bytes, bytearray)):
            content = content.decode('utf-8')
        return cls.loads(content)

    @classmethod
    def loads(cls, string: str) -> 'Shortcut':
        raise NotImplementedError()


class TomlLoader(BaseLoader):
    @classmethod
    def loads(cls, string: str) -> 'Shortcut':
        from shortcuts import Shortcut  # noqa

        shortcut_dict = toml.loads(string)
        shortcut = Shortcut(name=shortcut_dict.get('name', 'python-shortcuts'))

        if not isinstance(shortcut_dict.get('action'), list):
            raise ValueError('toml file must contain "action" array with actions')

        for action in shortcut_dict['action']:
            action_params = copy.deepcopy(action)
            del action_params['type']
            shortcut.actions.append(
                KEYWORD_TO_ACTION_MAP[action['type']](data=action_params)
            )

        return shortcut


class PListLoader(BaseLoader):
    @classmethod
    def loads(cls, string: Union[str, bytes]) -> 'Shortcut':
        from shortcuts import Shortcut  # noqa

        if isinstance(string, str):
            string = string.encode('utf-8')

        shortcut_dict: Dict = plistlib.loads(string)
        shortcut = Shortcut(
            name=shortcut_dict.get('name', 'python-shortcuts'),
            client_release=shortcut_dict['WFWorkflowClientRelease'],
            client_version=shortcut_dict['WFWorkflowClientVersion'],
        )

        for action in shortcut_dict['WFWorkflowActions']:
            shortcut.actions.append(cls._action_from_dict(action))

        return shortcut

    @classmethod
    def _action_from_dict(cls, action_dict: Dict) -> 'BaseAction':
        action_class = cls._get_action_class(action_dict)

        if not action_class:
            msg = f'''
            Unknown shortcut action: {type}

            Please, check documentation to add new shortcut action, or create an issue:
            Docs: https://github.com/alexander-akhmetov/python-shortcuts/tree/master/docs/new_action.md

            https://github.com/alexander-akhmetov/python-shortcuts/

            Action dictionary:

            {action_dict}
            '''
            raise RuntimeError(msg)

        shortcut_name_to_field_name = {
            f.name: f._attr for f in action_class().fields
        }
        params = {
            shortcut_name_to_field_name[p]: WFDeserializer(v).deserialized_data
            for p, v in action_dict['WFWorkflowActionParameters'].items()
            if p in shortcut_name_to_field_name
        }

        return action_class(data=params)

    @classmethod
    def _get_action_class(cls, action_dict: Dict) -> Union[Type['BaseAction'], None]:
        identifier = action_dict['WFWorkflowActionIdentifier']
        action_class = ITYPE_TO_ACTION_MAP.get(identifier)

        # in some cases we have action classes with the same itype (identifier)
        # but they have different parameters
        #
        # For example, Base64EncodeAction and Base64DecodeAction
        # classes have the same itype: "is.workflow.actions.base64encode"
        # we need to check parameters to determine which action class we need to use
        #
        # todo: action-based common solution
        if identifier == 'is.workflow.actions.conditional':
            action_class = cls._get_if_else_action_class(action_dict)
        elif identifier == 'is.workflow.actions.base64encode':
            action_class = cls._get_base64_action_class(action_dict)
        elif identifier == 'is.workflow.actions.repeat.count':
            action_class = cls._get_repeat_action_class(action_dict)
        elif identifier == 'is.workflow.actions.choosefrommenu':
            action_class = cls._get_menu_action_class(action_dict)

        return action_class

    @classmethod
    def _get_if_else_action_class(cls, action_dict: Dict) -> Type['BaseAction']:
        """Returns If-Else-EndIf action class based on WFControlFlowMode parameter of action_dict"""
        from shortcuts.actions import IfAction, ElseAction, EndIfAction
        return cls._get_action_class_by_wf_control_flow(
            from_classes=(IfAction, ElseAction, EndIfAction),
            action_dict=action_dict,
        )

    @classmethod
    def _get_repeat_action_class(cls, action_dict: Dict) -> Type['BaseAction']:
        """Returns Repeat-Start or Repeat-End action class based on WFControlFlowMode parameter of action_dict"""
        from shortcuts.actions import RepeatEndAction, RepeatStartAction
        return cls._get_action_class_by_wf_control_flow(
            from_classes=(RepeatEndAction, RepeatStartAction),
            action_dict=action_dict,
        )

    @classmethod
    def _get_menu_action_class(cls, action_dict: Dict) -> Type['BaseAction']:
        """Returns Menu action class based on WFControlFlowMode parameter of action_dict"""
        from shortcuts.actions import MenuStartAction, MenuItemAction, MenuEndAction
        return cls._get_action_class_by_wf_control_flow(
            from_classes=(MenuStartAction, MenuItemAction, MenuEndAction),
            action_dict=action_dict,
        )

    @classmethod
    def _get_action_class_by_wf_control_flow(cls,
                                             from_classes: Tuple[Type['BaseAction'], ...],
                                             action_dict: Dict) -> Type['BaseAction']:
        """Returns class from `from_classes` based on WFControlFlowMode parameter of action_dict"""
        flow_to_action = {a.default_fields['WFControlFlowMode']: a for a in from_classes}  # type: ignore
        wf_control_flow_mode = action_dict['WFWorkflowActionParameters']['WFControlFlowMode']
        return flow_to_action[wf_control_flow_mode]

    @classmethod
    def _get_base64_action_class(cls, action_dict: Dict) -> Type['BaseAction']:
        """Returns Base64EncodeAction or Base64DecodeAction based on WFEncodeMode parameter of action_dict"""
        from shortcuts.actions import Base64EncodeAction, Base64DecodeAction
        action_params = action_dict['WFWorkflowActionParameters']

        # by default it's encode, even if it doesn't have WFEncodeMode parameter
        encode_mode = action_params.get('WFEncodeMode', 'Encode')
        if encode_mode == 'Encode':
            return Base64EncodeAction
        elif encode_mode == 'Decode':
            return Base64DecodeAction

        raise RuntimeError(f'Unknown WFEncodeMode: "{encode_mode}"')


class WFDeserializer:
    """
    Deserializer for WF fields (from shortcuts plist)
    which converts their data to a format acceptable by Actions
    """
    def __init__(self, data) -> None:
        self._data = data

    @property
    def deserialized_data(self) -> Union[str, List, Dict]:
        if not isinstance(self._data, dict):
            # todo: check if there are other types
            return self._data

        serialization_to_field_map: Dict[str, Type[WFDeserializer]] = {
            'WFTextTokenString': WFVariableStringField,
            'WFDictionaryFieldValue': WFDictionaryField,
            'WFTextTokenAttachment': WFTextTokenAttachmentField,
            'WFTokenAttachmentParameterState': WFTokenAttachmentParameterStateField,
        }

        deserializer = serialization_to_field_map[self._data.get('WFSerializationType')]  # type: ignore
        if deserializer:
            return deserializer(self._data).deserialized_data

        raise RuntimeError(f'Unknown serialization type: {self._data.get("WFSerializationType")}')


class WFTokenAttachmentParameterStateField(WFDeserializer):
    def __init__(self, data) -> None:
        self._data = data['Value']


class WFTextTokenAttachmentField(WFDeserializer):
    @property
    def deserialized_data(self) -> str:
        if self._data['Value'].get('Type') == 'Ask':
            return '{{ask_when_run}}'

        return self._data['Value']['VariableName']


class WFDictionaryField(WFDeserializer):
    @property
    def deserialized_data(self) -> List[Dict[str, Any]]:
        result = []
        for item in self._data['Value']['WFDictionaryFieldValueItems']:
            key = WFDeserializer(item['WFKey']).deserialized_data
            value = WFDeserializer(item['WFValue']).deserialized_data
            result.append({'key': key, 'value': value})
        return result


class WFVariableStringField(WFDeserializer):
    """
    Converts wf variable string (dictionary)
        <dict>
            <key>Value</key>
            <dict>
                <key>attachmentsByRange</key>
                <dict>
                    <key>{7, 1}</key>
                    <dict>
                        <key>Type</key>
                        <string>Variable</string>
                        <key>VariableName</key>
                        <string>name</string>
                    </dict>
                </dict>
                <key>string</key>
                <string>Hello, ￼!</string>
            </dict>
            <key>WFSerializationType</key>
            <string>WFTextTokenString</string>
        </dict>

    to a shortcuts-string:
        "Hello, {{var}}!"
    """
    @property
    def deserialized_data(self) -> str:
        # if this field is a string with variables,
        # we need to convert it to our representation
        value = self._data['Value']
        value_string = value['string']

        positions = {}

        supported_types = ('Ask', 'Variable')

        for variable_range, variable_data in value['attachmentsByRange'].items():
            if variable_data['Type'] not in supported_types:
                # it doesn't support magic variables yet
                raise RuntimeError(
                    f'Unsupported variable type: {variable_data["Type"]} (possibly it is a magic variable)',
                )

            if variable_data['Type'] == 'Variable':
                variable_name = variable_data['VariableName']
            elif variable_data['Type'] == 'Ask':
                variable_name = 'ask_when_run'

            # let's find positions of all variables in the string
            position = self._get_position(variable_range)
            positions[position] = '{{%s}}' % variable_name

        # and then replace them with '{{variable_name}}'
        offset = 0
        for pos, variable in collections.OrderedDict(sorted(positions.items())).items():
            value_string = value_string[:pos + offset] + variable + value_string[pos + offset:]
            offset += len(variable)

        return value_string

    def _get_position(self, range_str: str) -> int:
        ranges = list(map(lambda x: int(x.strip()), range_str.strip('{} ').split(',')))
        return ranges[0]
