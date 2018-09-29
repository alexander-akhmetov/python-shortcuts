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

    dump_data = None
    dump_params = None

    toml = None
    exp_toml_params = None

    action_xml = None
    exp_xml_params = None

    def test_dumps(self):
        action = self.action_class(data=self.dump_data)
        dump_params = self.dump_params if self.dump_params else {}
        exp_dump = {
            'WFWorkflowActionIdentifier': self.itype,
            'WFWorkflowActionParameters': dump_params,
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        exp_params = self.exp_toml_params if self.exp_toml_params else {}
        self._assert_toml_loads(self.toml, self.action_class, exp_params)

    def test_loads_plist(self):
        plist = SHORTCUT_EMPTY_PLIST_TEMPLATE.format(actions=self.action_xml.strip())
        plist = plist.replace('    ', '').replace('\n', '')  # remove all indentation
        sc = Shortcut.loads(plist, file_format=FMT_SHORTCUT)

        assert len(sc.actions) == 1
        assert isinstance(sc.actions[0], self.action_class) is True

        exp_params = self.exp_xml_params if self.exp_xml_params else {}
        assert sc.actions[0].data == exp_params
