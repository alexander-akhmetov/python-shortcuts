from shortcuts import Shortcut, FMT_SHORTCUT
from shortcuts.actions import Base64DecodeAction, Base64EncodeAction

from tests.conftest import ActionTomlLoadsMixin


class TestBase64EncodeAction(ActionTomlLoadsMixin):
    def test_dumps(self):
        action = Base64EncodeAction()
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.base64encode',
            'WFWorkflowActionParameters': {
                'WFEncodeMode': 'Encode',
            }
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        toml = f'''
        [[action]]
        type = "base64_encode"
        '''
        self._assert_toml_loads(toml, Base64EncodeAction, {})


class TestBase64DecodeAction(ActionTomlLoadsMixin):
    def test_dumps(self):
        action = Base64DecodeAction()
        exp_dump = {
            'WFWorkflowActionIdentifier': 'is.workflow.actions.base64encode',
            'WFWorkflowActionParameters': {
                'WFEncodeMode': 'Decode',
            }
        }
        assert action.dump() == exp_dump

    def test_loads_toml(self):
        toml = f'''
        [[action]]
        type = "base64_decode"
        '''
        self._assert_toml_loads(toml, Base64DecodeAction, {})


class TestBase64Actions:
    def test_loads_plist(self):
        plist = '<?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"> <plist version="1.0"> <dict> <key>WFWorkflowActions</key> <array> <dict> <key>WFWorkflowActionIdentifier</key> <string>is.workflow.actions.base64encode</string> <key>WFWorkflowActionParameters</key> <dict> <key>WFEncodeMode</key> <string>Encode</string> </dict> </dict> <dict> <key>WFWorkflowActionIdentifier</key> <string>is.workflow.actions.base64encode</string> <key>WFWorkflowActionParameters</key> <dict> <key>WFEncodeMode</key> <string>Decode</string> </dict> </dict> </array> <key>WFWorkflowClientRelease</key> <string>2.0</string> <key>WFWorkflowClientVersion</key> <string>700</string> <key>WFWorkflowIcon</key> <dict> <key>WFWorkflowIconGlyphNumber</key> <integer>59511</integer> <key>WFWorkflowIconImageData</key> <data> </data> <key>WFWorkflowIconStartColor</key> <integer>4271458815</integer> </dict> <key>WFWorkflowImportQuestions</key> <array/> <key>WFWorkflowInputContentItemClasses</key> <array> <string>WFAppStoreAppContentItem</string> <string>WFArticleContentItem</string> <string>WFContactContentItem</string> <string>WFDateContentItem</string> <string>WFEmailAddressContentItem</string> <string>WFGenericFileContentItem</string> <string>WFImageContentItem</string> <string>WFiTunesProductContentItem</string> <string>WFLocationContentItem</string> <string>WFDCMapsLinkContentItem</string> <string>WFAVAssetContentItem</string> <string>WFPDFContentItem</string> <string>WFPhoneNumberContentItem</string> <string>WFRichTextContentItem</string> <string>WFSafariWebPageContentItem</string> <string>WFStringContentItem</string> <string>WFURLContentItem</string> </array> <key>WFWorkflowTypes</key> <array> <string>NCWidget</string> <string>WatchKit</string> </array> </dict> </plist>'

        sc = Shortcut.loads(plist, file_format=FMT_SHORTCUT)

        assert isinstance(sc.actions[0], Base64EncodeAction) is True
        assert isinstance(sc.actions[1], Base64DecodeAction) is True
