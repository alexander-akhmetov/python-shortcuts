from shortcuts.actions import NumberAction

from tests.conftest import ActionTomlLoadsMixin


class TestNumberAction(ActionTomlLoadsMixin):
    def test_dumps(self):
        number = 0.56
        action = NumberAction(data={'number': number})
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.number',
            'WFWorkflowActionParameters': {
                'WFNumberActionNumber': number,
            }
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        number = 15.5
        toml = f'''
        [[action]]
        type = "number"
        number = {number}
        '''
        self._assert_toml_loads(toml, NumberAction, {'number': number})
