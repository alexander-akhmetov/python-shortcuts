from shortcuts.actions import AppendFileAction

from tests.conftest import SimpleBaseDumpsLoadsTest


class TestAppendFileAction(SimpleBaseDumpsLoadsTest):
    action_class = AppendFileAction
    itype = 'is.workflow.actions.file.append'

    dump_data = {'path': '/123'}
    dump_params = {
        'WFFilePath': {
            'Value': {
                'attachmentsByRange': {}, 'string': '/123'
            },
            'WFSerializationType': 'WFTextTokenString',
        },
    }

    toml = '''
    [[action]]
    type = "append_file"
    path = "{{db_dir}}/{{db_name}}.txt"
    '''
    exp_toml_params = {'path': '{{db_dir}}/{{db_name}}.txt'}

    action_xml = '''
      <dict>
        <key>WFWorkflowActionIdentifier</key>
        <string>is.workflow.actions.file.append</string>
        <key>WFWorkflowActionParameters</key>
        <dict>
        <key>WFFilePath</key>
        <dict>
            <key>Value</key>
            <dict>
                <key>attachmentsByRange</key>
                <dict>
                    <key>{0, 1}</key>
                    <dict>
                        <key>Type</key>
                        <string>Variable</string>
                        <key>VariableName</key>
                        <string>db_dir</string>
                    </dict>
                    <key>{2, 1}</key>
                    <dict>
                        <key>Type</key>
                        <string>Variable</string>
                        <key>VariableName</key>
                        <string>db_name</string>
                    </dict>
                </dict>
                <key>string</key>
                <string>￼/￼.txt</string>
            </dict>
            <key>WFSerializationType</key>
            <string>WFTextTokenString</string>
        </dict>
        </dict>
      </dict>
    '''
    exp_xml_params = {'path': '{{db_dir}}￼/{{db_name}}￼.txt'}
