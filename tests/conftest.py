from shortcuts import Shortcut, FMT_SHORTCUT

from tests.templates import SHORTCUT_EMPTY_PLIST_TEMPLATE


class ActionTomlLoadsMixin:
    def _assert_toml_loads(self, toml, exp_cls, exp_data):
        sc = Shortcut.loads(toml)

        assert len(sc.actions) == 1

        action = sc.actions[0]
        assert isinstance(sc.actions[0], exp_cls) is True

        assert action.data == exp_data


class SimpleBaseDumpsLoadsTest(ActionTomlLoadsMixin):
    action_class = None
    itype = None
    toml = None
    action_xml = None

    def test_dumps(self):
        action = self.action_class()
        exp_dump = {
            'WFWorkflowActionIdentifier': self.itype,
            'WFWorkflowActionParameters': {}
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        self._assert_toml_loads(self.toml, self.action_class, {})

    def test_loads_plist(self):
        plist = SHORTCUT_EMPTY_PLIST_TEMPLATE.format(actions=self.action_xml.strip())
        plist = plist.replace('    ', '').replace('\n', '')  # remove all indentation
        sc = Shortcut.loads(plist, file_format=FMT_SHORTCUT)

        assert len(sc.actions) == 1
        assert isinstance(sc.actions[0], self.action_class) is True
