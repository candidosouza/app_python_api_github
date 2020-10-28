class WriterMeta(type):

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return hasattr(subclass, 'write') and callable(subclass.write)


class WriterInterface(metaclass=WriterMeta):

    @staticmethod
    def write(report):
        raise NotImplementedError
