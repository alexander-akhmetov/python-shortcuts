from shortcuts.actions.base import BaseAction, Field


class GetDictionaryValueAction(BaseAction):
    '''Get dictionary value'''
    type = 'is.workflow.actions.getvalueforkey'
    keyword = 'get_value_for_key'

    key = Field('WFDictionaryKey')
