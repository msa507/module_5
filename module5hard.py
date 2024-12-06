from webbrowser import register


class User:
    def __init__(self, nickname, hashpass, age):
        self.nickname = nickname
        self.password = hashpass
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode
        self.users = []
        self.current_user = None


class UrTube(User, Video):
    def __init__(self):
        users = User(self.nickname, self.hashpass, self.age)
        videos = Video(self.title)
        current_user = register(self.current_user)

    def log_in(self, login, password):
        hashpass = hash(password)
        for user in self.users:
            if (user.nickname == login) and (user.password == hashpass):
                self.current_user = user

    def register(self, nickname, hashpass, age):
        new_user = User(nickname, hashpass, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.user_user = None



# v1 = Video('Лучший язык программирования 2024 года', 200)
# v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)






