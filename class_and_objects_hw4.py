# Задание "Свой YouTube"

import time

class User:
    """
    Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
    """
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.age = int(age)
        self.password = int(password)

    def __str__(self):
        return self.nickname

    def __hash__(self):
        return hash(int(self.password))


class Video:
    """
    Атрибуты: title(заголовок, строка), duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """
    def __init__(self, title, duration, time_now = 0, adult_mode: bool = False):
        self.title = str(title)
        self.duration = duration
        self.time_now = time_now
        self.adult_mode =adult_mode


    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item in self.title


class UrTube:
    """
    Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
    """
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        password = hash(password)
        for user in self.users:
            if user.nickname == nickname:
                print('Пользователь ', nickname, ' уже существует.')
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user

    def log_out(self, current_user):
        self.current_user = None

    def get_videos(self, s_word):
        list_videos = []
        for video in self.videos:
            if s_word.upper() in video.title.upper():
                list_videos.append(video.title)
        return list_videos

    def add(self, *args):
        for movie in args:
            if movie not in self.videos:
                self.videos.append(movie)

    def watch_video(self, movie: str):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for x in self.videos:
            if x.title == movie:
                if x.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    return

                for i in range(x.duration):
                    print(i, end=' ')
                    x.time_now += 1
                x.time_now = 0
                print('Конец видео')

if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео

    ur.add(v1, v2)

    # Проверка поиска

    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение

    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт

    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео

    ur.watch_video('Лучший язык программирования 2024 года!')