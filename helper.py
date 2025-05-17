import faker
from faker import Faker

faker = Faker()

def generate_registration_data(name_length=5):

    name = faker.first_name()
    surname = faker.last_name()
    address = faker.address()
    phone_number = faker.phone_number()
    return name, surname, address, phone_number
