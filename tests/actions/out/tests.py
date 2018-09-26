from shortcuts.actions import ShowResultAction, ShowAlertAction, SetClipboardAction

from tests.conftest import ActionTomlLoadsMixin


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
                        '{2, 1}': {'Type': 'Variable', 'VariableName': 'v2'},
                    },
                    'string': '￼##￼',
                },
                'WFSerializationType': 'WFTextTokenString',
            },
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


class TestSetClipboardAction(ActionTomlLoadsMixin):

    def test_dumps(self):
        action = SetClipboardAction()
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.setclipboard',
            'WFWorkflowActionParameters': {}
        }
        assert action.dump() == exp_dump

    def test_dumps_with_parameters(self):
        expiration_date = 'Tomorrow at 2am'
        local_only = True
        action = SetClipboardAction(data={'local_only': local_only, 'expiration_date': expiration_date})
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.setclipboard',
            'WFWorkflowActionParameters': {
                'WFLocalOnly': local_only,
                'WFExpirationDate': expiration_date,
            }
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        toml = '''
        [[action]]
        type = "set_clipboard"
        '''
        self._assert_toml_loads(toml, SetClipboardAction, {})

    def test_loads_toml_with_parameters(self):
        toml = '''
        [[action]]
        type = "set_clipboard"
        expiration_date = "tomorrow"
        local_only = false
        '''
        self._assert_toml_loads(
            toml,
            SetClipboardAction,
            {'local_only': False, 'expiration_date': 'tomorrow'},
        )
