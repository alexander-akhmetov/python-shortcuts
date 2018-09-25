from shortcuts.actions.base import BaseAction, ChoiceField, Field, GroupIDField


IF_CHOICES = (
    'Equals',
    'Contains',
)


class IfAction(BaseAction):
    '''If'''
    itype = 'is.workflow.actions.conditional'
    keyword = 'if'

    condition = ChoiceField('WFCondition', choices=IF_CHOICES, capitalize=True)
    compare_with = Field('WFConditionalActionString')
    group_id = GroupIDField('GroupingIdentifier')

    default_fields = {
        'WFControlFlowMode': 0,
    }


class ElseAction(BaseAction):
    '''Else'''
    itype = 'is.workflow.actions.conditional'
    keyword = 'else'

    group_id = GroupIDField('GroupingIdentifier')

    default_fields = {
        'WFControlFlowMode': 1,
    }


class EndIfAction(BaseAction):
    '''EndIf: end a condition'''
    itype = 'is.workflow.actions.conditional'
    keyword = 'endif'

    group_id = GroupIDField('GroupingIdentifier')

    default_fields = {
        'WFControlFlowMode': 2,
    }
