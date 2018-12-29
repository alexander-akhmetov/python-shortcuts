from shortcuts.actions.base import BaseAction, BooleanField, ChoiceField, Field, FloatField, GroupIDField, IntegerField


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


class ChooseFromListAction(BaseAction):
    '''Choose from list'''
    itype = 'is.workflow.actions.choosefromlist'
    keyword = 'choose_from_list'
    prompt = Field('WFChooseFromListActionPrompt', required=False)
    select_multiple = BooleanField('WFChooseFromListActionSelectMultiple', required=False)
    select_all_initially = BooleanField('WFChooseFromListActionSelectAll', required=False)


class DelayAction(BaseAction):
    '''Delay'''
    itype = 'is.workflow.actions.delay'
    keyword = 'delay'

    time = FloatField('WFDelayTime')


class WaitToReturnAction(BaseAction):
    '''Wait to return'''
    itype = 'is.workflow.actions.waittoreturn'
    keyword = 'wait_to_return'


class RepeatStartAction(BaseAction):
    '''Repeat'''
    itype = 'is.workflow.actions.repeat.count'
    keyword = 'repeat_start'

    _additional_identifier_field = 'WFControlFlowMode'

    group_id = GroupIDField('GroupingIdentifier')
    count = IntegerField('WFRepeatCount')

    default_fields = {
        'WFControlFlowMode': 0,
    }


class RepeatEndAction(BaseAction):
    '''Repeat'''
    itype = 'is.workflow.actions.repeat.count'
    keyword = 'repeat_end'

    _additional_identifier_field = 'WFControlFlowMode'

    group_id = GroupIDField('GroupingIdentifier')

    default_fields = {
        'WFControlFlowMode': 2,
    }


class RepeatEachStartAction(BaseAction):
    '''Repeat with each start'''
    itype = 'is.workflow.actions.repeat.each'
    keyword = 'repeat_with_each_start'

    _additional_identifier_field = 'WFControlFlowMode'

    group_id = GroupIDField('GroupingIdentifier')

    default_fields = {
        'WFControlFlowMode': 0,
    }


class RepeatEachEndAction(BaseAction):
    '''Repeat with each end'''
    itype = 'is.workflow.actions.repeat.each'
    keyword = 'repeat_with_each_end'

    _additional_identifier_field = 'WFControlFlowMode'

    group_id = GroupIDField('GroupingIdentifier')

    default_fields = {
        'WFControlFlowMode': 2,
    }


HASH_CHOICES = (
    'MD5',
    'SHA1',
    'SHA256',
    'SHA512',
)


class HashAction(BaseAction):
    '''Hash action'''
    itype = 'is.workflow.actions.hash'
    keyword = 'hash'

    hash_type = ChoiceField('WFHashType', choices=HASH_CHOICES, default=HASH_CHOICES[0])


class GetMyShortcutsAction(BaseAction):
    '''Get my shortcuts'''
    itype = 'is.workflow.actions.getmyworkflows'
    keyword = 'get_my_shortcuts'


class RunShortcutAction(BaseAction):
    '''Run shortcut'''
    itype = 'is.workflow.actions.runworkflow'
    keyword = 'run_shortcut'

    show = BooleanField('WFShowWorkflow', default=False)
    shortcut_name = Field('WFWorkflowName')


class OpenAppAction(BaseAction):
    '''Opens the specified app.'''
    itype = 'is.workflow.actions.openapp'
    keyword = 'open_app'

    app = Field('WFAppIdentifier')
