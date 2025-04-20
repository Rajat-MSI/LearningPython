# python custom exception

# custom exception class ResourceNotExistException and inherited properties
# from Exception base class
class ResourceNotExistException(Exception):

    # constructor to initialize resource name and value that will be
    # shown when resource is absent
    def __init__(self,name,value):
        self.name = name
        self.value = value

        # using python dynamic strings and setting values
        message = f"{name} does not exist with {value}"
        # calling super() to initialize the message into parent class
        super().__init__(message)

# user define function to simulate database
def get_user(user_id):

    # user dictionary
    users = {1:"tony stark",2:"thor",3:"bruce banner",4:"steven rogers"}
    # if user_id is in user dictionary then return user value
    # if user_id is absent then throw our custom exception
    if user_id in users:
        return users.get(user_id)
    else:
        # raised custom exception with resource name as user and
        # resource value as user_id
        raise ResourceNotExistException("user",user_id)

# if user is in dictionary get_user() will return user value
try:
    print(get_user(0))
except ResourceNotExistException as e:
    # if user is not in dictionary custom message will be printed
    print("message:",e)
