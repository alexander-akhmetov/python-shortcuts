from shortcuts.actions.base import BaseAction, Field, WFVariableField


class SetVariableAction(BaseAction):
    '''Set variable: saves input to a variable with a name=`name`'''
    type = 'is.workflow.actions.setvariable'
    keyword = 'set_variable'

    name = Field('WFVariableName')


class GetVariableAction(BaseAction):
    '''Get variable: returns variable with name=`name` in the output'''
    type = 'is.workflow.actions.getvariable'
    keyword = 'get_variable'

    name = WFVariableField('WFVariable')
