from shortcuts import Shortcut


class TestConditionalAction:
    toml_string = '''
        [[action]]
        type = "if"
        condition = "equals"
        compare_with = "true"
        group_id = "123"

        [[action]]
        type = "else"
        group_id = "123"

        [[action]]
        type = "endif"
        group_id = "123"
    '''

    def test_loads_from_toml(self):
        sc = Shortcut.loads(self.toml_string)

        assert len(sc.actions) == 3

        if_action = sc.actions[0]
        else_action = sc.actions[1]
        endif_action = sc.actions[2]

        assert if_action.data == {'compare_with': 'true', 'condition': 'equals', 'group_id': '123'}
        assert else_action.data == {'group_id': '123'}
        assert endif_action.data == {'group_id': '123'}

    def test_dumps_to_plist(self):
        sc = Shortcut.loads(self.toml_string)
        dump = sc.dumps(file_format='plist')

        exp_dump = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>WFWorkflowActions</key>\n\t<array>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.conditional</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>GroupingIdentifier</key>\n\t\t\t\t<string>123</string>\n\t\t\t\t<key>WFCondition</key>\n\t\t\t\t<string>Equals</string>\n\t\t\t\t<key>WFConditionalActionString</key>\n\t\t\t\t<string>true</string>\n\t\t\t\t<key>WFControlFlowMode</key>\n\t\t\t\t<integer>0</integer>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.conditional</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>GroupingIdentifier</key>\n\t\t\t\t<string>123</string>\n\t\t\t\t<key>WFControlFlowMode</key>\n\t\t\t\t<integer>1</integer>\n\t\t\t</dict>\n\t\t</dict>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.conditional</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>GroupingIdentifier</key>\n\t\t\t\t<string>123</string>\n\t\t\t\t<key>WFControlFlowMode</key>\n\t\t\t\t<integer>2</integer>\n\t\t\t</dict>\n\t\t</dict>\n\t</array>\n\t<key>WFWorkflowClientRelease</key>\n\t<string>2.0</string>\n\t<key>WFWorkflowClientVersion</key>\n\t<string>700</string>\n\t<key>WFWorkflowIcon</key>\n\t<dict>\n\t\t<key>WFWorkflowIconGlyphNumber</key>\n\t\t<integer>59511</integer>\n\t\t<key>WFWorkflowIconImageData</key>\n\t\t<data>\n\t\t</data>\n\t\t<key>WFWorkflowIconStartColor</key>\n\t\t<integer>431817727</integer>\n\t</dict>\n\t<key>WFWorkflowImportQuestions</key>\n\t<array/>\n\t<key>WFWorkflowInputContentItemClasses</key>\n\t<array>\n\t\t<string>WFAppStoreAppContentItem</string>\n\t\t<string>WFArticleContentItem</string>\n\t\t<string>WFContactContentItem</string>\n\t\t<string>WFDateContentItem</string>\n\t\t<string>WFEmailAddressContentItem</string>\n\t\t<string>WFGenericFileContentItem</string>\n\t\t<string>WFImageContentItem</string>\n\t\t<string>WFiTunesProductContentItem</string>\n\t\t<string>WFLocationContentItem</string>\n\t\t<string>WFDCMapsLinkContentItem</string>\n\t\t<string>WFAVAssetContentItem</string>\n\t\t<string>WFPDFContentItem</string>\n\t\t<string>WFPhoneNumberContentItem</string>\n\t\t<string>WFRichTextContentItem</string>\n\t\t<string>WFSafariWebPageContentItem</string>\n\t\t<string>WFStringContentItem</string>\n\t\t<string>WFURLContentItem</string>\n\t</array>\n\t<key>WFWorkflowTypes</key>\n\t<array>\n\t\t<string>NCWidget</string>\n\t\t<string>WatchKit</string>\n\t</array>\n</dict>\n</plist>\n'
        assert dump == exp_dump
