# Data Type: List --> ordered collection
integer_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
heterogeneous_list = ['String', 0.1, True]
list_of_lists = [integer_list, heterogeneous_list]

list_length = len(integer_list)
list_sum = sum(integer_list)
x = integer_list

print(x[0])
print(x[1])
print(x[-1])
print(x[-2])
x[0] = -1
print(x[0])
x[0] = 10
print(x[:3])
print(x[:])
print(x[3:])
print(x[1:3])
print(x[::2])
print(1 in [1, 2, 3])
x.extend([21, 22, 23])
print(x)
x.append(24)
print(x)
a, b = [1, 2]
print(a, b)

# Data Type: Tuple --> immutable list
my_list = [1, 2]
my_tuple = (1, 2)
empty_tuple = ()
print(empty_tuple, my_tuple)
other_tuple = 1, 2
try:
    my_tuple [1] = 3 # cannot modify
except TypeError:
    print ("cannot modify tuple")

# Data Type: Dictionaries --> key/value pairs
empty_dict = {}
empty_dic2 = dict()
grades = {"john": 80, "Tim": 90}  # dictionary literal
print("John grade is", grades["john"])
try:
    print("Kate grade is", grades["kate"])
except KeyError:
    print('cannot find dictionary key pair')

print("john has grade in", "john" in grades)
print("John has grade in", "John" in grades)
# when lookup fails, returns default values
print(grades.get("john", 12))
print(grades.get("Kate", 0))
print(grades.get("mary"))
grades["simon"] = 75
print(len(grades))
print(grades)
print(grades.keys())
print(grades.values())
print(grades.items())
print(75 in grades.values())

document = ['mango', 'strawberry', 'banana', 'mango', 'strawberry', 'banana', 'pineapple', 'kiwi']
lookup = ['mango', 'strawberry', 'banana']
count = {'mango': 0, 'strawberry': 0, 'banana': 0}
print('document:', len(document))
i = 0
for words in document:
    print("searching for:", words)
    if words in lookup:
        print(words, "found")
        count[words] += 1
    else:
        print(words, "not found")
print(count)

Data Type: Default Dictionaries --> from Collections , default value with 0

from collections import defaultdict
words_count = defaultdict(int) # produces 0
print(words_count)
print(words_count["test"])

my_defaultdict = defaultdict(list)
print(my_defaultdict, my_defaultdict["test"])
my_defaultdict = defaultdict(dict)
print(my_defaultdict, my_defaultdict["test"])
my_defaultdict = defaultdict(lambda: [0, 1, 2])
print(my_defaultdict)
print(my_defaultdict[122])

# Data Type: Counters --> turns sequence of values into default dictionary
from collections import Counter
my_counter = Counter([1, 2, 3])
my_counter2 = Counter({1, 2, 3})
my_counter3 = Counter(['mango', 'strawberry', 'banana', 'mango', 'strawberry', 'banana', 'pineapple', 'kiwi'])
print (my_counter)
print(my_counter2)
print(my_counter3)
for word, count in my_counter3.most_common():
    print(word, count)

# Data Type: Sets --> collection of distinct elements
my_set = {'mango', 'banana', 'mango', 'strawberry'}
print(len(my_set))
my_set2 = {}
print(len(my_set2))
my_set3 = set()
my_set3.add(1)
my_set3.add(2)
print(my_set3)
y = 2 in my_set3
print(y)

# Control flow
if 2 > 3:
    print ("one is greater than 2")
elif 2 > 4:
    print("two is greater than three")
else:
    print('end of loop')

x = 2
parity = "even" if x % 2 == 0 else "odd"
print (parity)

x = 0
while x < 10:
    print(f"{x} is less than 10")
    x+= 1

for x in range(10):
    print(x)


# Boolean
test = 1 < 2
print(test)
try:
    assert test is False
except AssertionError:
    print('assertion failed')
x = None
assert x is not None
assert 1 + 1 == 3, "1 + 1 not equals 3"
def find_min(x):
    assert x, "empty variable"
    return min(x)
assert find_min([1,2,3,4]) == 1
assert find_min([])
x = 1
s = x and 0
print(s)
m = 2 if x < 0 else "3"
print(m)
print(all([1, 0])) # all should be true
print(any([1, 0])) # any should be true
print(all([True, 1, {}]))
print(any([True, 1, {}]))

# Sorting
my_list = [4,3,2,1]
my_tuple = (4,3,2,1)
my_dict = {"four":4, "three":3, "two":2, "one":1}
my_set = {4,3,2,1}
print(sorted(my_list))
print(sorted(my_tuple))
print(sorted(my_dict))
print(sorted(my_set))
print(sorted(my_list, key=abs, reverse=True))

List Comprehension
even_list = [x for x in range(10) if x % 2 == 0 ]
print(even_list)
square_list = [x*x for x in range(10)]
even_squares = [x*x for x in even_list]
print(square_list)
print(even_squares)
even_dictionary = {x:x*x for x in range(10)}
print(even_dictionary)
even_set = {x*x for x in range(10)}
print(even_set)
zero_list = [0 for _ in range(10)]
print(zero_list)
tuple_pairs = [(x, y)
               for x in range(10)
               for y in range(10)
               ]
tuple_pairs = [(x, x)
               for x in range(10)
               ]
print (tuple_pairs)

Object oriented Programming (OOP)

class CountingClicker:
    """This is a class that keeps count of how many people passed through the gate.
    It has member counter and member function clicked(), read_count() and reset"""

    def __init__(self, count=0):
        self.count = count

    def __repr__(self):
        return f"CountingClicker(count={self.count})"

    def click(self, num_times=1):
        self.count = num_times

    def read(self):
        return self.count

    def reset(self):
        self.count = 0


clicker1 = CountingClicker()
clicker2 = CountingClicker(100)
clicker3 = CountingClicker(count=200)
clicker1.read()
clicker2.click()
clicker3.click(num_times=200)
print(clicker1.read(), clicker2.read(), clicker3.read())
clicker3.reset()
print(clicker3.read())
assert clicker3.read() == 0, "counter not 0"
print(clicker2)

# a subclass inheriting all the behaviour of parent class
class SubClassCountingClikcer(CountingClicker):
    def reset(self):
        pass # does nothing

clicker4 = SubClassCountingClikcer()
clicker4.click(num_times=23)
print(clicker4)
clicker4.reset()
print(clicker4)

Iterables and Generators
# Generators creates the values lazily (on demand)
def generate_range(range=100):
    i = 0
    while i < range:
        yield i
        i+=1

for i in generate_range(10):
    print(f"i: {i}")

even_numbers = (i for i in generate_range(100) if i  % 2 == 0)
print(i)

names = ['Alice', 'Bob', 'Sandy', 'Susan']
for i, name in enumerate(names):
    print(f"{i}: {names[i]}")

Randomness
import random as r

r.seed(100)  # to get same result every time
four_random_nos = [x for x in range(5)]
print(four_random_nos)
four_random_nos = [r.random() for _ in range(5)]
print(four_random_nos)
four_random_nos = [r.random() for _ in range(5)]
print(four_random_nos)
four_random_nos = [r.randrange(10) for _ in range(5)]
print(four_random_nos)
four_random_nos = [r.randrange(3, 10) for _ in range(5)]
print(four_random_nos)
upto_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r.shuffle(upto_ten)
print(upto_ten)
names = ['Alice', 'Bob', 'Sandy', 'Susan']
print(r.choice(names))
print(r.sample(range(10),4)) # no repeat
print([r.choice(range(10)) for _ in range(4)]) # repeat

Regular Expression

import re
re_examples = [
    not re.match('a', 'cat'), # returns false, cat doesn't start with a
    re.search('a', 'cat') != None, # cat has a
    not re.search('dog', 'cat'), # cat doesn't have dog
     len(re.split('[ab]', 'carbs')) == 3, # split on a or b to c, r, s
    'R-D-' == re.sub('[0-9]','-','R2D2') # replace numbers with -
]
print(re_examples)
print(re.search("a", "cat") != None)
assert all(re_examples), "All regex should be true"

Zip and argument unpacking
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']
#print([pair for pair in zip(list1, list2)])
pairs = [('a',1), ('b',2), ('c', 3), ('d', 4)]
print(pairs)
letters, numbers = zip(*pairs)
print(letters)
print(numbers)

args and kwargs
def doubler(f):
    def g(x):
        return 2 * f(x)
    return g
def f1(x):
    return x + 1
g = doubler(f1)
assert g(3) == 8

def magic(*args, **kwargs):
    print('unnamed args:', args)
    print('keyword args:',kwargs)

magic(1,2,name='John',gender='male')

Type annotation
to differentiate between dynamic and static type annotation
def dynamic_add(a,b):
    return a + b
print(dynamic_add(10,5)) # 10 + 5 -> 15
print(dynamic_add([1,2],[3])) # [1, 2] + [3] -> [1,2,3]
print(dynamic_add('hello', 'world')) # 'hello' + 'world' -> 'hello world'
print(dynamic_add("hello",5)) # cannot concatenate
def static_add(a: int, b: int) -> int:
    return a + b

print (static_add(10,15))
print(static_add(['hello','world'],[1]))

from typing import List
Number = int
Numbers = List[Number]
def total(xs: Numbers) -> Number:
    return sum(xs)