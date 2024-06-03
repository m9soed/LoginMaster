from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from user_manager import UserManager

class RegisterWindow(QMainWindow):
    def __init__(self, user_manager):
        super().__init__()
        self.setWindowTitle("Регистрация")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.login_label = QLabel("Логин:")
        self.login_input = QLineEdit()
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_input)

        self.password_label = QLabel("Пароль:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.confirm_password_label = QLabel("Повторите пароль:")
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_input)

        self.name_label = QLabel("Имя:")
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.surname_label = QLabel("Фамилия:")
        self.surname_input = QLineEdit()
        layout.addWidget(self.surname_label)
        layout.addWidget(self.surname_input)

        self.email_label = QLabel("Электронная почта:")
        self.email_input = QLineEdit()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        self.register_button = QPushButton("Создать")
        self.register_button.clicked.connect(self.register)
        layout.addWidget(self.register_button)

        self.central_widget.setLayout(layout)

        self.user_manager = user_manager

    def register(self):
        login = self.login_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()
        name = self.name_input.text()
        surname = self.surname_input.text()
        email = self.email_input.text()

        if password != confirm_password:
            QMessageBox.warning(self, "Ошибка", "Пароли не совпадают.")
            return

        if not self.user_manager.is_password_strong(password):
            QMessageBox.warning(self, "Ошибка", "Пароль недостаточно сложный.")
            return

        if self.user_manager.add_user(login, password, name, surname, email):
            QMessageBox.information(self, "Сообщение", "Пользователь успешно зарегистрирован.")
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Пользователь с таким логином уже существует.")
