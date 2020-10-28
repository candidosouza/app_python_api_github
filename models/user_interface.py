class UserMeta(type):

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return hasattr(subclass, 'work') and callable(subclass.work)


class UserInterface(metaclass=UserMeta):

    __slots__ = ['__username', '__email']

    def __init__(self, username, email):
        self.__username = username
        self.__email = email

    def __str__(self):
        return 'UserInterface()'

    def work(self):
        raise NotImplementedError
