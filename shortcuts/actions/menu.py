from shortcuts.actions.base import ArrayField, BaseAction, Field, GroupIDField


class MenuStartAction(BaseAction):
    '''
    Start menu

    To build a menu, you have to write at least three actions:
        * Start menu
        * Menu item
        * End menu

    So the menu with two items will look like:

        ```
        Start menu

        Menu item title=1
            ... some actions...

        Menu item title=2
            ...other actions...

        End menu
        ```

    As in other actions which have `group_id` field, you don't need to specify it, it will be generated automatically.
    '''
    itype = 'is.workflow.actions.choosefrommenu'
    keyword = 'start_menu'

    group_id = GroupIDField('GroupingIdentifier')

    menu_items = ArrayField('WFMenuItems')

    default_fields = {
        'WFControlFlowMode': 0,
    }


class MenuItemAction(BaseAction):
    '''
    Menu item

    You must specify the title for the item.
    After this action write all actions which you want to be executed when a user selects this option in the menu.
    '''
    itype = 'is.workflow.actions.choosefrommenu'
    keyword = 'menu_item'

    group_id = GroupIDField('GroupingIdentifier')
    title = Field('WFMenuItemTitle')

    default_fields = {
        'WFControlFlowMode': 1,
    }


class MenuEndAction(BaseAction):
    '''End menu'''
    itype = 'is.workflow.actions.choosefrommenu'
    keyword = 'end_menu'

    group_id = GroupIDField('GroupingIdentifier')

    default_fields = {
        'WFControlFlowMode': 2,
    }
