from shortcuts.actions.base import BaseAction, Field


class SetVariableAction(BaseAction):
    '''Set variable: saves input to a variable with a name=`name`'''
    type = 'is.workflow.actions.setvariable'
    keyword = 'set_variable'

    name = Field('WFVariableName')
