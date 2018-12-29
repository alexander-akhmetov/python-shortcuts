import re
from copy import deepcopy
from typing import Any, Dict, List, Optional, Tuple, Union


class BaseAction:
    itype: Union[
        str, None
    ] = None    # identificator from shortcut source (being used by iOS app): WFWorkflowActionIdentifier
    keyword: Union[str, None] = None    # this keyword is being used in the toml file
    default_fields: Dict = {}    # noqa dictionary with default parameters fields
    _additional_identifier_field: Union[str, None] = None
    _default_class: Optional[bool] = None

    def __init__(self, data: Union[Dict, None] = None) -> None:
        self.data = data if data is not None else {}
        self.default_fields = deepcopy(self.default_fields)

    def dump(self) -> Dict:
        data = {
            'WFWorkflowActionIdentifier': self.itype,
            'WFWorkflowActionParameters': {},
        }

        data['WFWorkflowActionParameters'].update(    # type: ignore
            self._get_parameters(),
        )

        return data

    def _get_parameters(self) -> Dict:
        '''
        Returns dictionary with action parameters for a plist.
        It iterates over all fields, and processes the action's params to get values for all fields.

        As an output we have dictionary, and values of the dictionary
        are prepared data by corresponding field's "process_value" method.
        '''
        params = {}

        if self.default_fields:
            params.update(self.default_fields)

        for field in self.fields:
            try:
                data_value = self.data[field._attr]
            except KeyError:
                if field.default is not None:
                    data_value = field.default
                elif field.required:
                    raise ValueError(f'{self}, Field is required: {field._attr}:{field.name}')
                else:
                    continue

            params[field.name] = field.process_value(data_value)

        return params

    @property
    def fields(self) -> List[Any]:
        '''Returns list of all fields of the action (with memoization).'''
        if not hasattr(self, '_fields'):
            self._fields: List['Field'] = []
            for attr in dir(self):
                field = getattr(self, attr)
                if isinstance(field, (Field, VariablesField)):
                    field._attr = attr
                    self._fields.append(field)

        return self._fields


class Field:
    _attr: Union[None, str] = None

    def __init__(self, name, default=None, required=True, capitalize=False, help=''):
        self.name = name
        self.required = required
        self.capitalize = capitalize
        self.help = help
        self.default = default

    def process_value(self, value):
        '''Prepares the value to be represented in the Shortcuts app'''
        if self.capitalize:
            value = value.capitalize()

        return value


class GroupIDField(Field):
    def __init__(self, *args, **kwargs):
        kwargs['required'] = False
        super().__init__(*args, **kwargs)


class ChoiceField(Field):
    def __init__(self, name, choices, default=None, required=True, capitalize=False, help=''):
        super().__init__(
            name=name, required=required, default=default, capitalize=capitalize, help=help
        )
        self.choices = choices

    def process_value(self, value):
        value = super().process_value(value)
        if value not in self.choices:
            raise ValueError(f'Value "{value}" not in the choices list: {self.choices}')
        return value


class ArrayField(Field):
    def process_value(self, value):
        if not isinstance(value, (list, tuple)):
            raise ValueError(f'{self._attr}:{self.__class__}: Value must be a list')

        return super().process_value(value)


class FloatField(Field):
    def process_value(self, value):
        return float(super().process_value(value))


class IntegerField(Field):
    def process_value(self, value):
        return int(super().process_value(value))


class BooleanField(Field):
    def process_value(self, value):
        if isinstance(value, bool):
            return value

        value = value.lower().strip()
        if value == 'true':
            return True
        elif value == 'false':
            return False

        raise ValueError(f'BooleanField: incorrect value: {value} type: {type(value)}')


class WFVariableField(Field):
    def process_value(self, value):
        return {
            'Value': {
                'Type': 'Variable',
                'VariableName': super().process_value(value),
            },
            'WFSerializationType': 'WFTextTokenAttachment',
        }


# system variables are special variables supported by Shortcuts app.
# Like "Ask when run", "Clipboard", "Current date" and others
# Keys in the dictionary are variable names in the python-shortcuts
# and values are names in the app
SYSTEM_VARIABLES = {
    'ask_when_run': 'Ask',
    'shortcut_input': 'ExtensionInput',
    'clipboard': 'Clipboard',
    'current_date': 'CurrentDate',
}
SYSTEM_VARIABLES_TYPE_TO_VAR = {v: k for k, v in SYSTEM_VARIABLES.items()}


class VariablesField(Field):
    _regexp = re.compile(r'({{[A-Za-z0-9_-]+}})')

    def process_value(self, value: str) -> Dict:
        token = self._check_token_match(value)
        if token:
            return token

        return {
            'Value': self._get_variables_dict(value),
            'WFSerializationType': 'WFTextTokenString',
        }

    def _check_token_match(self, value):
        variable = value.strip('{}')
        var_type = SYSTEM_VARIABLES.get(variable)
        if var_type:
            return {
                'WFSerializationType': 'WFTextTokenAttachment',
                'Value': {
                    'Type': var_type
                },
            }

        return None

    def _get_variables_dict(self, value: str) -> Dict:
        attachments_by_range, string = self._get_variables_from_text(value)
        return {
            'attachmentsByRange': attachments_by_range,
            'string': string,
        }

    def _get_variables_from_text(self, value: str) -> Tuple[Dict[str, Dict[str, str]], str]:
        attachments_by_range = {}
        offset = 0
        for m in self._regexp.finditer(value):
            variable_name = m.group().strip('{}')
            var_type = SYSTEM_VARIABLES.get(variable_name, 'Variable')
            variable_range = f'{{{m.start() - offset}, {1}}}'
            attachments_by_range[variable_range] = {
                'Type': var_type,
            }
            if var_type == 'Variable':
                attachments_by_range[variable_range]['VariableName'] = variable_name
            offset += len(m.group())

        # replacing all variables with char 65523 (OBJECT REPLACEMENT CHARACTER)
        string = self._regexp.sub('￼', value)
        return attachments_by_range, string


class DictionaryField(VariablesField):
    '''
        {
            'Value': {
                'WFDictionaryFieldValueItems': [
                    {
                        'WFItemType': 0,
                        'WFKey': {
                            'Value': {'attachmentsByRange': {},  'string': 'k'},
                            'WFSerializationType': 'WFTextTokenString'
                        },
                        'WFValue': {
                            'Value': {'attachmentsByRange': {}, 'string': 'v'},
                            'WFSerializationType': 'WFTextTokenString'
                        }
                    }
                ]
            },
            'WFSerializationType': 'WFDictionaryFieldValue'
        }
    '''

    def process_value(self, value):
        return {
            'Value': {
                'WFDictionaryFieldValueItems': [self._process_single_value(v) for v in value],
            },
            'WFSerializationType': 'WFDictionaryFieldValue',
        }

    def _process_single_value(self, value):
        key = super().process_value(value['key'])
        value = super().process_value(value['value'])
        return {
            'WFItemType': 0,    # text
            'WFKey': key,
            'WFValue': value,
        }
