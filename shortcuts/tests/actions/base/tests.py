from actions.base import BaseAction
from actions.variables import SetVariableAction
from actions.out import (
    ShowResultAction,
    ShowAlertAction,
)
from actions.web import URLAction


class TestBaseAction:
    def test_get_parameters(self):
        base_action = BaseAction()
        base_action.type = '123'
        dump = base_action.dumps()

        exp_dump = {
            'WFWorkflowActionIdentifier': base_action.type,
            'WFWorkflowActionParameters': {},
        }
        assert dump == exp_dump


class TestSetVariable:
    def test_get_parameters(self):
        name = 'var'
        set_action = SetVariableAction(data={'name': name})

        dump = set_action._get_parameters()

        exp_dump = {
            'WFVariableName': name,
        }
        assert dump == exp_dump


class TestShowResultAction:
    def test_get_parameters(self):
        text = '{{v1}}##{{v2}}'
        action = ShowResultAction(data={'text': text})

        dump = action._get_parameters()

        exp_dump = {
            'Text': {
                'Value': {
                    'attachmentsByRange': {
                        '{0, 1}': {'Type': 'Variable', 'VariableName': 'v1'},
                        '{3, 1}': {'Type': 'Variable', 'VariableName': 'v2'},
                    },
                    'string': '￼##￼',
                },
                'WFSerializationType': 'WFTextTokenString',
            },
            'WFSerializationType': 'WFTextTokenString',
        }
        assert dump == exp_dump


class TestShowAlertAction:
    def test_get_parameters(self):
        title = 'some title'
        text = 'some text'
        show_cancel_button = True
        action = ShowAlertAction(
            dict(title=title, text=text, show_cancel_button=show_cancel_button)
        )

        dump = action._get_parameters()

        exp_dump = {
            'WFAlertActionCancelButtonShown': show_cancel_button,
            'WFAlertActionMessage': text,
            'WFAlertActionTitle': title,
        }
        assert dump == exp_dump


class TestURLAction:
    def test_get_parameters(self):
        url = 'https://aleks.sh'
        action = URLAction(data={'url': url})

        dump = action._get_parameters()

        exp_dump = {
            'WFURLActionURL': url,
        }
        assert dump == exp_dump
