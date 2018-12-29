from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton


class AppFormatFullname(BaseWidget):

    def __init__(self):
        super(AppFormatFullname, self).__init__('Format Fullname')

        # Definition of the forms fields
        self._firstname = ControlText('First name')
        self._lastname = ControlText('Lastname name')
        self._fullname = ControlText('Full name')
        self._button = ControlButton('Press this button')
        self._button.value = self.__buttonAction

        self.formset = [
            ('_firstname', '_lastname'),
            '_button', '_fullname', ' '
        ]

    def __buttonAction(self):
        """Button action event"""
        self._fullname.value = "{} {}".format(self._firstname.value, self._lastname.value)


if __name__ == '__main__':
    from pyforms import start_app

    start_app(AppFormatFullname)
