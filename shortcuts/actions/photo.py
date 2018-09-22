from shortcuts.actions.base import BaseAction


class CameraAction(BaseAction):
    '''Take photo'''
    type = 'is.workflow.actions.takephoto'
    keyword = 'take_photo'


class GetLastPhotoAction(BaseAction):
    '''Get latest photos'''
    type = 'is.workflow.actions.getlastphoto'
    keyword = 'get_last_photo'


class SelectPhotoAction(BaseAction):
    '''Select photos'''
    type = 'is.workflow.actions.selectphoto'
    keyword = 'select_photo'
