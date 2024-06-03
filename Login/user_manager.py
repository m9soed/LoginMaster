import json
import re

class UserManager:
    def __init__(self, filename="users.json"):
        # Инициализация UserManager с указанием имени файла для хранения данных пользователей
        self.filename = filename
        self.load_users()

    def load_users(self):
        # Загрузка данных пользователей из файла
        try:
            with open(self.filename, 'r') as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.users = {}

    def save_users(self):
        # Сохранение данных пользователей в файл
        with open(self.filename, 'w') as file:
            json.dump(self.users, file, indent=4)

    def authenticate_user(self, login, password):
        # Аутентификация пользователя по логину и паролю
        return login in self.users and self.users[login]['password'] == password

    def get_user_info(self, login):
        # Получение информации о пользователе по логину
        return self.users.get(login, {})

    def update_user_info(self, login, name, surname, email):
        # Обновление информации о пользователе
        if login in self.users:
            self.users[login]['name'] = name
            self.users[login]['surname'] = surname
            self.users[login]['email'] = email
            self.save_users()

    def add_user(self, login, password, name, surname, email):
        # Добавление нового пользователя
        if login in self.users:
            return False
        self.users[login] = {
            'password': password,
            'name': name,
            'surname': surname,
            'email': email
        }
        self.save_users()
        return True

    def is_password_strong(self, password):
        # Определение сложности пароля: минимум 8 символов, хотя бы одна цифра, одна заглавная и одна строчная буква
        if len(password) < 8:
            return False
        if not re.search(r"\d", password):
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        return True
