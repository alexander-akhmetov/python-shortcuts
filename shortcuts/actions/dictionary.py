from shortcuts.actions.base import BaseAction, Field, DictionaryField


class GetDictionaryValueAction(BaseAction):
    '''Get dictionary value'''
    type = 'is.workflow.actions.getvalueforkey'
    keyword = 'get_value_for_key'

    key = Field('WFDictionaryKey')


class DictionaryAction(BaseAction):
    '''Dictionary'''
    type = 'is.workflow.actions.dictionary'
    keyword = 'dictionary'

    items = DictionaryField('WFItems')
