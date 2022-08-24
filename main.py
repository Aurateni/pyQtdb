from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *


class PyExecutor(QDialog):
    def __init__(self, iniFile, parent=None):
        super(PyExecutor, self).__init__(parent)
        self.setWindowFlags(self.windowFlags()
                            | Qt.WindowMinimizeButtonHint
                            | Qt.WindowMaximizeButtonHint
                            )

        self.topLay = QVBoxLayout(self)
        self.topLay.setContentsMargins(6, 6, 6, 6)
        self.lay = QFormLayout()
        self.topLay.addLayout(self.lay)
        self.resultLay = QVBoxLayout()
        self.topLay.addLayout(self.resultLay)
        self.bar = QStatusBar(self)
        self.topLay.addWidget(self.bar)

        self.loadIni(iniFile)

    def loadIni(self, iniFile):
        ini = QSettings(iniFile, QSettings.IniFormat)
        ini.setIniCodec('utf-8')
        ini.beginGroup('Input')
        for key in sorted(ini.childKeys()):
            v = ini.value(key).split(':')
            if len(v) > 1:
                paramTitle = v[0]
                paramValue = v[1]
            else:
                paramTitle = key
                paramValue = v[0]
