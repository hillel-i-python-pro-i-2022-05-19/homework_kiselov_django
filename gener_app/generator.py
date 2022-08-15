from typing import NamedTuple

from faker import Faker


class User(NamedTuple):
    name: str
    email: str


def generate_one_user() -> User:
    faker = Faker()
    return User(faker.name(), faker.email())


def generate_users(amount):
    for _ in range(amount):
        yield generate_one_user()
