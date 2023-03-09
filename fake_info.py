import pandas as pd
from faker import Faker

fake = Faker()
fake.name()
fake.text()
fake.address()
fake.email()
fake.date()
fake.country()
fake.phone_number()
fake.random_number(digits=5)

fakeDataframe = pd.DataFrame(
    {
        "date": [fake.date() for _ in range(5)],
        "name": [fake.name() for _ in range(5)],
        "email": [fake.email() for _ in range(5)],
        "text": [fake.text() for _ in range(5)],
    }
)
print(fakeDataframe)
