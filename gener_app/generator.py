from faker import Faker
from typing import NamedTuple


class User(NamedTuple):
    name:str
    email:str

def gener_one() -> User:
    faker = Faker()
    return User(faker.name(), faker.email())


def gener_users(amount):
    for i in range(amount):
        yield gener_one()

