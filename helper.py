from faker import Faker
from url import URL
import requests


class FakeData:
    @staticmethod
    def email():
        fake = Faker()
        email = fake.ascii_free_email()
        return email

    @staticmethod
    def password():
        fake = Faker()
        password = fake.password(length=10)
        return password

    @staticmethod
    def name():
        fake = Faker()
        name = fake.first_name()
        return name


class Body:
    @staticmethod
    def build_user_body(email, password, name):
        user_body = {
                "email": email,
                "password": password,
                "name": name
            }
        return user_body

    @staticmethod
    def build_login_pass_body(email, password):
        login_pass_body = {
                "email": email,
                "password": password
            }
        return login_pass_body


class Request:
    @staticmethod
    def create_user(body_user):
        return requests.post(f'{URL.ENDPOINT_CREATING_USER}', json=body_user)

    @staticmethod
    def login_user(login_pass):
        return requests.post(f'{URL.ENDPOINT_LOGIN}', data=login_pass)

    @staticmethod
    def delete_user(token):
        return requests.delete(f'{URL.ENDPOINT_USER}', headers={'Authorization': token})