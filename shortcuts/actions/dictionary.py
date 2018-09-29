from shortcuts.actions.base import BaseAction, DictionaryField, VariablesField


class GetDictionaryValueAction(BaseAction):
    '''Get dictionary value'''
    itype = 'is.workflow.actions.getvalueforkey'
    keyword = 'get_value_for_key'

    key = VariablesField('WFDictionaryKey')


class SetDictionaryValueAction(BaseAction):
    '''Set dictionary value'''
    itype = 'is.workflow.actions.setvalueforkey'
    keyword = 'set_value_for_key'

    key = VariablesField('WFDictionaryKey')
    value = VariablesField('WFDictionaryValue')


class DictionaryAction(BaseAction):
    '''Dictionary'''
    itype = 'is.workflow.actions.dictionary'
    keyword = 'dictionary'

    items = DictionaryField('WFItems')


class GetDictionaryFromInputAction(BaseAction):
    '''Get dictionary from input'''
    itype = 'is.workflow.actions.detect.dictionary'
    keyword = 'get_dictionary'
