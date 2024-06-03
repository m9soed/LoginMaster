from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMenuBar
from PySide6.QtGui import QAction
# Импортируем UserManager для управления пользователями
from user_manager import UserManager
# Импортируем EditWindow для редактирования данных пользователя
from edit_window import EditWindow
# Импортируем auth_window для перехода обратно к окну авторизации
import auth_window

class MainWindow(QMainWindow):
    def __init__(self, username, user_manager):
        super().__init__()
        self.setWindowTitle("Главное окно")

        # Сохраняем имя пользователя и ссылку на UserManager
        self.username = username
        self.user_manager = user_manager
        self.user_info = self.user_manager.get_user_info(username)

        # Инициализируем пользовательский интерфейс
        self.init_ui()

    def init_ui(self):
        # Создаем центральный виджет
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Создаем вертикальный лэйаут
        layout = QVBoxLayout()

        # Добавляем метки с информацией о пользователе
        self.name_label = QLabel(f"Имя: {self.user_info['name']}")
        layout.addWidget(self.name_label)

        self.surname_label = QLabel(f"Фамилия: {self.user_info['surname']}")
        layout.addWidget(self.surname_label)

        self.email_label = QLabel(f"Электронная почта: {self.user_info['email']}")
        layout.addWidget(self.email_label)

        # Добавляем кнопку для редактирования данных
        self.edit_button = QPushButton("Редактировать")
        self.edit_button.clicked.connect(self.show_edit_window)
        layout.addWidget(self.edit_button)

        # Устанавливаем лэйаут для центрального виджета
        self.central_widget.setLayout(layout)

        # Создаем меню
        menubar = self.menuBar()

        # Добавляем пункты меню
        file_menu = menubar.addMenu("Меню")

        logout_action = QAction("Сменить пользователя", self)
        logout_action.triggered.connect(self.logout)
        file_menu.addAction(logout_action)

        exit_action = QAction("Выход", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

    def show_edit_window(self):
        # Показываем окно редактирования
        self.edit_window = EditWindow(self.username, self.user_manager)
        self.edit_window.data_updated.connect(self.update_user_info)
        self.edit_window.show()

    def logout(self):
        # Переходим к окну авторизации
        self.auth_window = auth_window.AuthWindow()
        self.auth_window.show()
        self.close()

    def update_user_info(self):
        # Обновляем информацию о пользователе после редактирования
        self.user_info = self.user_manager.get_user_info(self.username)
        self.name_label.setText(f"Имя: {self.user_info['name']}")
        self.surname_label.setText(f"Фамилия: {self.user_info['surname']}")
        self.email_label.setText(f"Электронная почта: {self.user_info['email']}")
