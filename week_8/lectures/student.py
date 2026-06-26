class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # GETTER
    @property
    def house(self):
        return self._house

    # SETTER
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("InvalidHouse")
        self._house = house


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()


# --- Visual ---

# student.house = "Ravenclaw"
#         │
#         ▼
#     SETTER runs
#         │
#         ▼
#     self._house = "Ravenclaw"   (value is now stored)

# print(student.house)
#         │
#         ▼
#     GETTER runs
#         │
#         ▼
#     return self._house   (returns "Ravenclaw")
#         │
#         ▼
#     prints "Ravenclaw"
