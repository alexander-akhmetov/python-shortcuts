from shortcuts import Shortcut
from shortcuts.actions import TextAction, SetVariableAction


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

        exp_dump = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>WFWorkflowActions</key>\n\t<array>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.setvariable</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFVariableName</key>\n\t\t\t\t<string>var2</string>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.gettext</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t<key>WFTextActionText</key>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t<dict>\n\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t<key>{13, 1}</key>\n\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t<key>Type</key>\n\t\t\t\t\t\t\t\t<string>Variable</string>\n\t\t\t\t\t\t\t\t<key>VariableName</key>\n\t\t\t\t\t\t\t\t<string>var1</string>\n\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t<string>simple text: ￼</string>\n\t\t\t\t\t</dict>\n\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t</dict>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.gettext</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t<key>WFTextActionText</key>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t<dict>\n\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t<key>{14, 1}</key>\n\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t<key>Type</key>\n\t\t\t\t\t\t\t\t<string>Variable</string>\n\t\t\t\t\t\t\t\t<key>VariableName</key>\n\t\t\t\t\t\t\t\t<string>var1</string>\n\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t<string>another text: ￼</string>\n\t\t\t\t\t</dict>\n\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t</dict>\n\t\t\t</dict>\n\t\t</dict>\n\t</array>\n\t<key>WFWorkflowClientRelease</key>\n\t<string>2.0</string>\n\t<key>WFWorkflowClientVersion</key>\n\t<string>700</string>\n\t<key>WFWorkflowIcon</key>\n\t<dict>\n\t\t<key>WFWorkflowIconGlyphNumber</key>\n\t\t<integer>59511</integer>\n\t\t<key>WFWorkflowIconImageData</key>\n\t\t<data>\n\t\t</data>\n\t\t<key>WFWorkflowIconStartColor</key>\n\t\t<integer>431817727</integer>\n\t</dict>\n\t<key>WFWorkflowImportQuestions</key>\n\t<array/>\n\t<key>WFWorkflowInputContentItemClasses</key>\n\t<array>\n\t\t<string>WFAppStoreAppContentItem</string>\n\t\t<string>WFArticleContentItem</string>\n\t\t<string>WFContactContentItem</string>\n\t\t<string>WFDateContentItem</string>\n\t\t<string>WFEmailAddressContentItem</string>\n\t\t<string>WFGenericFileContentItem</string>\n\t\t<string>WFImageContentItem</string>\n\t\t<string>WFiTunesProductContentItem</string>\n\t\t<string>WFLocationContentItem</string>\n\t\t<string>WFDCMapsLinkContentItem</string>\n\t\t<string>WFAVAssetContentItem</string>\n\t\t<string>WFPDFContentItem</string>\n\t\t<string>WFPhoneNumberContentItem</string>\n\t\t<string>WFRichTextContentItem</string>\n\t\t<string>WFSafariWebPageContentItem</string>\n\t\t<string>WFStringContentItem</string>\n\t\t<string>WFURLContentItem</string>\n\t</array>\n\t<key>WFWorkflowTypes</key>\n\t<array>\n\t\t<string>NCWidget</string>\n\t\t<string>WatchKit</string>\n\t</array>\n</dict>\n</plist>\n'
        assert sc.dumps() == exp_dump


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

        dump = sc.dumps()

        exp_dump = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>WFWorkflowActions</key>\n\t<array>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.ask</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFAskActionPrompt</key>\n\t\t\t\t<string>What is your name?</string>\n\t\t\t</dict>\n\t\t</dict>\n\t</array>\n\t<key>WFWorkflowClientRelease</key>\n\t<string>2.0</string>\n\t<key>WFWorkflowClientVersion</key>\n\t<string>700</string>\n\t<key>WFWorkflowIcon</key>\n\t<dict>\n\t\t<key>WFWorkflowIconGlyphNumber</key>\n\t\t<integer>59511</integer>\n\t\t<key>WFWorkflowIconImageData</key>\n\t\t<data>\n\t\t</data>\n\t\t<key>WFWorkflowIconStartColor</key>\n\t\t<integer>431817727</integer>\n\t</dict>\n\t<key>WFWorkflowImportQuestions</key>\n\t<array/>\n\t<key>WFWorkflowInputContentItemClasses</key>\n\t<array>\n\t\t<string>WFAppStoreAppContentItem</string>\n\t\t<string>WFArticleContentItem</string>\n\t\t<string>WFContactContentItem</string>\n\t\t<string>WFDateContentItem</string>\n\t\t<string>WFEmailAddressContentItem</string>\n\t\t<string>WFGenericFileContentItem</string>\n\t\t<string>WFImageContentItem</string>\n\t\t<string>WFiTunesProductContentItem</string>\n\t\t<string>WFLocationContentItem</string>\n\t\t<string>WFDCMapsLinkContentItem</string>\n\t\t<string>WFAVAssetContentItem</string>\n\t\t<string>WFPDFContentItem</string>\n\t\t<string>WFPhoneNumberContentItem</string>\n\t\t<string>WFRichTextContentItem</string>\n\t\t<string>WFSafariWebPageContentItem</string>\n\t\t<string>WFStringContentItem</string>\n\t\t<string>WFURLContentItem</string>\n\t</array>\n\t<key>WFWorkflowTypes</key>\n\t<array>\n\t\t<string>NCWidget</string>\n\t\t<string>WatchKit</string>\n\t</array>\n</dict>\n</plist>\n'

        assert dump == exp_dump
