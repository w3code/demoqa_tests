import random

from faker import Faker

from utils.get_birth_date import get_birth_date
from utils.get_path import get_path


class TestData:

    def __init__(self):
        faker = Faker()

        self.user_first_name: str = faker.first_name()
        self.user_last_name: str = faker.last_name()
        self.user_email: str = faker.email()
        self.user_gender: str = random.choice(["Male", "Female", "Other"])
        self.user_phone_number: str = faker.numerify("##########")
        self.user_age: str = str(faker.random_int(18, 60))
        self.user_salary: str = str(faker.random_int(10000, 100000))
        self.user_department: str = faker.word()
        self.user_birth_day, self.user_birth_month, self.user_birth_year = get_birth_date()
        self.user_subject: str = random.choice(
            ("Hindi", "English", "Maths", "Physics", "Chemistry", "Biology",
             "Computer Science", "Commerce", "Accounting", "Economics",
             "Arts", "Social Studies", "History", "Civics")
        )
        self.user_hobby: str = random.choice(["Sports", "Reading", "Music"])
        self.user_picture: str = get_path("picture.jpg")
        self.user_current_address: str = faker.address().replace("\n", " ")
        states_and_cities = {"NCR": ("Delhi", "Gurgaon", "Noida"),
                             "Uttar Pradesh": ("Agra", "Lucknow", "Merrut"),
                             "Haryana": ("Karnal", "Panipat"),
                             "Rajasthan": ("Jaipur", "Jaiselmer")}
        self.user_state: str = random.choice(list(states_and_cities.keys()))
        self.user_city: str = random.choice(states_and_cities[self.user_state])
