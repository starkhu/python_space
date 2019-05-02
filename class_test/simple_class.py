#@property: 用法1：将类方法转换成类属性
#           用法2：当做装饰函数来用

class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

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

def main():
    tony = Person("Tony", 35)
    #attr_test(tony)
    property_test(tony)


if __name__ == "__main__":
    main()