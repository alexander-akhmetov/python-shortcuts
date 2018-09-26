from shortcuts.actions.base import BaseAction, FloatField


class NumberAction(BaseAction):
    itype = 'is.workflow.actions.number'
    keyword = 'number'

    number = FloatField('WFNumberActionNumber')
