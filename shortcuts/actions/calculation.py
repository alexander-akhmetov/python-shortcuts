from shortcuts.actions.base import BaseAction, Field


class CountAction(BaseAction):
    '''Count'''
    itype = 'is.workflow.actions.count'
    keyword = 'count'

    count = Field('WFCountType', capitalize=True)
