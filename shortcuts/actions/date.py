from shortcuts.actions.base import BaseAction, Field, VariablesField


class DateAction(BaseAction):
    '''Date'''
    type = 'is.workflow.actions.date'
    keyword = 'date'

    default_answer = VariablesField('WFAskActionDefaultAnswer', required=False)


class FormatDateAction(BaseAction):
    '''Format date'''
    type = 'is.workflow.actions.format.date'
    keyword = 'format_date'

    format = Field('WFDateFormat')

    default_fields = {
        'WFDateFormatStyle': 'Custom',
    }
