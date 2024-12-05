class User:


    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __hash__(self):
        return hash(self.password)

class Video:

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = False

class UrTube(User, Video):

    def log_in(self, nickname, password):
        self.nickname = nickname
        self.password = password
        if self.nickname == User.__init__(nickname):
            print('Есть такой пользователь')
        else: print('Нет такого пользователя')

    def log_out(self):
        self.user = None




us1 = User('Serg', '258', 62)




# v1 = Video('Лучший язык программирования 2024 года', 200)
# print(v1.title, v1.duration, v1.time_now, v1.adult_mode)
