from shortcuts.actions.web import URLAction


class TestURLAction:
    def test_get_parameters(self):
        url = 'https://aleks.sh'
        action = URLAction(data={'url': url})

        dump = action._get_parameters()

        exp_dump = {
            'WFURLActionURL': url,
        }
        assert dump == exp_dump
