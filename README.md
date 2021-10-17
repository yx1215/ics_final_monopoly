# ics_final_monopoly
## 1. How to add pictures to Qt Designer Resource:
You can find a file called `picture.qrc`. Inside it you will find the following code:

```xml
<!DOCTYPE RCC><RCC version="1.0">
    <qresource prefix="/figure">
        <file alias="ics_game_cover.jpg">./figure/ics_game_cover.jpg</file>
    </qresource>
</RCC>
```

For example if you want to add a picture named `example.png'`, you should first put it
in the `figure` directory and then add a line 

`<file alias="example.png">./figure/ics_game_cover.png</file>`

in the above file in the `<qresource>` section. After this, the code should become:

```xml
<!DOCTYPE RCC><RCC version="1.0">
    <qresource prefix="/figure">
        <file alias="ics_game_cover.jpg">./figure/ics_game_cover.jpg</file>
        <file alias="example.png">./figure/ics_game_cover.png</file>
    </qresource>
</RCC>

```

After reloading this file in Qt Designer, you can then find the new added picture in resource section.

## 2.How to make a picture fit the label/button.

When adding a picture to a label/button, choose `border-image` instead of `background-image`.

## 3.How to generate .py file from Qt Designer.

(a) Save Qt Desinger as a .ui file, for example, `test.ui`.
(b) Run the following code in the terminal:

```bash
pyuci5 -m test.ui -o test.py
pyrcc5 picture.qrc -o picture_rc.py

```

`test.py` is the file generated for the Qt Designer and `picture_rc.py` is the binary file transformed from the pictures.

(c) Create a new file, for example, `main_test.py`, and include the following code (already done in this repository).

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from test import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    app.startingUp()
    myWin.show()
    sys.exit(app.exec_())

```
In order to test the PyQt window, please run `main_test.py`.
(Notice that if you do not generate `picture.py`, pictures will not be available when you run `main_test.py`.)

## 4. How to add fate events.
You can find a function named `pass_building()` in the file `main_test.py`. It has codes like:
```python
def pass_building(self, player, x, y):
    assert isinstance(player, Player)
    building = self.building_dic[(x, y)]
    if building is not None:
        # fate part
        if building.objectName() == "bursar":
            player.cash += 1000
            self.fate.setText("Get funded by bursar.")
        # other fates here
        elif building.objectName() == <building_name>:
            <event>
        # update once after fate.
        self.set_player1_info()
        self.set_player2_info()
        ...
```
`<building_name>` means the building to need to pass to make this `<event>` happen.
