from shortcuts.actions import GetClipboardAction

from tests.conftest import ActionTomlLoadsMixin


class TestGetClipboardAction(ActionTomlLoadsMixin):
    def test_dumps(self):
        action = GetClipboardAction()
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.getclipboard',
            'WFWorkflowActionParameters': {}
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        toml = '''
        [[action]]
        type = "get_clipboard"
        '''
        self._assert_toml_loads(toml, GetClipboardAction, {})
