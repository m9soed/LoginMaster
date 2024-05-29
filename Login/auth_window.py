from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from user_manager import UserManager
from register_window import RegisterWindow
import main_window

class AuthWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")

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

        self.login_button = QPushButton("Войти")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.register_button = QPushButton("Регистрация")
        self.register_button.clicked.connect(self.show_register_window)
        layout.addWidget(self.register_button)

        self.central_widget.setLayout(layout)

        self.user_manager = UserManager()

    def login(self):
        login = self.login_input.text()
        password = self.password_input.text()

        if self.user_manager.authenticate_user(login, password):
            self.main_window = main_window.MainWindow(login, self.user_manager)
            self.main_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка авторизации", "Пользователь не найден или неверный пароль.")

    def show_register_window(self):
        self.register_window = RegisterWindow(self.user_manager)
        self.register_window.show()
