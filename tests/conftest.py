from shortcuts import Shortcut


class ActionTomlLoadsMixin:
    def _assert_toml_loads(self, toml, exp_cls, exp_data):
        sc = Shortcut.loads(toml)

        assert len(sc.actions) == 1

        action = sc.actions[0]
        assert isinstance(sc.actions[0], exp_cls) is True

        assert action.data == exp_data
