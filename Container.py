class Container:
    __container = {}

    def __init__(self, clazz):
        self.__container[clazz.__name__] = clazz
        
        @classmethod
        def instanceGetter(self):
            return self.__container[clazz.__name__]
        instanceGetter.__name__ = "{}".format(clazz.__name__)
        setattr(Container, instanceGetter.__name__, instanceGetter)
