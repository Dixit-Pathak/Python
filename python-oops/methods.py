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

aPerson = Person("Adam", faces.images[0], datetime.datetime(1990, 9, 16))

print(str(aPerson.get_age()))

print(str(aPerson))
print(aPerson.__str__())
print(aPerson)