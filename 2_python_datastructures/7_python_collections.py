# python collection module
import collections

# collection module is defined as a container that is used to store collections
# of data, like list,dict,set and tuple

# 1.namedtuple()
# it returns a tuple-like object with names for each position in the
# tuple. It was used to eliminate the problem of remembering the index of
# each field of a tuple object in ordinary tuples
# to use namedtuple we need to import from collections import namedtuple

print("* namedtuple()")
from collections import namedtuple

p_tuple = namedtuple("p_tuple",["python","java","cpp"])
language = p_tuple("python","java","cpp")
print("item at index python:",language.python)
print("item at index java:",language.java)
print("item at index cpp:",language.cpp)


# 2.OrderedDict()
# in OrderedDict() keys maintain the order of insertion. If we try to insert key
# again, the previous value will be overwritten for that key
print("\n* OrderedDict()")

o_dict = collections.OrderedDict()
o_dict[1] = "python"
o_dict[3] = "cpp"
o_dict[2] = "java"
print("OrderedDict():",o_dict)


# 3.defaultdict()
# it is a subclass of the built-in dict class. It provides all methods
# provided by dictionary but takes the first argument as a default data type
print("\n* defaultdict()")

from collections import defaultdict

d_dict = defaultdict(str)
d_dict[1] = "python"
d_dict[2] = "java"
d_dict[3] = "cpp"

print("defaultdict():",d_dict)


# 4.Counter()
# Counter() is a subclass of dictionary object which helps to count hashable
# objects like counting frequency
print("\n* Counter()")

p_list = [1,2,1,5,6,5,8,6,1]
f_counter = collections.Counter(p_list)
print("frequency:",f_counter)
for i in f_counter.items():
    print(i)


# 5.deque()
# it is double-ended queue which allows us to add and remove elements from
# both the ends
# use cases
# 1.queue FIFO
# 2.stack LIFO
# 3.sliding window
# 4.history tracking

print("\n* deque()")

from collections import deque

p_deque = deque([1,2,3,4])
print("p_deque:",p_deque)

p_deque.append(5)
print("added to right:",p_deque)
p_deque.appendleft(10)
print("added to left:",p_deque)
p_deque.pop()
print("pop from right:",p_deque)
p_deque.popleft()
print("pop from left:",p_deque)
p_deque.rotate(1)
print("rotated right:",p_deque)
p_deque.rotate(-1)
print("rotated left:",p_deque)
p_deque.extend([10,20,30])
print("added multiple items:",p_deque)
p_deque.extendleft([90,80,70])
print("added multiple items to left:",p_deque)
p_deque.clear()
print("cleared p_deque:",p_deque)


# 6.ChainMap()
# is used to combine multiple dictionaries into a single list
print("\n* ChainMap()")

from collections import ChainMap

p_dict = {
    "lang_1":"python",
    "lang_2":"java"
}
n_dict = {
    "lang_3":"cpp",
    "lang_4":"perl"
}
m_dict = {
    "lang_5":"javascript",
    "lang_6":"golang"
}

def print_dict(message,user_dict):
    print(message)
    for i in user_dict.items():
        print(i)

print_dict("p_dict:",p_dict)
print()
print_dict("n_dict:",n_dict)
print()
print_dict("m_dict:",m_dict)
print()
dict_list = ChainMap(p_dict,n_dict,m_dict)
print("combined dict:")
for i in dict_list.items():
    print(i)

# 7.UserString
# A wrapper around regular strings that behaves like a string
# 8.UserList
# A wrapper around a list, useful when you want to extend or override list behavior.
# 9.UserDict
# A wrapper around a dictionary, helpful for customizing dictionary behavior.

# class	      wraps	   useful when you want to
# UserString   str	   customize string methods or behaviors
# UserList	   list	   add validation or tracking to list actions
# UserDict	   dict	   intercept key assignments, customize dicts