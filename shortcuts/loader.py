import copy
import plistlib
import collections
from typing import Dict

import toml

from shortcuts.actions import KEYWORD_TO_ACTION_MAP, TYPE_TO_ACTION_MAP


class BaseLoader:
    @classmethod
    def load(cls, file_obj) -> str:
        content = file_obj.read()
        if isinstance(content, (bytes, bytearray)):
            content = content.decode('utf-8')
        return cls.loads(content)

    @classmethod
    def loads(cls, string) -> str:
        raise NotImplementedError()


class TomlLoader(BaseLoader):
    @classmethod
    def loads(cls, string) -> str:
        from shortcuts import Shortcut

        shortcut_dict = toml.loads(string)
        shortcut = Shortcut(name=shortcut_dict.get('name', 'python-shortcuts'))

        for action in shortcut_dict['action']:
            action_params = copy.deepcopy(action)
            del action_params['type']
            shortcut.actions.append(
                KEYWORD_TO_ACTION_MAP[action['type']](data=action_params)
            )

        return shortcut


class PListLoader(BaseLoader):
    @classmethod
    def loads(cls, string) -> str:
        from shortcuts import Shortcut

        if isinstance(string, str):
            string = string.encode('utf-8')

        shortcut_dict = plistlib.loads(string)
        shortcut = Shortcut(
            name=shortcut_dict.get('name', 'python-shortcuts'),
            client_release=shortcut_dict['WFWorkflowClientRelease'],
            client_version=shortcut_dict['WFWorkflowClientVersion'],
        )

        import pdb; pdb.set_trace()
        for action in shortcut_dict['WFWorkflowActions']:
            shortcut.actions.append(cls._action_from_dict(action))

        return shortcut

    @classmethod
    def _action_from_dict(self, action_dict: Dict):
        type = action_dict['WFWorkflowActionIdentifier']
        action_class = TYPE_TO_ACTION_MAP.get(type)
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
            shortcut_name_to_field_name[p]: self._load_parameter_value(v)
            for p, v in action_dict['WFWorkflowActionParameters'].items()
            if p in shortcut_name_to_field_name
        }

        return action_class(data=params)

    @classmethod
    def _load_parameter_value(cls, value):
        # todo: move to fields
        if not isinstance(value, dict):
            return value

        if value.get('WFSerializationType') == 'WFTextTokenString':
            # if thhis field is a string with variables,
            # we need to convert it to our representation
            value = value['Value']
            value_string = value['string']

            positions = {}

            for variable_range, variable_data in value['attachmentsByRange'].items():
                if variable_data['Type'] != 'Variable':
                    # it doesn't support magic variables yet
                    raise RuntimeError(f'Unsupported variable type: {variable_data["Type"]}')

                # let's find positions of all variables in the string
                position = cls._get_position(variable_range)
                positions[position] = '{{%s}}' % variable_data['VariableName']

            # and then replace them with '{{variable_name}}'
            offset = 0
            for pos, variable in collections.OrderedDict(sorted(positions.items())).items():
                value_string = value_string[:pos + offset] + variable + value_string[pos + offset:]
                offset += len(variable)

            return value_string

    @classmethod
    def _get_position(cls, range_str) -> int:
        ranges = list(map(lambda x: int(x.strip()), range_str.strip('{} ').split(',')))
        return ranges[0]
