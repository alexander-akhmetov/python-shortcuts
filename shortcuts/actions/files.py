from shortcuts.actions.base import BaseAction, Field, BooleanField


class ReadFileAction(BaseAction):
    '''Get file'''
    type = 'is.workflow.actions.documentpicker.open'
    keyword = 'read_file'

    path = Field('WFFileDestinationPath')
    not_found_error = BooleanField('WFFileErrorIfNotFound')
    show_picker = BooleanField('WFAskWhereToSave')


class SaveFileAction(BaseAction):
    '''Save file'''
    type = 'is.workflow.actions.documentpicker.save'
    keyword = 'save_file'

    path = Field('WFFileDestinationPath')
    overwrite = Field('WFSaveFileOverwrite')
    show_picker = BooleanField('WFAskWhereToSave')


class CreateFolderAction(BaseAction):
    '''Create folder'''
    type = 'is.workflow.actions.file.createfolder'
    keyword = 'create_folder'

    path = Field('WFFilePath')
