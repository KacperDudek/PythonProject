"""
Implementation of singleton. I do not know, if implementation
in "app" was good idea so I did it outside the app properly
"""


class Singleton(object):
    """
    Create class with Singleton
    """
    __instance = None
    """
    set instance as private and empty 
    """

    def __new__(cls, *args, **kwargs):
        """
        Creation instances of singleton
        """
        if not Singleton.__instance:
            Singleton.__instance = object.__new__(cls)
        return Singleton.__instance

    def __init__(self, first_name, last_name):
        """
        This is what code need to work properly
        :param first_name:
        :param last_name:
        """
        self.first_name = first_name
        self.last_name = last_name


"""
Check if Singleton is working
"""
s1 = Singleton("Kacper", "Dudek")
s2 = Singleton("Miłosz", "Kałas")
s3 = Singleton("Przemek", "Mońka")

print(s1)
print(s2)
print(s3)
print(s1.first_name)

if s1 == s2:
    print(s2.first_name)

if s1 == s3:
    print(s3.first_name)
