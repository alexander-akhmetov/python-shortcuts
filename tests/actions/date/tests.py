from shortcuts.actions import DetectDateAction, GetTimeBetweenDates

from tests.conftest import SimpleBaseDumpsLoadsTest


class TestDetectDateAction(SimpleBaseDumpsLoadsTest):
    action_class = DetectDateAction
    itype = 'is.workflow.actions.detect.date'
    toml = '[[action]]\ntype = "detect_date"'
    action_xml = '''
      <dict>
        <key>WFWorkflowActionIdentifier</key>
        <string>is.workflow.actions.detect.date</string>
        <key>WFWorkflowActionParameters</key>
        <dict>
        </dict>
      </dict>
    '''


class TestGetTimeBetweenDates(SimpleBaseDumpsLoadsTest):
    action_class = GetTimeBetweenDates
    itype = 'is.workflow.actions.gettimebetweendates'

    dump_data = {'units': 'Seconds'}
    dump_params = {
        'WFTimeUntilUnit': 'Seconds'
    }

    toml = '[[action]]\ntype = "get_time_between_dates"\nunits = "Days"'
    exp_toml_params = {'units': 'Days'}

    action_xml = '''
      <dict>
        <key>WFWorkflowActionIdentifier</key>
        <string>is.workflow.actions.gettimebetweendates</string>
        <key>WFWorkflowActionParameters</key>
        <dict>
            <key>WFTimeUntilUnit</key>
            <string>Minutes</string>
        </dict>
      </dict>
    '''
    exp_xml_params = {'units': 'Minutes'}
