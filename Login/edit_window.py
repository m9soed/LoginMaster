from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtCore import Signal
from user_manager import UserManager

class EditWindow(QMainWindow):
    data_updated = Signal()

    def __init__(self, username, user_manager):
        super().__init__()
        self.setWindowTitle("Редактирование данных")

        self.username = username
        self.user_manager = user_manager
        self.user_info = self.user_manager.get_user_info(username)

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.name_label = QLabel("Имя:")
        self.name_input = QLineEdit(self.user_info['name'])
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.surname_label = QLabel("Фамилия:")
        self.surname_input = QLineEdit(self.user_info['surname'])
        layout.addWidget(self.surname_label)
        layout.addWidget(self.surname_input)

        self.email_label = QLabel("Электронная почта:")
        self.email_input = QLineEdit(self.user_info['email'])
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        self.save_button = QPushButton("Сохранить")
        self.save_button.clicked.connect(self.save_changes)
        layout.addWidget(self.save_button)

        self.central_widget.setLayout(layout)

    def save_changes(self):
        name = self.name_input.text()
        surname = self.surname_input.text()
        email = self.email_input.text()

        if name and surname and email:
            self.user_manager.update_user_info(self.username, name, surname, email)
            self.data_updated.emit()
            QMessageBox.information(self, "Успех", "Данные пользователя успешно обновлены.")
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены.")
