from shortcuts.actions.base import BaseAction, Field


class IfAction(BaseAction):
    '''If: you must specify group_id of this if condition'''
    type = 'is.workflow.actions.conditional'
    keyword = 'if'

    condition = Field('WFCondition', capitalize=True)
    compare_with = Field('WFConditionalActionString')
    group_id = Field('GroupingIdentifier')

    default_fields = {
        'WFControlFlowMode': 0,
    }


class ElseAction(BaseAction):
    '''Else: else for a specified group_id'''
    type = 'is.workflow.actions.conditional'
    keyword = 'else'

    group_id = Field('GroupingIdentifier')

    default_fields = {
        'WFControlFlowMode': 1,
    }


class EndIfAction(BaseAction):
    '''EndIf: end a condition with specified group_id'''
    type = 'is.workflow.actions.conditional'
    keyword = 'endif'

    group_id = Field('GroupingIdentifier')

    default_fields = {
        'WFControlFlowMode': 2,
    }
