from shortcuts.actions.base import BaseAction, Field, BooleanField, VariablesField


class ReadFileAction(BaseAction):
    '''Get file'''
    type = 'is.workflow.actions.documentpicker.open'
    keyword = 'read_file'

    path = VariablesField('WFGetFilePath')
    not_found_error = BooleanField('WFFileErrorIfNotFound')
    show_picker = BooleanField('WFShowFilePicker')


class SaveFileAction(BaseAction):
    '''Save file'''
    type = 'is.workflow.actions.documentpicker.save'
    keyword = 'save_file'

    path = VariablesField('WFFileDestinationPath')
    overwrite = Field('WFSaveFileOverwrite')
    show_picker = BooleanField('WFAskWhereToSave')


class CreateFolderAction(BaseAction):
    '''Create folder'''
    type = 'is.workflow.actions.file.createfolder'
    keyword = 'create_folder'

    path = VariablesField('WFFilePath')


class PreviewDocumentAction(BaseAction):
    '''Preview document'''
    type = 'is.workflow.actions.previewdocument'
    keyword = 'preview'
