#@property: 用法1：将类方法转换成类属性
#           用法2：当做装饰函数来用
#__slot__: 用来限定当前类（不包括其子类）只能绑定限制的属性
#          如果不加slot, 类可以动态添加属性
#super(): 给父节点同名函数传参。
#@staticmethod: 类的静态方法，给类调用的函数，不是给对象调用的函数

class Person(object):
    __slots__ = ('_name', '_age', '_gender')
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @staticmethod
    def is_valid_age(age):
        if age < 0:
            raise ValueError("valid age!")


    @property
    def full_name(self):
        return "%s %s" % (self._name, "Stark")

    @property
    def set_age(self):
        return self._age

    @set_age.setter
    def set_age(self, age):
        if isinstance(age, int):
            if age >= 0 and age <= 100:
                 self._age = age
            else:
                raise ValueError("illeage age")
        else:
            raise ValueError("illeage input")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade


def attr_test(tony):
    print(getattr(tony, '_age'))
    setattr(tony, '_age', 36)
    print(getattr(tony, '_age'))
    delattr(tony, '_age')
    if hasattr(tony, '_age'):
        print("not delete this attr")
    else:
        print("delete this attr")

def property_test(tony):
    print(tony. full_name)
    tony.set_age = 90
    print(tony.set_age)

def slot_test(tony):
    tony._gender = "man"
    print(tony._gender)
    #tony._height = 180 #wrong property


def main():
    #age = -10
    #if Person.is_valid_age(age):
    #   cook = Person("Cook", age)

    tony = Person("Tony", 25)
    #attr_test(tony)
    #property_test(tony)
    slot_test(tony)


if __name__ == "__main__":
    main()