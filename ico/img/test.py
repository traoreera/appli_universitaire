from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu flottant transparent")
        self.setGeometry(100, 100, 300, 200)

        button = QPushButton("Afficher le menu", self)
        button.setGeometry(50, 50, 200, 50)
        button.clicked.connect(self.show_menu)

    def show_menu(self):
        menu = QMenu(self)
        
        # Appliquer le style CSS pour rendre le menu transparent
        """menu.setStyleSheet("QMenu {background-color: transparent;}"
                           "QMenu::item {background-color: transparent; color: white;}"
                           "QMenu::item:selected {background-color: rgba(255, 255, 255, 0.2);}")"""
        
        action1 = menu.addAction("Option 1")
        action2 = menu.addAction("Option 2")
        action3 = menu.addAction("Option 3")

        action1.triggered.connect(self.handle_action)
        action2.triggered.connect(self.handle_action)
        action3.triggered.connect(self.handle_action)

        menu.exec_(self.mapToGlobal(self.sender().pos()))

    def handle_action(self):
        action = self.sender()
        print("Option sélectionnée :", action.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
