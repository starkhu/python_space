class cls(object):
    val =1

c = cls()
print(getattr(c, 'val'))
print(getattr(c, 'val1', 2)) #r如果没有该属性值，默认设置为2

print(getattr(class_test, cls, None))

