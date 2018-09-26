from shortcuts.actions.base import BaseAction
from shortcuts.actions.registry import ActionsRegistry


class SimpleTestAction(BaseAction):
    itype = 'sh.aleks.simple_action'
    keyword = 'simple_action'


class IfTestAction(BaseAction):
    itype = 'sh.aleks.if'
    keyword = 'if'

    _additional_identifier_field = 'WFControlFlowMode'

    default_fields = {
        'WFControlFlowMode': 0,
    }


class ElseTestAction(BaseAction):
    itype = 'sh.aleks.if'
    keyword = 'else'

    _additional_identifier_field = 'WFControlFlowMode'

    default_fields = {
        'WFControlFlowMode': 1,
    }


class TestActionsRegistry:
    def test_init(self):
        registry = ActionsRegistry()

        assert registry._keyword_to_action_map == {}
        assert registry._itype_to_action_map == {}

    def test_register_simple_action(self):
        registry = ActionsRegistry()

        registry.register_action(SimpleTestAction)

        # check that get methods work
        assert registry.get_by_itype(SimpleTestAction.itype, action_params=None) == SimpleTestAction
        assert registry.get_by_keyword(SimpleTestAction.keyword) == SimpleTestAction

        # check internal structures
        assert registry._keyword_to_action_map == {
            'simple_action': SimpleTestAction,
        }
        assert registry._itype_to_action_map == {
            'sh.aleks.simple_action': {
                'type': 'class',
                'value': SimpleTestAction,
            }
        }

    def test_register_complex_action(self):
        # check registration of complex action: two actions with the same itype
        # but different fields
        registry = ActionsRegistry()

        registry.register_action(IfTestAction)
        registry.register_action(ElseTestAction)

        # check that get methods work
        params = {
            'WFWorkflowActionParameters': {
                'WFControlFlowMode': IfTestAction.default_fields['WFControlFlowMode'],
            }
        }
        assert registry.get_by_itype(IfTestAction.itype, action_params=params) == IfTestAction
        assert registry.get_by_keyword(IfTestAction.keyword) == IfTestAction

        params = {
            'WFWorkflowActionParameters': {
                'WFControlFlowMode': ElseTestAction.default_fields['WFControlFlowMode'],
            }
        }
        assert registry.get_by_itype(ElseTestAction.itype, action_params=params) == ElseTestAction
        assert registry.get_by_keyword(ElseTestAction.keyword) == ElseTestAction

        # check internal structures
        assert registry._keyword_to_action_map == {
            'if': IfTestAction,
            'else': ElseTestAction,
        }
        assert registry._itype_to_action_map == {
            'sh.aleks.if': {
                'type': 'property_based',
                'field': 'WFControlFlowMode',
                'value': {
                    0: IfTestAction,
                    1: ElseTestAction,
                },
            },
        }

    def test_actions(self):
        registry = ActionsRegistry()

        # before it's empty
        assert registry.actions == []

        registry.register_action(SimpleTestAction)

        assert registry.actions == [SimpleTestAction]

    def test_create_class_field_if_needed(self):
        registry = ActionsRegistry()
        assert registry._itype_to_action_map == {}

        registry._create_class_field_if_needed(IfTestAction)

        assert registry._itype_to_action_map == {
            'sh.aleks.if': {
                'type': 'property_based',
                'field': 'WFControlFlowMode',
                'value': {},
            },
        }
