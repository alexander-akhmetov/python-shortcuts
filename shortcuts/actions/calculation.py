from shortcuts.actions.base import BaseAction, Field


class CountAction(BaseAction):
    '''Count'''
    type = 'is.workflow.actions.count'
    keyword = 'count'

    count = Field('WFCountType', capitalize=True)
