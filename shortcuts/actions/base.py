import re
from typing import Dict, Tuple, List, Union, Any


class BaseAction:
    type = None  # identificator from shortcut source
    keyword = None  # this keyword is used in the toml file
    default_fields = None  # dictionary with default parameters fields

    def __init__(self, data: Union[Dict, None] = None) -> None:
        self.data = data if data is not None else {}

    def dumps(self) -> Dict:
        data = {
            'WFWorkflowActionIdentifier': self.type,
            'WFWorkflowActionParameters': {},
        }

        data['WFWorkflowActionParameters'].update(
            self._get_parameters(),
        )

        return data

    def _get_parameters(self) -> Dict:
        params = {}

        if self.default_fields:
            params.update(self.default_fields)

        for field in self.fields:
            try:
                data_value = self.data[field._attr]
            except KeyError:
                if field.required:
                    raise ValueError(f'{self}, Field is required: {field._attr}:{field.name}')
                else:
                    continue

            params[field.name] = field.process_value(data_value)

            if isinstance(field, VariablesField):
                params['WFSerializationType'] = 'WFTextTokenString'

        return params

    @property
    def fields(self) -> List[Any]:
        if not hasattr(self, '_fields'):
            self._fields = []
            for attr in dir(self):
                field = getattr(self, attr)
                if isinstance(field, (Field, VariablesField)):
                    field._attr = attr
                    self._fields.append(field)

        return self._fields


class Field:
    def __init__(self, name, required=True, capitalize=False, help=''):
        self.name = name
        self.required = required
        self.capitalize = capitalize
        self.help = help

    def process_value(self, value):
        if self.capitalize:
            value = value.capitalize()

        return value


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


class VariablesField(Field):
    _regexp = re.compile(r'({{[A-Za-z0-9_-]+}})')

    def process_value(self, value):
        attachments_by_range, string = self._get_variables_from_text(value)

        if not attachments_by_range:
            # if we don't have variables in the string,
            # just return the value
            return value

        return {
            'Value': {
                'attachmentsByRange': attachments_by_range,
                'string': string,
            },
            'WFSerializationType': 'WFTextTokenString',
        }

    def _get_variables_from_text(self, value: str) -> List[Tuple[str, str]]:
        attachments_by_range = {}
        offset = 0
        for m in self._regexp.finditer(value):
            attachments_by_range[f'{{{m.start() - offset}, {1}}}'] = {
                'Type': 'Variable',
                'VariableName': m.group().strip('{}'),
            }
            offset += len(m.group()) - 1

        # replacing all variables with char 65523 (OBJECT REPLACEMENT CHARACTER)
        string = self._regexp.sub('￼', value)
        return attachments_by_range, string
