from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
# Импортируем UserManager для управления пользователями
from user_manager import UserManager
# Импортируем RegisterWindow для регистрации новых пользователей
from register_window import RegisterWindow
# Импортируем main_window для отображения главного окна после авторизации
import main_window

class AuthWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")

        # Создаем центральный виджет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Создаем вертикальный лэйаут
        layout = QVBoxLayout()

        # Создаем и добавляем виджеты для ввода логина
        self.login_label = QLabel("Логин:")
        self.login_input = QLineEdit()
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_input)

        # Создаем и добавляем виджеты для ввода пароля
        self.password_label = QLabel("Пароль:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        # Создаем и добавляем кнопку "Войти"
        self.login_button = QPushButton("Войти")
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        # Создаем и добавляем кнопку "Регистрация"
        self.register_button = QPushButton("Регистрация")
        self.register_button.clicked.connect(self.show_register_window)
        layout.addWidget(self.register_button)

        # Устанавливаем лэйаут для центрального виджета
        self.central_widget.setLayout(layout)

        # Создаем экземпляр UserManager для управления пользователями
        self.user_manager = UserManager()

    def login(self):
        # Получаем введенные логин и пароль
        login = self.login_input.text()
        password = self.password_input.text()

        # Проверяем подлинность пользователя
        if self.user_manager.authenticate_user(login, password):
            # Если пользователь аутентифицирован, открываем главное окно
            self.main_window = main_window.MainWindow(login, self.user_manager)
            self.main_window.show()
            self.close()
        else:
            # Если аутентификация не удалась, показываем сообщение об ошибке
            QMessageBox.warning(self, "Ошибка авторизации", "Пользователь не найден или неверный пароль.")

    def show_register_window(self):
        # Показываем окно регистрации
        self.register_window = RegisterWindow(self.user_manager)
        self.register_window.show()
