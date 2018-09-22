from shortcuts.actions.base import BaseAction, Field


class URLAction(BaseAction):
    '''URL: returns url as an output'''
    type = 'is.workflow.actions.url'
    keyword = 'url'

    url = Field('WFURLActionURL')
