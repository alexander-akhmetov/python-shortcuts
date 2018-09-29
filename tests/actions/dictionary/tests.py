from shortcuts.actions import DictionaryAction, SetDictionaryValueAction, GetDictionaryFromInputAction
from shortcuts import Shortcut, FMT_SHORTCUT

from tests.conftest import ActionTomlLoadsMixin, SimpleBaseDumpsLoadsTest


class TestDictionaryAction:
    def test_dump(self):
        data = {
            'items': [
                {'key': 'k1', 'value': 'v1'},
                {'key': 'k2', 'value': '{{var}}'},
            ],
        }
        action = DictionaryAction(data=data)

        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.dictionary',
            'WFWorkflowActionParameters': {
                'WFItems': {
                    'Value': {
                        'WFDictionaryFieldValueItems': [
                            {
                                'WFItemType': 0,
                                'WFKey': {
                                    'Value': {'attachmentsByRange': {}, 'string': 'k1'},
                                    'WFSerializationType': 'WFTextTokenString',
                                },
                                'WFValue': {
                                    'Value': {'attachmentsByRange': {}, 'string': 'v1'},
                                    'WFSerializationType': 'WFTextTokenString',
                                }
                            },
                            {
                                'WFItemType': 0,
                                'WFKey': {
                                    'Value': {'attachmentsByRange': {}, 'string': 'k2'},
                                    'WFSerializationType': 'WFTextTokenString',
                                },
                                'WFValue': {
                                    'Value': {
                                        'attachmentsByRange': {
                                            '{0, 1}': {'Type': 'Variable', 'VariableName': 'var'}
                                        },
                                        'string': '￼',
                                    },
                                    'WFSerializationType': 'WFTextTokenString',
                                }
                            }
                        ]
                    },
                    'WFSerializationType': 'WFDictionaryFieldValue',
                },
            },
        }
        assert action.dump() == exp_dump


class TestShortcutWithDictionary:
    toml_string = '''
        [[action]]
        type = "dictionary"

            [[action.items]]
            key = "some key"
            value = "some value"

            [[action.items]]
            key = "another key"
            value = "{{x}}"
    '''

    def test_loads_from_toml(self):
        sc = Shortcut.loads(self.toml_string)

        assert len(sc.actions) == 1

        action = sc.actions[0]
        assert isinstance(action, DictionaryAction) is True

        exp_data = {
            'items': [
                {'key': 'some key', 'value': 'some value'},
                {'key': 'another key', 'value': '{{x}}'},
            ],
        }
        assert action.data == exp_data

    def test_dumps_to_plist(self):
        sc = Shortcut.loads(self.toml_string)
        dump = sc.dumps(file_format=FMT_SHORTCUT)

        exp_dump = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>WFWorkflowActions</key>\n\t<array>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.dictionary</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>WFItems</key>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t<dict>\n\t\t\t\t\t\t<key>WFDictionaryFieldValueItems</key>\n\t\t\t\t\t\t<array>\n\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t<key>WFItemType</key>\n\t\t\t\t\t\t\t\t<integer>0</integer>\n\t\t\t\t\t\t\t\t<key>WFKey</key>\n\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t\t\t\t\t<dict/>\n\t\t\t\t\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t\t\t\t\t<string>some key</string>\n\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t<key>WFValue</key>\n\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t\t\t\t\t<dict/>\n\t\t\t\t\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t\t\t\t\t<string>some value</string>\n\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t<key>WFItemType</key>\n\t\t\t\t\t\t\t\t<integer>0</integer>\n\t\t\t\t\t\t\t\t<key>WFKey</key>\n\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t\t\t\t\t<dict/>\n\t\t\t\t\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t\t\t\t\t<string>another key</string>\n\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t<key>WFValue</key>\n\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t\t<key>{0, 1}</key>\n\t\t\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t\t\t<key>Type</key>\n\t\t\t\t\t\t\t\t\t\t\t\t<string>Variable</string>\n\t\t\t\t\t\t\t\t\t\t\t\t<key>VariableName</key>\n\t\t\t\t\t\t\t\t\t\t\t\t<string>x</string>\n\t\t\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t\t\t\t\t<string>￼</string>\n\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t</array>\n\t\t\t\t\t</dict>\n\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t<string>WFDictionaryFieldValue</string>\n\t\t\t\t</dict>\n\t\t\t</dict>\n\t\t</dict>\n\t</array>\n\t<key>WFWorkflowClientRelease</key>\n\t<string>2.0</string>\n\t<key>WFWorkflowClientVersion</key>\n\t<string>700</string>\n\t<key>WFWorkflowIcon</key>\n\t<dict>\n\t\t<key>WFWorkflowIconGlyphNumber</key>\n\t\t<integer>59511</integer>\n\t\t<key>WFWorkflowIconImageData</key>\n\t\t<data>\n\t\t</data>\n\t\t<key>WFWorkflowIconStartColor</key>\n\t\t<integer>431817727</integer>\n\t</dict>\n\t<key>WFWorkflowImportQuestions</key>\n\t<array/>\n\t<key>WFWorkflowInputContentItemClasses</key>\n\t<array>\n\t\t<string>WFAppStoreAppContentItem</string>\n\t\t<string>WFArticleContentItem</string>\n\t\t<string>WFContactContentItem</string>\n\t\t<string>WFDateContentItem</string>\n\t\t<string>WFEmailAddressContentItem</string>\n\t\t<string>WFGenericFileContentItem</string>\n\t\t<string>WFImageContentItem</string>\n\t\t<string>WFiTunesProductContentItem</string>\n\t\t<string>WFLocationContentItem</string>\n\t\t<string>WFDCMapsLinkContentItem</string>\n\t\t<string>WFAVAssetContentItem</string>\n\t\t<string>WFPDFContentItem</string>\n\t\t<string>WFPhoneNumberContentItem</string>\n\t\t<string>WFRichTextContentItem</string>\n\t\t<string>WFSafariWebPageContentItem</string>\n\t\t<string>WFStringContentItem</string>\n\t\t<string>WFURLContentItem</string>\n\t</array>\n\t<key>WFWorkflowTypes</key>\n\t<array>\n\t\t<string>NCWidget</string>\n\t\t<string>WatchKit</string>\n\t</array>\n</dict>\n</plist>\n'
        assert dump == exp_dump


class TestSetDictionaryValueAction(ActionTomlLoadsMixin):
    def test_dumps(self):
        key = 'key1'
        value = 'value1'
        action = SetDictionaryValueAction(data={'key': key, 'value': value})
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.setvalueforkey',
            'WFWorkflowActionParameters': {
                'WFDictionaryKey': {
                    'Value': {'attachmentsByRange': {}, 'string': key},
                    'WFSerializationType': 'WFTextTokenString',
                },
                'WFDictionaryValue': {
                    'Value': {'attachmentsByRange': {}, 'string': value},
                    'WFSerializationType': 'WFTextTokenString',
                },
            }
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        key = 'key2'
        value = 'value2'
        toml = f'''
        [[action]]
        type = "set_value_for_key"
        key = "{key}"
        value = "{value}"
        '''
        self._assert_toml_loads(toml, SetDictionaryValueAction, {'key': key, 'value': value})


class TestGetDictionaryFromInputAction(SimpleBaseDumpsLoadsTest):
    action_class = GetDictionaryFromInputAction
    itype = 'is.workflow.actions.detect.dictionary'
    toml = '[[action]]\ntype = "get_dictionary"'
    action_xml = '''
      <dict>
        <key>WFWorkflowActionIdentifier</key>
        <string>is.workflow.actions.detect.dictionary</string>
        <key>WFWorkflowActionParameters</key>
        <dict></dict>
      </dict>
    '''
