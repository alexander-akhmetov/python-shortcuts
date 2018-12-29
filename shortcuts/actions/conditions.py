from shortcuts.actions.base import BaseAction, ChoiceField, GroupIDField, VariablesField


IF_CHOICES = (
    'Equals',
    'Contains',
)


class IfAction(BaseAction):
    '''If'''
    itype = 'is.workflow.actions.conditional'
    keyword = 'if'

    _additional_identifier_field = 'WFControlFlowMode'

    condition = ChoiceField(
        'WFCondition', choices=IF_CHOICES, capitalize=True, default=IF_CHOICES[0]
    )
    compare_with = VariablesField('WFConditionalActionString')
    group_id = GroupIDField('GroupingIdentifier')

    default_fields = {
        'WFControlFlowMode': 0,
    }


class ElseAction(BaseAction):
    '''Else'''
    itype = 'is.workflow.actions.conditional'
    keyword = 'else'

    _additional_identifier_field = 'WFControlFlowMode'

    group_id = GroupIDField('GroupingIdentifier')

    default_fields = {
        'WFControlFlowMode': 1,
    }


class EndIfAction(BaseAction):
    '''EndIf: end a condition'''
    itype = 'is.workflow.actions.conditional'
    keyword = 'endif'

    _additional_identifier_field = 'WFControlFlowMode'

    group_id = GroupIDField('GroupingIdentifier')

    default_fields = {
        'WFControlFlowMode': 2,
    }
