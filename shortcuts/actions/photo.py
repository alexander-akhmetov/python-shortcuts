from shortcuts.actions.base import BaseAction, BooleanField, Field


class CameraAction(BaseAction):
    '''Take photo'''
    itype = 'is.workflow.actions.takephoto'
    keyword = 'take_photo'


class GetLastPhotoAction(BaseAction):
    '''Get latest photos'''
    itype = 'is.workflow.actions.getlastphoto'
    keyword = 'get_last_photo'


class SelectPhotoAction(BaseAction):
    '''Select photos'''
    itype = 'is.workflow.actions.selectphoto'
    keyword = 'select_photo'


class ImageConvertAction(BaseAction):
    '''Image convert'''
    itype = 'is.workflow.actions.image.convert'
    keyword = 'convert_image'

    compression_quality = Field('WFImageCompressionQuality')
    format = Field('WFImageFormat')
    preserve_metadata = BooleanField('WFImagePreserveMetadata')
