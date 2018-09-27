from shortcuts.actions.base import BaseAction, ChoiceField, Field, VariablesField


class CommentAction(BaseAction):
    '''Comment: just a comment'''
    itype = 'is.workflow.actions.comment'
    keyword = 'comment'

    text = Field('WFCommentActionText', help='Text to show in the comment')


class TextAction(BaseAction):
    '''Text: returns text as an output'''
    itype = 'is.workflow.actions.gettext'
    keyword = 'text'

    text = VariablesField('WFTextActionText', help='Output of this action')


CASE_CHOICES = (
    'UPPERCASE',
    'lowercase',
    'Capitalize Every Word',
    'Capitalize with Title Case',
    'Capitalize with sentence case.',
    'cApItAlIzE wItH aLtErNaTiNg CaSe.',
)


class ChangeCaseAction(BaseAction):
    '''Change case'''
    itype = 'is.workflow.actions.text.changecase'
    keyword = 'change_case'

    case_type = ChoiceField('WFCaseType', choices=CASE_CHOICES)


SPLIT_SEPARATOR_CHOICES = (
    'New Lines',
    'Spaces',
    'Every Character',
    'Custom',
)


class SplitTextAction(BaseAction):
    '''Split text'''
    itype = 'is.workflow.actions.text.split'
    keyword = 'split_text'

    separator_type = ChoiceField(
        'WFTextSeparator',
        choices=SPLIT_SEPARATOR_CHOICES,
        default=SPLIT_SEPARATOR_CHOICES[0],
    )
    custom_separator = Field(
        'WFTextCustomSeparator',
        help='Works only with "Custom" `separator_type`',
        required=False,
    )


class DetectLanguageAction(BaseAction):
    '''Detect Language with Microsoft'''
    itype = 'is.workflow.actions.detectlanguage'
    keyword = 'detect_language'


class GetNameOfEmojiAction(BaseAction):
    '''Get name of emoji'''
    itype = 'is.workflow.actions.getnameofemoji'
    keyword = 'get_name_of_emoji'


class GetTextFromInputAction(BaseAction):
    '''
    Get text from input

    Returns text from the previous action's input.
    For example, this action can get the name of a photo
    or song, or the text of a web page.
    '''
    itype = 'is.workflow.actions.detect.text'
    keyword = 'get_text_from_input'


class ScanQRBarCodeAction(BaseAction):
    '''Scan QR/Barcode'''
    itype = 'is.workflow.actions.scanbarcode'
    keyword = 'scan_barcode'


class ShowDefinitionAction(BaseAction):
    '''Show definition'''
    itype = 'is.workflow.actions.showdefinition'
    keyword = 'show_definition'
