import faker


def get_faker_user() -> dict:
    fake = faker.Faker()
    email = fake.email()
    password = fake.password(7)
    name = fake.name()
    return {"email": email, "password": password, "name": name}
