from shortcuts import Shortcut, FMT_SHORTCUT
from shortcuts.actions import (
    TextAction,
    SetVariableAction,
    IfAction,
    ElseAction,
    EndIfAction,
    VibrateAction,
    GetURLAction,
    NotificationAction,
)


class TestShortcutDumps:
    def test_dumps_simple_shortcut(self):
        sc = Shortcut(name='test')

        sc.actions = [
            SetVariableAction(data={'name': 'var2'}),
            TextAction(data={'text': 'simple text: {{var1}}'}),
            TextAction(data={'text': 'another text: {{var1}}'}),
        ]

        for action in sc.actions:
            action.id = 'id'

        exp_dump = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>WFWorkflowActions</key>\n\t<array>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.setvariable</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFVariableName</key>\n\t\t\t\t<string>var2</string>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.gettext</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFTextActionText</key>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t<dict>\n\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t<key>{13, 1}</key>\n\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t<key>Type</key>\n\t\t\t\t\t\t\t\t<string>Variable</string>\n\t\t\t\t\t\t\t\t<key>VariableName</key>\n\t\t\t\t\t\t\t\t<string>var1</string>\n\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t<string>simple text: ￼</string>\n\t\t\t\t\t</dict>\n\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t</dict>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.gettext</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFTextActionText</key>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t<dict>\n\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t<key>{14, 1}</key>\n\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t<key>Type</key>\n\t\t\t\t\t\t\t\t<string>Variable</string>\n\t\t\t\t\t\t\t\t<key>VariableName</key>\n\t\t\t\t\t\t\t\t<string>var1</string>\n\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t<string>another text: ￼</string>\n\t\t\t\t\t</dict>\n\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t</dict>\n\t\t\t</dict>\n\t\t</dict>\n\t</array>\n\t<key>WFWorkflowClientRelease</key>\n\t<string>2.0</string>\n\t<key>WFWorkflowClientVersion</key>\n\t<string>700</string>\n\t<key>WFWorkflowIcon</key>\n\t<dict>\n\t\t<key>WFWorkflowIconGlyphNumber</key>\n\t\t<integer>59511</integer>\n\t\t<key>WFWorkflowIconImageData</key>\n\t\t<data>\n\t\t</data>\n\t\t<key>WFWorkflowIconStartColor</key>\n\t\t<integer>431817727</integer>\n\t</dict>\n\t<key>WFWorkflowImportQuestions</key>\n\t<array/>\n\t<key>WFWorkflowInputContentItemClasses</key>\n\t<array>\n\t\t<string>WFAppStoreAppContentItem</string>\n\t\t<string>WFArticleContentItem</string>\n\t\t<string>WFContactContentItem</string>\n\t\t<string>WFDateContentItem</string>\n\t\t<string>WFEmailAddressContentItem</string>\n\t\t<string>WFGenericFileContentItem</string>\n\t\t<string>WFImageContentItem</string>\n\t\t<string>WFiTunesProductContentItem</string>\n\t\t<string>WFLocationContentItem</string>\n\t\t<string>WFDCMapsLinkContentItem</string>\n\t\t<string>WFAVAssetContentItem</string>\n\t\t<string>WFPDFContentItem</string>\n\t\t<string>WFPhoneNumberContentItem</string>\n\t\t<string>WFRichTextContentItem</string>\n\t\t<string>WFSafariWebPageContentItem</string>\n\t\t<string>WFStringContentItem</string>\n\t\t<string>WFURLContentItem</string>\n\t</array>\n\t<key>WFWorkflowTypes</key>\n\t<array>\n\t\t<string>NCWidget</string>\n\t\t<string>WatchKit</string>\n\t</array>\n</dict>\n</plist>\n'
        assert sc.dumps(file_format=FMT_SHORTCUT) == exp_dump


class TestShortcutLoads:
    def test_loads(self):
        toml_string = '''
            [[action]]
            type = "text"
            text = "ping"

            [[action]]
            type = "set_variable"
            name = "variable"

            [[action]]
            type = "show_result"
            text = "My variable: {{variable}}"
        '''
        sc = Shortcut.loads(toml_string)

        assert len(sc.actions) == 3

        assert sc.actions[0].keyword == 'text'
        assert sc.actions[0].data['text'] == 'ping'
        assert sc.actions[0].itype == 'is.workflow.actions.gettext'

        assert sc.actions[1].keyword == 'set_variable'
        assert sc.actions[1].data['name'] == 'variable'
        assert sc.actions[1].itype == 'is.workflow.actions.setvariable'

        assert sc.actions[2].keyword == 'show_result'
        assert sc.actions[2].data['text'] == 'My variable: {{variable}}'
        assert sc.actions[2].itype == 'is.workflow.actions.showresult'


class TestShortcutLoadsAndDumps:
    def test_loads_and_dumps_with_not_all_params(self):
        question = 'What is your name?'
        toml_string = f'''
            [[action]]
            type = "ask"
            question = "{question}"
        '''

        sc = Shortcut.loads(toml_string)

        assert len(sc.actions) == 1

        action = sc.actions[0]

        assert action.keyword == 'ask'
        assert action.data['question'] == question
        assert action.itype == 'is.workflow.actions.ask'

        assert action.data == {'question': question}

        dump = sc.dumps(file_format=FMT_SHORTCUT)

        exp_dump = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>WFWorkflowActions</key>\n\t<array>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.ask</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFAskActionPrompt</key>\n\t\t\t\t<string>What is your name?</string>\n\t\t\t</dict>\n\t\t</dict>\n\t</array>\n\t<key>WFWorkflowClientRelease</key>\n\t<string>2.0</string>\n\t<key>WFWorkflowClientVersion</key>\n\t<string>700</string>\n\t<key>WFWorkflowIcon</key>\n\t<dict>\n\t\t<key>WFWorkflowIconGlyphNumber</key>\n\t\t<integer>59511</integer>\n\t\t<key>WFWorkflowIconImageData</key>\n\t\t<data>\n\t\t</data>\n\t\t<key>WFWorkflowIconStartColor</key>\n\t\t<integer>431817727</integer>\n\t</dict>\n\t<key>WFWorkflowImportQuestions</key>\n\t<array/>\n\t<key>WFWorkflowInputContentItemClasses</key>\n\t<array>\n\t\t<string>WFAppStoreAppContentItem</string>\n\t\t<string>WFArticleContentItem</string>\n\t\t<string>WFContactContentItem</string>\n\t\t<string>WFDateContentItem</string>\n\t\t<string>WFEmailAddressContentItem</string>\n\t\t<string>WFGenericFileContentItem</string>\n\t\t<string>WFImageContentItem</string>\n\t\t<string>WFiTunesProductContentItem</string>\n\t\t<string>WFLocationContentItem</string>\n\t\t<string>WFDCMapsLinkContentItem</string>\n\t\t<string>WFAVAssetContentItem</string>\n\t\t<string>WFPDFContentItem</string>\n\t\t<string>WFPhoneNumberContentItem</string>\n\t\t<string>WFRichTextContentItem</string>\n\t\t<string>WFSafariWebPageContentItem</string>\n\t\t<string>WFStringContentItem</string>\n\t\t<string>WFURLContentItem</string>\n\t</array>\n\t<key>WFWorkflowTypes</key>\n\t<array>\n\t\t<string>NCWidget</string>\n\t\t<string>WatchKit</string>\n\t</array>\n</dict>\n</plist>\n'

        assert dump == exp_dump

    def test_loads_plist(self):
        plist = '<?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"> <plist version="1.0"> <dict> <key>WFWorkflowActions</key> <array> <dict> <key>WFWorkflowActionIdentifier</key> <string>is.workflow.actions.gettext</string> <key>WFWorkflowActionParameters</key> <dict> <key>WFTextActionText</key> <dict> <key>Value</key> <dict> <key>attachmentsByRange</key> <dict/> <key>string</key> <string>ping</string> </dict> <key>WFSerializationType</key> <string>WFTextTokenString</string> </dict> </dict> </dict> <dict> <key>WFWorkflowActionIdentifier</key> <string>is.workflow.actions.setvariable</string> <key>WFWorkflowActionParameters</key> <dict> <key>WFVariableName</key> <string>init</string> </dict> </dict> <dict> <key>WFWorkflowActionIdentifier</key> <string>is.workflow.actions.conditional</string> <key>WFWorkflowActionParameters</key> <dict> <key>GroupingIdentifier</key> <string>73C63251-8CE2-4DC2-A078-57CBBC823657</string> <key>WFCondition</key> <string>Equals</string> <key>WFConditionalActionString</key> <string>ping</string> <key>WFControlFlowMode</key> <integer>0</integer> </dict> </dict> <dict> <key>WFWorkflowActionIdentifier</key> <string>is.workflow.actions.gettext</string> <key>WFWorkflowActionParameters</key> <dict> <key>WFTextActionText</key> <dict> <key>Value</key> <dict> <key>attachmentsByRange</key> <dict/> <key>string</key> <string>test</string> </dict> <key>WFSerializationType</key> <string>WFTextTokenString</string> </dict> </dict> </dict> <dict> <key>WFWorkflowActionIdentifier</key> <string>is.workflow.actions.setvariable</string> <key>WFWorkflowActionParameters</key> <dict> <key>WFVariableName</key> <string>test</string> </dict> </dict> <dict> <key>WFWorkflowActionIdentifier</key> <string>is.workflow.actions.conditional</string> <key>WFWorkflowActionParameters</key> <dict> <key>GroupingIdentifier</key> <string>73C63251-8CE2-4DC2-A078-57CBBC823657</string> <key>WFControlFlowMode</key> <integer>1</integer> </dict> </dict> <dict> <key>WFWorkflowActionIdentifier</key> <string>is.workflow.actions.vibrate</string> <key>WFWorkflowActionParameters</key> <dict/> </dict> <dict> <key>WFWorkflowActionIdentifier</key> <string>is.workflow.actions.downloadurl</string> <key>WFWorkflowActionParameters</key> <dict> <key>Advanced</key> <true/> <key>ShowHeaders</key> <true/> <key>WFHTTPBodyType</key> <string>Json</string> <key>WFHTTPHeaders</key> <dict> <key>Value</key> <dict> <key>WFDictionaryFieldValueItems</key> <array> <dict> <key>WFItemType</key> <integer>0</integer> <key>WFKey</key> <dict> <key>Value</key> <dict> <key>attachmentsByRange</key> <dict/> <key>string</key> <string>Auth</string> </dict> <key>WFSerializationType</key> <string>WFTextTokenString</string> </dict> <key>WFValue</key> <dict> <key>Value</key> <dict> <key>attachmentsByRange</key> <dict/> <key>string</key> <string>token</string> </dict> <key>WFSerializationType</key> <string>WFTextTokenString</string> </dict> </dict> </array> </dict> <key>WFSerializationType</key> <string>WFDictionaryFieldValue</string> </dict> <key>WFHTTPMethod</key> <string>POST</string> <key>WFJSONValues</key> <dict> <key>Value</key> <dict> <key>WFDictionaryFieldValueItems</key> <array> <dict> <key>WFItemType</key> <integer>0</integer> <key>WFKey</key> <dict> <key>Value</key> <dict> <key>attachmentsByRange</key> <dict/> <key>string</key> <string>key1</string> </dict> <key>WFSerializationType</key> <string>WFTextTokenString</string> </dict> <key>WFValue</key> <dict> <key>Value</key> <dict> <key>attachmentsByRange</key> <dict> <key>{0, 1}</key> <dict> <key>Type</key> <string>Variable</string> <key>VariableName</key> <string>init</string> </dict> </dict> <key>string</key> <string>￼￼</string> </dict> <key>WFSerializationType</key> <string>WFTextTokenString</string> </dict> </dict> <dict> <key>WFItemType</key> <integer>0</integer> <key>WFKey</key> <dict> <key>Value</key> <dict> <key>attachmentsByRange</key> <dict/> <key>string</key> <string>key2</string> </dict> <key>WFSerializationType</key> <string>WFTextTokenString</string> </dict> <key>WFValue</key> <dict> <key>Value</key> <dict> <key>attachmentsByRange</key> <dict/> <key>string</key> <string>5</string> </dict> <key>WFSerializationType</key> <string>WFTextTokenString</string> </dict> </dict> </array> </dict> <key>WFSerializationType</key> <string>WFDictionaryFieldValue</string> </dict> </dict> </dict> <dict> <key>WFWorkflowActionIdentifier</key> <string>is.workflow.actions.conditional</string> <key>WFWorkflowActionParameters</key> <dict> <key>GroupingIdentifier</key> <string>73C63251-8CE2-4DC2-A078-57CBBC823657</string> <key>WFControlFlowMode</key> <integer>2</integer> </dict> </dict> <dict> <key>WFWorkflowActionIdentifier</key> <string>is.workflow.actions.notification</string> <key>WFWorkflowActionParameters</key> <dict> <key>WFNotificationActionBody</key> <dict> <key>Value</key> <dict> <key>attachmentsByRange</key> <dict> <key>{13, 1}</key> <dict> <key>Type</key> <string>Variable</string> <key>VariableName</key> <string>test</string> </dict> </dict> <key>string</key> <string>Hello World! ￼￼</string> </dict> <key>WFSerializationType</key> <string>WFTextTokenString</string> </dict> <key>WFNotificationActionSound</key> <false/> <key>WFNotificationActionTitle</key> <dict> <key>Value</key> <dict> <key>attachmentsByRange</key> <dict/> <key>string</key> <string>hi</string> </dict> <key>WFSerializationType</key> <string>WFTextTokenString</string> </dict> </dict> </dict> </array> <key>WFWorkflowClientRelease</key> <string>2.0</string> <key>WFWorkflowClientVersion</key> <string>700</string> <key>WFWorkflowIcon</key> <dict> <key>WFWorkflowIconGlyphNumber</key> <integer>59511</integer> <key>WFWorkflowIconImageData</key> <data> </data> <key>WFWorkflowIconStartColor</key> <integer>431817727</integer> </dict> <key>WFWorkflowImportQuestions</key> <array/> <key>WFWorkflowInputContentItemClasses</key> <array> <string>WFAppStoreAppContentItem</string> <string>WFArticleContentItem</string> <string>WFContactContentItem</string> <string>WFDateContentItem</string> <string>WFEmailAddressContentItem</string> <string>WFGenericFileContentItem</string> <string>WFImageContentItem</string> <string>WFiTunesProductContentItem</string> <string>WFLocationContentItem</string> <string>WFDCMapsLinkContentItem</string> <string>WFAVAssetContentItem</string> <string>WFPDFContentItem</string> <string>WFPhoneNumberContentItem</string> <string>WFRichTextContentItem</string> <string>WFSafariWebPageContentItem</string> <string>WFStringContentItem</string> <string>WFURLContentItem</string> </array> <key>WFWorkflowTypes</key> <array> <string>NCWidget</string> <string>WatchKit</string> </array> </dict> </plist>'

        sc = Shortcut.loads(plist, file_format=FMT_SHORTCUT)

        exp_actions = [
            TextAction,
            SetVariableAction,
            IfAction,
            TextAction,
            SetVariableAction,
            ElseAction,
            VibrateAction,
            GetURLAction,
            EndIfAction,
            NotificationAction,
        ]

        assert [type(a) for a in sc.actions] == exp_actions


class TestShortcut:
    def test_set_group_ids_for_empty_shortcut(self):
        sc = Shortcut()

        assert len(sc.actions) == 0
        sc._set_group_ids()
        assert len(sc.actions) == 0

    def test_set_group_ids(self):
        # test that _set_group_ids sets group_ids correctly
        sc = Shortcut()
        sc.actions = [
            IfAction(data={'condition': 'equals', 'compare_with': 'test'}),

            IfAction(data={'condition': 'equals', 'compare_with': 'test'}),
            EndIfAction(data={}),

            ElseAction(data={}),
            # pass
            EndIfAction(data={}),
        ]

        # all actions are without group_id info
        assert any([a.data.get('group_id') for a in sc.actions]) is False

        sc._set_group_ids()

        # now all actions are with group_id info
        assert all([a.data.get('group_id') for a in sc.actions]) is True

        # first cycle check
        assert sc.actions[0].data['group_id'] == sc.actions[3].data['group_id'] == sc.actions[4].data['group_id']

        # second cycle
        assert sc.actions[1].data['group_id'] == sc.actions[2].data['group_id']

        # ids are different
        assert sc.actions[0].data['group_id'] != sc.actions[1].data['group_id']
