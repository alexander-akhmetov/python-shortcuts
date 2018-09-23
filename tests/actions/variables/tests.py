from shortcuts.actions.variables import SetVariableAction


class TestSetVariable:
    def test_get_parameters(self):
        name = 'var'
        set_action = SetVariableAction(data={'name': name})

        dump = set_action._get_parameters()

        exp_dump = {
            'WFVariableName': name,
        }
        assert dump == exp_dump

