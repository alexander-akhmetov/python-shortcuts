from shortcuts.actions.base import BaseAction, DictionaryField, Field


class GetDictionaryValueAction(BaseAction):
    '''Get dictionary value'''
    itype = 'is.workflow.actions.getvalueforkey'
    keyword = 'get_value_for_key'

    key = Field('WFDictionaryKey')


class DictionaryAction(BaseAction):
    '''Dictionary'''
    itype = 'is.workflow.actions.dictionary'
    keyword = 'dictionary'

    items = DictionaryField('WFItems')
