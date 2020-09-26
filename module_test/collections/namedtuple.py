import collections


# Person = collections.namedtuple("Person", ["name", "gender", "age", "class"], rename=True)
Person = collections.namedtuple("Person", 'name, gender, age,', rename=True)

obj = Person(name="Bob", gender="male", age=18)

print(obj.name)
print(obj.gender)
print(obj.age)

print(obj[0])
print(obj[1])
print(obj[2])

