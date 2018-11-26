import pytest
import mock

from shortcuts.actions import (
    NothingAction,
    SetItemNameAction,
    ViewContentGraphAction,
    ContinueInShortcutAppAction,
    DelayAction,
    WaitToReturnAction,
    RepeatEachStartAction,
    RepeatEachEndAction,
    HashAction,
    GetMyShortcutsAction,
    RunShortcutAction,
    ChooseFromListAction,
    OpenAppAction
)
from shortcuts.actions.scripting import HASH_CHOICES
from shortcuts import Shortcut, FMT_SHORTCUT

from tests.conftest import ActionTomlLoadsMixin, SimpleBaseDumpsLoadsTest


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


class TestRepeatWithEachActions:
    toml_string = '''
        [[action]]
        type = "repeat_with_each_start"

        [[action]]
        type = "repeat_with_each_end"
    '''

    def test_loads_from_toml(self):
        sc = Shortcut.loads(self.toml_string)

        assert len(sc.actions) == 2

        assert isinstance(sc.actions[0], RepeatEachStartAction) is True
        assert isinstance(sc.actions[1], RepeatEachEndAction) is True

    def test_dumps_to_plist(self):
        sc = Shortcut.loads(self.toml_string)

        mocked_uuid = mock.Mock()
        mocked_uuid.uuid4.return_value = 'some-uuid'

        with mock.patch('shortcuts.shortcut.uuid', mocked_uuid):
            dump = sc.dumps(file_format=FMT_SHORTCUT)

        exp_dump = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>WFWorkflowActions</key>\n\t<array>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.repeat.each</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>GroupingIdentifier</key>\n\t\t\t\t<string>some-uuid</string>\n\t\t\t\t<key>WFControlFlowMode</key>\n\t\t\t\t<integer>0</integer>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.repeat.each</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>GroupingIdentifier</key>\n\t\t\t\t<string>some-uuid</string>\n\t\t\t\t<key>WFControlFlowMode</key>\n\t\t\t\t<integer>2</integer>\n\t\t\t</dict>\n\t\t</dict>\n\t</array>\n\t<key>WFWorkflowClientRelease</key>\n\t<string>2.0</string>\n\t<key>WFWorkflowClientVersion</key>\n\t<string>700</string>\n\t<key>WFWorkflowIcon</key>\n\t<dict>\n\t\t<key>WFWorkflowIconGlyphNumber</key>\n\t\t<integer>59511</integer>\n\t\t<key>WFWorkflowIconImageData</key>\n\t\t<data>\n\t\t</data>\n\t\t<key>WFWorkflowIconStartColor</key>\n\t\t<integer>431817727</integer>\n\t</dict>\n\t<key>WFWorkflowImportQuestions</key>\n\t<array/>\n\t<key>WFWorkflowInputContentItemClasses</key>\n\t<array>\n\t\t<string>WFAppStoreAppContentItem</string>\n\t\t<string>WFArticleContentItem</string>\n\t\t<string>WFContactContentItem</string>\n\t\t<string>WFDateContentItem</string>\n\t\t<string>WFEmailAddressContentItem</string>\n\t\t<string>WFGenericFileContentItem</string>\n\t\t<string>WFImageContentItem</string>\n\t\t<string>WFiTunesProductContentItem</string>\n\t\t<string>WFLocationContentItem</string>\n\t\t<string>WFDCMapsLinkContentItem</string>\n\t\t<string>WFAVAssetContentItem</string>\n\t\t<string>WFPDFContentItem</string>\n\t\t<string>WFPhoneNumberContentItem</string>\n\t\t<string>WFRichTextContentItem</string>\n\t\t<string>WFSafariWebPageContentItem</string>\n\t\t<string>WFStringContentItem</string>\n\t\t<string>WFURLContentItem</string>\n\t</array>\n\t<key>WFWorkflowTypes</key>\n\t<array>\n\t\t<string>NCWidget</string>\n\t\t<string>WatchKit</string>\n\t</array>\n</dict>\n</plist>\n'
        assert dump == exp_dump


class TestHashAction(ActionTomlLoadsMixin):
    @pytest.mark.parametrize('hash_type', [
        *HASH_CHOICES,
    ])
    def test_dumps_with_choices(self, hash_type):
        action = HashAction(data={'hash_type': hash_type})
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.hash',
            'WFWorkflowActionParameters': {
                'WFHashType': hash_type,
            }
        }
        assert action.dump() == exp_dump

    @pytest.mark.parametrize('hash_type', [
        *HASH_CHOICES,
    ])
    def test_loads_toml(self, hash_type):
        toml = f'''
        [[action]]
        type = "hash"
        hash_type = "{hash_type}"
        '''
        self._assert_toml_loads(toml, HashAction, {'hash_type': hash_type})

    def test_choices(self):
        exp_choices = (
            'MD5',
            'SHA1',
            'SHA256',
            'SHA512',
        )
        assert HASH_CHOICES == exp_choices


class TestGetMyShortcutsAction(SimpleBaseDumpsLoadsTest):
    action_class = GetMyShortcutsAction
    itype = 'is.workflow.actions.getmyworkflows'
    toml = '[[action]]\ntype = "get_my_shortcuts"'
    action_xml = '''
      <dict>
        <key>WFWorkflowActionIdentifier</key>
        <string>is.workflow.actions.getmyworkflows</string>
        <key>WFWorkflowActionParameters</key>
        <dict></dict>
      </dict>
    '''


class TestChooseFromListAction(SimpleBaseDumpsLoadsTest):
    action_class = ChooseFromListAction
    itype = 'is.workflow.actions.choosefromlist'
    dump_data = {'select_multiple': False, 'select_all_initially': False}
    dump_params = {'WFChooseFromListActionSelectMultiple': False, 'WFChooseFromListActionSelectAll': False}
    toml = '''
        [[action]] 
         type = "choose_from_list"
         prompt = "test"
           '''
    exp_toml_params = {'prompt': 'test'}
    action_xml = '''
    <dict>
    <key>WFWorkflowActionIdentifier</key>
            <string>is.workflow.actions.choosefromlist</string>
            <key>WFWorkflowActionParameters</key>
            <dict>
                <key>WFChooseFromListActionPrompt</key>
                <string>test</string>
                <key>WFChooseFromListActionSelectAll</key>
                <true/>
                <key>WFChooseFromListActionSelectMultiple</key>
                <true/>
            </dict>
    </dict>
    '''
    exp_xml_params = {'select_all_initially': True, 'select_multiple': True, 'prompt': 'test'}


class TestOpenAppAction(SimpleBaseDumpsLoadsTest):
    action_class = OpenAppAction
    itype = 'is.workflow.actions.openapp'

    dump_data = {'app': 'com.apple.camera'}
    dump_params = {
        'WFAppIdentifier': 'com.apple.camera'
    }
    
    toml = '''
        [[action]] 
         type = "open_app"
         app = "com.apple.camera"
    '''
    exp_toml_params = {'app': 'com.apple.camera'}

    action_xml = '''
      <dict>
        <key>WFWorkflowActionIdentifier</key>
        <string>is.workflow.actions.openapp</string>
        <key>WFWorkflowActionParameters</key>
        <dict>
            <key>WFAppIdentifier</key>
            <string>com.apple.camera</string>
        </dict>
      </dict>
    '''
    exp_xml_params = {'app': 'com.apple.camera'}


class TestRunShortcut(SimpleBaseDumpsLoadsTest):
    action_class = RunShortcutAction
    itype = 'is.workflow.actions.runworkflow'

    dump_data = {'shortcut_name': 'test', 'show': False}
    dump_params = {
        'WFShowWorkflow': False,
        'WFWorkflowName': 'test',
    }

    toml = '''
    [[action]]
    type = "run_shortcut"
    shortcut_name = "test_shortcut"
    '''
    exp_toml_params = {'shortcut_name': 'test_shortcut'}

    action_xml = '''
      <dict>
        <key>WFWorkflowActionIdentifier</key>
        <string>is.workflow.actions.runworkflow</string>
        <key>WFWorkflowActionParameters</key>
        <dict>
        <key>WFWorkflowName</key>
        <string>mywf</string>
        <key>WFShowWorkflow</key>
        <true/>
        </dict>
      </dict>
    '''
    exp_xml_params = {'shortcut_name': 'mywf', 'show': True}
