from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText


class MenuExample(BaseWidget):
    def __init__(self):
        super(MenuExample, self).__init__('Menu example')

        self._output = ControlText('Output')
        menu1 = self._output.add_popup_menu_option(
            'option 1',
            function_action=self.__menu1,
            key="Control+1",
        )
        menu2 = self._output.add_popup_submenu('option 2')
        menu2_1 = self._output.add_popup_submenu('option 2.1', submenu=menu2)
        menu2_1_1 = self._output.add_popup_menu_option(
            'option 2.1.1',
            function_action=self.__menu2_1_1,
            menu=menu2_1,
        )

        self.formset = [
            '_output',
        ]
        self.mainmenu = [
            {
                'File': [
                    {'Open': self.__openEvent},
                    '-',
                    {'Save': self.__saveEvent},
                    {'Save as': self.__saveAsEvent}
                ]
            },
            {
                'Edit': [
                    {'Copy': self.__editEvent},
                    {'Paste': self.__pasteEvent}
                ]
            }
        ]

    def __openEvent(self):
        self._output.value = "open event"

    def __saveEvent(self):
        self._output.value = "save event"

    def __saveAsEvent(self):
        self._output.value = "save as event"

    def __editEvent(self):
        self._output.value = "edit event"

    def __pasteEvent(self):
        self._output.value = "paste event"

    def __menu1(self):
        self._output.value = "1"

    def __menu2_1_1(self):
        self._output.value = "2.1.1"


if __name__ == '__main__':
    from pyforms import start_app

    start_app(MenuExample)
