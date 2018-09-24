from shortcuts.actions import (
    NothingAction,
    SetItemNameAction,
    ViewContentGraphAction,
    ContinueInShortcutAppAction,
    DelayAction,
    WaitToReturnAction,
)

from tests.conftest import ActionTomlLoadsMixin


class TestNothingAction(ActionTomlLoadsMixin):
    def test_dumps(self):
        action = NothingAction()
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.nothing',
            'WFWorkflowActionParameters': {}
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        toml = '''
        [[action]]
        type = "nothing"
        '''
        self._assert_toml_loads(toml, NothingAction, {})


class TestSetItemNameAction(ActionTomlLoadsMixin):
    def test_dumps(self):
        action = SetItemNameAction()
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.setitemname',
            'WFWorkflowActionParameters': {}
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        toml = '''
        [[action]]
        type = "set_item_name"
        '''
        self._assert_toml_loads(toml, SetItemNameAction, {})


class TestViewContentGraphAction(ActionTomlLoadsMixin):
    def test_dumps(self):
        action = ViewContentGraphAction()
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.viewresult',
            'WFWorkflowActionParameters': {}
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        toml = '''
        [[action]]
        type = "view_content_graph"
        '''
        self._assert_toml_loads(toml, ViewContentGraphAction, {})


class TestContinueInShortcutAppAction(ActionTomlLoadsMixin):
    def test_dumps(self):
        action = ContinueInShortcutAppAction()
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.handoff',
            'WFWorkflowActionParameters': {}
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        toml = '''
        [[action]]
        type = "continue_in_shortcut_app"
        '''
        self._assert_toml_loads(toml, ContinueInShortcutAppAction, {})


class TestDelayAction(ActionTomlLoadsMixin):
    def test_dumps(self):
        action = DelayAction(data={'time': 0.75})
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.delay',
            'WFWorkflowActionParameters': {'WFDelayTime': 0.75},
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        toml = '''
        [[action]]
        type = "delay"
        time = 0.58
        '''
        self._assert_toml_loads(toml, DelayAction, {'time': 0.58})


class TestWaitToReturnAction(ActionTomlLoadsMixin):
    def test_dumps(self):
        action = WaitToReturnAction()
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.waittoreturn',
            'WFWorkflowActionParameters': {}
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        toml = '''
        [[action]]
        type = "wait_to_return"
        '''
        self._assert_toml_loads(toml, WaitToReturnAction, {})
