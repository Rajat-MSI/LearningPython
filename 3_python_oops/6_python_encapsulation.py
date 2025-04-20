# python encapsulation
# wrapping up of data in one single unit

# access modifiers in python
# 1.public (name)
# can be accessed anywhere in scope

# 2.protected (_name)
# can be accessed within classes and subclasses

# 3.private (__name)
# can be access only within single class
print("* access modifiers")
class Student:
    def __init__(self,__s_id,__name,__age,school,_address):
        self.__s_id = __s_id        # private member
        self.__name = __name        # private member
        self.__age = __age          # private member
        self.school = school        # public member
        self._address = _address    # protected member

# created student object
student = Student(100,
                  "tony stark",
                  25,
                  "school_name",
                  "tony_address")

try:
    print("error thrown now executing except block")
    print("s_id:",student.__s_id)
    print("name:",student.__name)
    print("age:",student.__age)
except:
    print("__s_id, __name, __age are private member")
    # to access private members python internally renames private variables
    # to avoid accidental access — this is called name mangling
    # name mangling: _Classname__attribute

    print("private - s_id:",getattr(student,"_Student__s_id"))
    print("private - name:",getattr(student,"_Student__name"))
    print("private - age:",getattr(student,"_Student__age"))
    print("public - school:",getattr(student,"school"))
    print("protected - address:",getattr(student,"_address"))


