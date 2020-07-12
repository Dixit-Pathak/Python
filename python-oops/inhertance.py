from sklearn.datasets import fetch_olivetti_faces
import datetime

# Load the dataset
faces = fetch_olivetti_faces()

# Prove that the dataset was loaded
#print(faces.data.shape)

class Person:
    def __init__(self, name, photo, date_of_birth):
        self.name = name
        self.photo = photo
        self.dob = date_of_birth

    def get_age(self):
        return int((datetime.datetime.now() - self.dob).days / 365.25)

    def __str__(self):
        return self.name + ', age ' + str(self.get_age())

class MissingPerson(Person):
    def __init__(self, name, photo, date_of_birth, date_missing):
        # Construct the base object
        Person.__init__(self, name, photo, date_of_birth)

        # Add a missing_since attribute
        self.missing_since = date_missing

    # Add a get_years_missing() method
    def get_years_missing(self):
        return int((datetime.datetime.now() - self.missing_since).days / 365.25)

# aPerson = MissingPerson("Adam", faces.images[0], datetime.datetime(1990, 9, 16), datetime.datetime(2016, 1, 1))
# print(aPerson.name + ' has been missing for ' + str(aPerson.get_years_missing()) + ' years')
# print(dir(aPerson))

class MissingSKPerson(MissingPerson):
    def __init__(self, name, photo, date_of_birth, date_missing):
        MissingPerson.__init__(self, name, photo, date_of_birth, date_missing)

    # Override the get_age() method
    def get_age(self):
        return super().get_age() + 1

date_birth = datetime.datetime(1990, 9, 16)
date_missing = datetime.datetime(2016, 1, 1)
face = faces.images[0]
name = "Adam"

aPerson = Person(name, face, date_birth)
print(str(aPerson.get_age()))

aPerson = MissingPerson(name, face, date_birth, date_missing)
print(str(aPerson.get_age()))

aPerson = MissingSKPerson(name, face, date_birth, date_missing)
print(str(aPerson.get_age()))

class AnonymousPerson(Person):
    def __init__(self, photo, date_of_birth):
        Person.__init__(self, '', photo, date_of_birth)
        delattr(self, 'name')

aPerson = AnonymousPerson(faces.images[0], datetime.datetime(1990, 9, 16))

