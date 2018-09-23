from shortcuts.actions.base import BaseAction, BooleanField, Field


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


class ImageConvertAction(BaseAction):
    '''Image convert'''
    type = 'is.workflow.actions.image.convert'
    keyword = 'convert_image'

    compression_quality = Field('WFImageCompressionQuality')
    format = Field('WFImageFormat')
    preserve_metadata = BooleanField('WFImagePreserveMetadata')
