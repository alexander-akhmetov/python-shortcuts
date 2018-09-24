from shortcuts.actions import (
    CameraAction,
    GetLastPhotoAction,
    SelectPhotoAction,
)


class BasePhotoTest:
    def test_get_parameters(self):
        action = self.action_class()
        dump = action._get_parameters()
        assert dump == {}


class TestCameraAction(BasePhotoTest):
    action_class = CameraAction


class TestGetLastPhotoAction(BasePhotoTest):
    action_class = GetLastPhotoAction


class TestSelectPhotoAction(BasePhotoTest):
    action_class = SelectPhotoAction
