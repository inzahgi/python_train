#!/usr/bin/python
# -*-coding:utf-8 -*-


class People:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.__score = s
        ##self.__print_people()

    def print_people(self):
        s = 'name = %s , age = %d, score = %0.2f'%(self.name, self.age, self.__score)
        print(s)

    __print_people = print_people

class Student(People):
    def __init__(self, n, a, w):
        People.__init__(self, n, a, w)
        self.name = 'Student ' + self.name

    def print_people(self):
        s = 'name = %s, age = %d'%(self.name, self.age)
        print(s)

def func(p):
    p.age=11


if __name__=='__main__':
    p = People('Tom', 10, 3.14159)
    func(p)
    p.print_people()
    print("\n")

    j = Student('Jerry', 12, 2.71828)
    print("\n")

    p.print_people()
    j.print_people()
    print("\n")

    People.print_people(p)
    People.print_people(j)
