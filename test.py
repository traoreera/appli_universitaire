import sys
from PySide2.QtCore import QObject, Signal, Slot, Property
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
import subprocess

class CommandRunner(QObject):
    outputChanged = Signal(str)

    @Slot(str)
    def runCommand(self, command):
        try:
            result = subprocess.check_output(command, shell=True)
            output = result.decode("utf-8")
        except subprocess.CalledProcessError as e:
            output = e.output.decode("utf-8")
        self.outputChanged.emit(output)

app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
commandRunner = CommandRunner()
engine.rootContext().setContextProperty("commandRunner", commandRunner)
engine.load("test.qml")
sys.exit(app.exec_())
