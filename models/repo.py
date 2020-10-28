class Repo:
    
    __slots__ = ['__id', '__name', '__stars']
    
    def __init__(self, id, name, stars):
        self.__id = id
        self.__name = name
        self.__stars = stars
    
    def __str__(self):
        return f'id: {self.__id} - name: {self.__name} - stars: {self.__stars}'
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def stars(self):
        return self.__stars
