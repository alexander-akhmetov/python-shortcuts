from shortcuts.actions.base import BaseAction, ChoiceField, Field, VariablesField


class DateAction(BaseAction):
    '''Date'''
    itype = 'is.workflow.actions.date'
    keyword = 'date'

    default_answer = VariablesField('WFAskActionDefaultAnswer', required=False)


class FormatDateAction(BaseAction):
    '''Format date'''
    itype = 'is.workflow.actions.format.date'
    keyword = 'format_date'

    format = Field('WFDateFormat')

    default_fields = {
        'WFDateFormatStyle': 'Custom',
    }


class DetectDateAction(BaseAction):
    '''Detect date'''
    itype = 'is.workflow.actions.detect.date'
    keyword = 'detect_date'


DATE_DIFF_UNITS_CHOICES = (
    'Total Time',
    'Seconds',
    'Minutes',
    'Hours',
    'Days',
    'Weeks',
    'Years',
    'Other',
)


class GetTimeBetweenDates(BaseAction):
    '''Get time difference between dates'''
    itype = 'is.workflow.actions.gettimebetweendates'
    keyword = 'get_time_between_dates'

    units = ChoiceField(
        'WFTimeUntilUnit', choices=DATE_DIFF_UNITS_CHOICES, default=DATE_DIFF_UNITS_CHOICES[0]
    )
    custom_date = Field('WFTimeUntilCustomDate', required=False)
