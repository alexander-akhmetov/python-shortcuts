from typing import Dict, Union

from shortcuts.actions.base import BaseAction, BooleanField, DictionaryField, Field


class URLAction(BaseAction):
    '''URL: returns url as an output'''
    itype = 'is.workflow.actions.url'
    keyword = 'url'

    url = Field('WFURLActionURL')


class HTTPMethodField(Field):
    methods = (
        'GET',
        'POST',
        'PUT',
        'PATCH',
        'DELETE',
    )

    def process_value(self, value):
        value = super().process_value(value).upper()
        if value not in self.methods:
            raise ValueError(f'Unsupported HTTP method: {value}. \nSupported: {self.methods}')
        return value


class GetURLAction(BaseAction):
    '''Get URL'''
    itype = 'is.workflow.actions.downloadurl'
    keyword = 'get_url'

    advanced = BooleanField('Advanced', required=False)
    method = HTTPMethodField('WFHTTPMethod', required=False)
    headers = DictionaryField('WFHTTPHeaders', required=False)
    json = DictionaryField('WFJSONValues', required=False)    # todo: array or dict
    form = DictionaryField('WFFormValues', required=False)    # todo: array or dict

    def __init__(self, data: Union[Dict, None] = None) -> None:
        self.default_fields = {}
        super().__init__(data=data)

        if data and data.get('form'):
            self.default_fields['WFHTTPBodyType'] = 'Form'
        elif data and data.get('json'):
            self.default_fields['WFHTTPBodyType'] = 'Json'

        if data and data.get('headers'):
            self.default_fields['ShowHeaders'] = True


class URLEncodeAction(BaseAction):
    '''URL Encode'''
    itype = 'is.workflow.actions.urlencode'
    keyword = 'urlencode'

    _additional_identifier_field = 'WFEncodeMode'
    _default_class = True

    default_fields = {
        'WFEncodeMode': 'Encode',
    }


class URLDecodeAction(BaseAction):
    '''URL Dencode'''
    itype = 'is.workflow.actions.urlencode'
    keyword = 'urldecode'

    _additional_identifier_field = 'WFEncodeMode'

    default_fields = {
        'WFEncodeMode': 'Decode',
    }


class ExpandURLAction(BaseAction):
    '''
    Expand URL: This action expands and cleans up URLs
    that have been shortened by a URL shortening
    service like TinyURL or bit.ly
    '''
    itype = 'is.workflow.actions.url.expand'
    keyword = 'expand_url'


class OpenURLAction(BaseAction):
    '''Open URL from previous action'''
    itype = 'is.workflow.actions.openurl'
    keyword = 'open_url'
