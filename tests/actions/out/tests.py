from shortcuts.actions import ShowResultAction, ShowAlertAction


class TestShowResultAction:
    def test_get_parameters(self):
        text = '{{v1}}##{{v2}}'
        action = ShowResultAction(data={'text': text})

        dump = action._get_parameters()

        exp_dump = {
            'Text': {
                'Value': {
                    'attachmentsByRange': {
                        '{0, 1}': {'Type': 'Variable', 'VariableName': 'v1'},
                        '{3, 1}': {'Type': 'Variable', 'VariableName': 'v2'},
                    },
                    'string': '￼##￼',
                },
                'WFSerializationType': 'WFTextTokenString',
            },
            'WFSerializationType': 'WFTextTokenString',
        }
        assert dump == exp_dump


class TestShowAlertAction:
    def test_get_parameters(self):
        title = 'some title'
        text = 'some text'
        show_cancel_button = True
        action = ShowAlertAction(
            dict(title=title, text=text, show_cancel_button=show_cancel_button)
        )

        dump = action._get_parameters()

        exp_dump = {
            'WFAlertActionCancelButtonShown': show_cancel_button,
            'WFAlertActionMessage': text,
            'WFAlertActionTitle': title,
        }
        assert dump == exp_dump
