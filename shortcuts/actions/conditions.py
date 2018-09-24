from shortcuts.actions.base import BaseAction, ChoiceField, Field, GroupIDField


class IfAction(BaseAction):
    '''If: you must specify group_id of this if condition'''
    itype = 'is.workflow.actions.conditional'
    keyword = 'if'

    condition = ChoiceField('WFCondition', choices=('Equals', 'Contains'), capitalize=True)
    compare_with = Field('WFConditionalActionString')
    group_id = GroupIDField('GroupingIdentifier')

    default_fields = {
        'WFControlFlowMode': 0,
    }


class ElseAction(BaseAction):
    '''Else: else for a specified group_id'''
    itype = 'is.workflow.actions.conditional'
    keyword = 'else'

    group_id = GroupIDField('GroupingIdentifier')

    default_fields = {
        'WFControlFlowMode': 1,
    }


class EndIfAction(BaseAction):
    '''EndIf: end a condition with specified group_id'''
    itype = 'is.workflow.actions.conditional'
    keyword = 'endif'

    group_id = GroupIDField('GroupingIdentifier')

    default_fields = {
        'WFControlFlowMode': 2,
    }
