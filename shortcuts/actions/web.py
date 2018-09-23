from typing import Dict, Union

from shortcuts.actions.base import (
    BaseAction,
    BooleanField,
    Field,
    DictionaryField,
)


class URLAction(BaseAction):
    '''URL: returns url as an output'''
    type = 'is.workflow.actions.url'
    keyword = 'url'

    url = Field('WFURLActionURL')


class HTTPMethodField(Field):
    methods = (
        'GET', 'POST', 'PUT', 'PATCH', 'DELETE',
    )

    def process_value(self, value):
        value = super().process_value(value).upper()
        if value not in self.methods:
            raise ValueError(f'Unsupported HTTP method: {value}. \nSupported: {self.methods}')
        return value


class GetURLAction(BaseAction):
    '''Get URL'''
    type = 'is.workflow.actions.downloadurl'
    keyword = 'get_url'

    advanced = BooleanField('Advanced', required=False)
    method = HTTPMethodField('WFHTTPMethod', required=False)
    headers = DictionaryField('WFHTTPHeaders', required=False)
    json = DictionaryField('WFJSONValues', required=False)  # todo: array or dict
    form = DictionaryField('WFFormValues', required=False)  # todo: array or dict

    def __init__(self, data: Union[Dict, None] = None) -> None:
        self.default_fields = {}
        super().__init__(data=data)

        if data and data.get('form'):
            self.default_fields['WFHTTPBodyType'] = 'Form'
        elif data and data.get('json'):
            self.default_fields['WFHTTPBodyType'] = 'Json'

        if data and data.get('headers'):
            self.default_fields['ShowHeaders'] = True
