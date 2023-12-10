from random import randint
from faker import Faker


class Helpers:
    # Генерация случайного email
    @staticmethod
    def fake_email():
        faker = Faker()
        fake_email = faker.email()
        return fake_email

    # Генерация случайного пароля
    @staticmethod
    def password():
        password = randint(100000, 9999999)
        return password
