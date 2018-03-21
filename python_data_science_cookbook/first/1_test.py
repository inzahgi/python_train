import numpy as np
import io
from collections import defaultdict
from collections import Counter
from collections import namedtuple
from sklearn.metrics import jaccard_similarity_score
from random import shuffle
from math import log
from string import punctuation
from operator import itemgetter
from operator import attrgetter
from operator import methodcaller
from itertools import chain, compress, combinations,count,islice


##1.2
sentence = "Peter Piper picked a peck of pickled peppers A peck of pickled  \
           peppers Peter Piper picked If Peter piper picked a peck of pickled \
           peppers Where the peck of pickled peppers Peter Piper picked "


word_dict = {}
for word in sentence.split():
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

print(word_dict)

## 每次赋值前判断
word_dict_1 = {}
for word in sentence.split():
    ## D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
    word_dict_1.setdefault(word, 0);
    word_dict_1[word] += 1
print(word_dict_1)


## int()作为参数传递进字典 当没有某个key后 返回int()的返回值0
word_dict_2 = defaultdict(int)
for word in sentence.split():
    word_dict_2[word] += 1
print(word_dict_2)


##Counter是一个字典类
word_dict_3 = Counter(sentence.split())
print(word_dict_3)

print("\n\n")
print("1.3\n")
##1.3
user_mpvice_rating = defaultdict(lambda :defaultdict(int))
user_mpvice_rating["Alice"]["LOR1"] = 4
user_mpvice_rating["Alice"]["LOR2"] = 5
user_mpvice_rating["Alice"]["LOR3"] = 3
user_mpvice_rating["Alice"]["SW1"] = 5
user_mpvice_rating["Alice"]["SW2"] = 3
print(user_mpvice_rating)


print("\n\n")
print("1.4\n")
##1.4
a_tuple = (1, 2, '1')
b_tuple = 1,2,'c'

print(b_tuple[0])
print(b_tuple[-1])

try:
    b_tuple[0] = 20
except:
    print("cannot change value of tuple by index")

c_tuple = (1, 2, [10,20,30])
c_tuple[2][0] = 1000

print(a_tuple + b_tuple)

a = (1,2,3,4,5,6,7,8,9,10)
print(a[1:])
print(a[1:3])
print(a[1:6:2])
print(a[:-1])

print(min(a), max(a))

if 1 in a:
    print("Element 1 is available in tuple a")
else:
    print("Element 1 is available in tuple a")


vector = namedtuple("Dimension", 'x y z')
vec_1 = vector(1,1,1)
vec_2 = vector(1,0,1)

manhattan_distance = abs(vec_1.x - vec_2.x) + abs(vec_1.y - vec_2.y) \
    + abs(vec_1.z - vec_2.z)
print("Manhattan distance between vectors = %d"%manhattan_distance)


##1.5

print("\n\n")
print("1.5\n")

st_1 = "dog chase cats"
st_2 = "dog hate cats"

st_1_words = set(st_1.split())
st_2_words = set(st_2.split())

no_word_st_1 = len(st_1_words)
no_word_st_2 = len(st_2_words)

cmn_words = st_1_words.intersection(st_2_words)
no_cms_words = len(st_1_words.intersection(st_2_words))

unq_words = st_1_words.union(st_2_words)
no_unq_words = len(st_1_words.union(st_2_words))

similarity = no_cms_words / (1.0 * no_unq_words)

print("No words in sent_1 = %d"%no_word_st_1)
print("Sentence 1 words = ", st_1_words)
print("No words in sent_2 = %d"%no_word_st_2)
print("Sentence 2 words = ", st_2_words)
print("No words in common = %d"%no_cms_words)
print("Common words = ", cmn_words)
print("Total unique words = %d"%no_unq_words)
print("Unique words = ", unq_words)
print("Similarity = No words in common / No unique words, %d/%d \
      = %.2f"%(no_cms_words, no_unq_words, similarity))


a = [ 1 if w in st_1_words else 0 for w in unq_words]
b = [ 1 if w in st_2_words else 0 for w in unq_words]

print(a)
print(b)
print(jaccard_similarity_score(a,b))



print("\n\n")
print("1.6\n")
##1.6
a = range(1, 10)
print(a)
b = ["a", "b", "c"]
print(b)

print(a[0])

a[-1]

print(a[1:3])
print(a[1:])
print(a[-1:])
print(a[:-1])

a = [1, 2]
b = [3,4]
print(a + b)

print(min(a), max(a))

if 1 in a:
    print("Element 1 is available in list a")
else:
    print("Element 1 is available in tuple a")

a = list(range(1, 10))
print(a)
a.append(10)
print(a)

a_stack = []

a_stack.append(1)
a_stack.append(2)
a_stack.append(3)

print(a_stack.pop())
print(a_stack.pop())
print(a_stack.pop())

a_queue = []
a_queue.append(1)
a_queue.append(2)
a_queue.append(3)

print(a_queue.pop(0))
print(a_queue.pop(0))
print(a_queue.pop(0))


a = list(range(1, 20))
shuffle(a)
print(a)
a.sort()
print(a)
a.reverse()
print(a)


print("\n\n")
print("1.7\n")

## 1.7
a = [1,2,-1,-2,3,4,-3,-4]
b=[pow(x,2) for x in a if x < 0]
print(b)

a = {'a':1, 'b':2,'c':3}
b = {x:pow(y,2) for x, y in a.items()}
print(b)

def process(x):
    if isinstance(x, str):
        return x.lower()
    elif isinstance(x, int):
        return x*x
    else:
        return -9

a = (1,2,-1,-2,'D',3,4,-3,'A')
b = tuple(process(x) for x in a)
print(b)

class SimpleCounter(object):
    def __init__(self, start, end):
        self.current = start
        self.end = end
    def __iter__(self):
        'Returns itself as an iterator object'
        return self
    def next(self):
        'Returns the next value till current is lower than end'
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

c = SimpleCounter(1,3)
print(c.next())
print(c.next())
print(c.next())
# print(c.next())


###   ?????
# c = SimpleCounter(1,3)
# for entry in iter(c):
#     print(entry)



print("\n\n")
print("1.9\n")

###1.9
SimpleCounter = (x**2 for x in range(1,10))
tot = 0
for val in SimpleCounter:
    tot += val
print(tot)

def my_gen(low, high):
    for x in range(low, high):
        yield x**2
tot = 0

gen = (x**2 for x in range(1, 10))
for val in iter(gen):
    print(val)



print("\n\n")
print("1.10\n")

class SimpleIterable(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end;
    def __iter__(self):
        for x in range(self.start, self.end):
            yield x**2

c = SimpleIterable(1, 10)
tot = 0
for val in iter(c):
    tot += val
print(tot)

tot = 0
for val in iter(c):
    tot += val
print(tot)



print("\n\n")
print("1.11\n")

#### 1.11
def square_input(x):
    return x*x
square_me = square_input
print(square_me(5))


print("\n\n")
print("1.12\n")

### 1.12
def sum_square(x):
    def square_input(x):
        return x*x
    return sum([square_input(x1) for x1 in x])

print(sum_square([2,4,5]))


print("\n\n")
print("1.13\n")


def square_input(x):
    return x*x
def apply_func(func_x, input_x):
    return map(func_x, input_x)
a = [2,3,4]
print(list(apply_func(square_input, a)))
print(list(apply_func(log, a)))



print("\n\n")
print("1.14\n")

def cylinder_vol(r):
    pi = 3.141
    def get_vol(h):
        return pi *r**2*h
    return get_vol
radius = 10
find_volume = cylinder_vol(radius)
height = 10
print("Volume of cylinder of radius %d and height %d = %.2f cubic \
      units"%(radius, height, find_volume(height)))
height = 20
print("Volume of cylinder of radius %d and height %d = %.2f cubic \
      units"%(radius, height, find_volume(height)))


print("\n\n")
print("1.15\n")
#### 1.5

def pipeline_wrapper(func):
    def to_lower(x):
        print(x)
        return x.lower()
    def remove_punc(x):
        for p in punctuation:
            x = x.replace(p, '')
        return x
    def wrapper(*args, **kwargs):
        x = to_lower(*args, **kwargs)
        x = remove_punc(x)
        return func(x)
    return wrapper

@pipeline_wrapper
def tokenize_whitespace(inText):
    return inText.split()

s = "string. With. Punctuation?"
print(tokenize_whitespace(s))



print("\n\n")
print("1.16\n")
## 1.16
a = [10, 20, 30]
def do_list(a_list, func):
    total = 0
    for element in a_list:
        total += func(element)
    return total

print(do_list(a, lambda x:x**2))
print(do_list(a, lambda x:x**3))


print("\n\n")
print("1.17\n")
##  1.17
a=[10,20,30]
print(list(map(lambda x:x**2, a)))
print(list(map(lambda x:x**3, a)))
print(sum(list(map(lambda x:x**2, a))))
print(sum(list(map(lambda x:x**3, a))))
b = [1,2,3]
print(list(map(pow,a,b)))

print("\n\n")
print("1.18")
###### 1.18
a=[10,20,30,40,50]
print(list(filter(lambda x:x>10, a)))

print("\n\n")
print("1.19\n")

#### 1.19
print(list(zip(range(1,5), range(1,5))))
a=(2,3)
print(pow(*a))
a_dict = {"x":10,"y":10,"z":10,"x1":10, "y1":10, "z1":10}
def dist(x,y,z,x1,y1,z1):
    return abs((x-x1)+(y-y1)+(z-z1))
print(dist(**a_dict))

def any_sum(*args):
    tot = 0
    for arg in args:
        tot += arg
    return tot
print(any_sum(1,2))
print(any_sum(1,2,3))



print("\n\n")
print("1.20\n")
#### 1.20

in_data = io.StringIO("10,20,30\n56, 89,90\n33,46,89")
data = np.genfromtxt(in_data, dtype=int, delimiter=",")
print(data)

in_data = io.StringIO("10,20,30\n56, 89,90\n33,46,89")
data = np.genfromtxt(in_data, dtype=int, delimiter=",",usecols=(0,1))
print(data)

in_data = io.StringIO("10,20,30\n56, 89,90\n33,46,89")
data = np.genfromtxt(in_data, dtype=int, delimiter=",", names="a,b,c")
print(data)


print("\n\n")
print("1.21\n")
######  1.21
in_data = io.StringIO("30kg, inr2000, 31.11, 56.33, 1 \
                      n52kg, inr8000.35,12, 16.7,2")
data = np.genfromtxt(in_data, delimiter=",")
print(data)

in_data = io.StringIO("30kg, inr2000, 31.11, 56.33, 1 \
                      n52kg, inr8000.35,12, 16.7,2")
strip_func_1 = lambda x : float(x.decode().rstrip("kg"))
strip_func_2 = lambda x : float(x.decode().lstrip("inr"))

convert_funcs = {0: strip_func_1, 1:strip_func_2}
data = np.genfromtxt(in_data, delimiter=",", converters=convert_funcs)
print(data)

in_data = io.StringIO("10,20,30\n56,,90\n33,46,89")
mss_func = lambda x : float(x.decode().strip() or -999)
data = np.genfromtxt(in_data, delimiter=",", converters={1:mss_func})
print(data)


print("\n\n")
print("1.22\n")
####  1.22

a = [8,0,3,4,5,2,9,6,7,1]
b = [8,0,3,4,5,2,9,6,7,1]
print(a)
a.sort()
print(a)

print(b)
b_s = sorted(b)
print(b_s)

a.sort(reverse=True)
print(a)

a=(8,0,3,4,5,2,9,6,7,1)
a_2 = sorted(a, reverse=True)
print(a_2)


print("\n\n")
print("1.23\n")
####   1.23
employee_records = [('joe', 1, 53), ('beck', 2,26), \
                    ('ele', 6, 32), ('neo',3, 45), \
                    ('christ', 5,33), ('trinity', 4, 29),]
print(sorted(employee_records, key=lambda emp : emp[0]))
print(sorted(employee_records, key=lambda emp : emp[1]))
print(sorted(employee_records, key=lambda emp : emp[2]))
print("\n")
print(sorted(employee_records, key=itemgetter(0)))
print(sorted(employee_records, key=itemgetter(1)))
print(sorted(employee_records, key=itemgetter(2)))
print("\n")
print(sorted(employee_records, key=itemgetter(0, 1)))


class employee(object):
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
    def pretty_print(self):
        print(self.name, self.id, self.id)
    def random_method(self):
        return self.age /self.id

employee_records = []
emp1 = employee('joe',1,53)
emp2 = employee('beck',2,26)
emp3 = employee('ele',6,32)

employee_records.append(emp1)
employee_records.append(emp2)
employee_records.append(emp3)

for emp in employee_records:
    emp.pretty_print()

print("\n")
employee_records_sorted = sorted(employee_records, key=attrgetter('age'))
for emp in employee_records_sorted:
    emp.pretty_print()
print("\n")
employee_records_sorted = sorted(employee_records, key=methodcaller('random_method'))
for emp in employee_records_sorted:
    emp.pretty_print()




print("\n\n")
print("1.24\n")
### 1.24

a = [1,2,3]
b = ['a','b','c']
print(chain(a,b))
print("\n")
a= [1,2,3]
b= [1,0,1]
print(list(compress(a,b)))
print("\n")
a = [1,2,3,4]
print(list(combinations(a,2)))
print("\n")
a = range(5)
## python3 zip  built in   same as python 2.7 itertools.izip
b = zip(count(1), a)

print("\n")
a = range(100)
b = islice(a,0,100,2)
print(list(b))