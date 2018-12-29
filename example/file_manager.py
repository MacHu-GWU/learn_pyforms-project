"""
This demo is not finished yet.
"""

from pyforms.basewidget import BaseWidget
from pyforms.controls import (
    ControlBase,
    ControlCheckBox,
    ControlFilesTree,
    ControlCodeEditor,
)


class AppFormatFullname(BaseWidget):

    def __init__(self):
        super(AppFormatFullname, self).__init__('Format Fullname')

        # Definition of the forms fields
        self._check_box = ControlCheckBox(label="check box")
        self._file_tree = ControlFilesTree(label="file tree")
        self._file_tree.value = "/Users/sanhehu/Documents/GitHub/learn_pyforms-project"
        self._code_editor = ControlCodeEditor(label="code editor")
        self.formset = [
            "_check_box",
            "_file_tree",
            "_code_editor",
        ]


if __name__ == '__main__':
    from pyforms import start_app

    start_app(AppFormatFullname)
