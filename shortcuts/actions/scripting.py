from shortcuts.actions.base import BaseAction, FloatField


class NothingAction(BaseAction):
    '''Nothing'''
    itype = 'is.workflow.actions.nothing'
    keyword = 'nothing'


class SetItemNameAction(BaseAction):
    '''Set item name'''
    # todo: advanced
    # <dict>
    #   <key>WFWorkflowActionIdentifier</key>
    #   <string>is.workflow.actions.setitemname</string>
    #   <key>WFWorkflowActionParameters</key>
    #   <dict>
    #       <key>Advanced</key>
    #       <true/>
    #       <key>WFDontIncludeFileExtension</key>
    #       <true/>
    #   </dict>
    # </dict>

    itype = 'is.workflow.actions.setitemname'
    keyword = 'set_item_name'


class ViewContentGraphAction(BaseAction):
    '''View content graph'''
    itype = 'is.workflow.actions.viewresult'
    keyword = 'view_content_graph'


class ContinueInShortcutAppAction(BaseAction):
    '''Continue in shortcut app'''
    itype = 'is.workflow.actions.handoff'
    keyword = 'continue_in_shortcut_app'


class DelayAction(BaseAction):
    '''Delay'''
    itype = 'is.workflow.actions.delay'
    keyword = 'delay'

    time = FloatField('WFDelayTime')


class WaitToReturnAction(BaseAction):
    '''Wait to return'''
    itype = 'is.workflow.actions.waittoreturn'
    keyword = 'wait_to_return'
