class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class AuthService:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def register(self, username, password):
        if username in self.users:
            print("Пользователь уже существует!")
        else:
            self.users[username] = User(username, password)
            print(f"Пользователь {username} зарегистрирован!")

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            self.current_user = user
            print(f"Добро пожаловать, {username}!")
        else:
            print("Неверное имя пользователя или пароль!")

    def logout(self):
        if self.current_user:
            print(f"Пользователь {self.current_user.username} вышел из системы.")
            self.current_user = None
        else:
            print("Вы не авторизованы!")

    def access_resource(self):
        if self.current_user:
            print(f"Доступ к ресурсу для {self.current_user.username} предоставлен.")
        else:
            print("Доступ запрещен! Необходимо войти в систему.")

auth_service = AuthService()
auth_service.register("user1", "password123")
auth_service.login("user1", "password123")
auth_service.access_resource()
auth_service.logout()
auth_service.access_resource()
