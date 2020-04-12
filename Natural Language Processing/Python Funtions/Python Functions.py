# coding: utf-8
#import driver2
from functools import reduce
from operator import mul
def alnum_fn(s):
    return s.isalnum();

def is_noun(s):
    return (s.startswith("NN"))
    

def is_even(i):
    if(i%2==0):
        return True
    else:
        return False
    
def add_one(v1):
    return [i+1 for i in v1] 

def drop_bad(v1):
    li = list(filter(lambda x:x.isalpha()==True,v1))
    return li;

def show_nouns(v1):
    return [i for i in v1 if i[1].startswith('N')]


def show_nouns2(v1):
    li= [i for i in v1 for j in i[1] if j.startswith('N')]
    return li;

def show_nouns3(v1):
    li = [i[0] for i in v1 for j in i[1] if j.startswith('N')]
    return li


def select_numbers(v1):
    return [i+1 for i in v1 if i%2==0]


def show_count(v1):
    li =list(map(lambda i : len(i),v1))
    li = reduce((lambda x,y : x + y),li)
    return li


def show_totals(v1):
    v1 = list(map(lambda i:reduce((lambda x,y : x + y),i),v1))
    return v1;


def show_total(v1):
    v1 = list(map(lambda i:reduce((lambda x,y : x + y),i),v1))
    v2 = reduce((lambda x,y:x+y),v1)
    return v2

def dot_product(v1):
   li = list(map(mul,v1[0],v1[1]))
   return reduce(lambda x,y:x+y,li); 

def remove_dot(v1):
    li = list(map(lambda i : i,v1[0:len(v1)-1]))
    return li;

def produce_lower(v1):
    v2 = list(map((lambda i : i.lower()),v1))
    return v2;

def count_words(v1):
    v2 = len(set(v1[0:len(v1)-1]))
    return v2


def avg_grade(v1):
    result = [j for i in v1 for counter,j in enumerate(i[2]) if counter==0]
    val = reduce(lambda x,y: x+y,result)
    val2 = float(len(result))
    return val/val2 

def ugrad_points(v1):
    result = [j for i in v1 for counter,j in enumerate(i[2]) if(counter==1 and i[1]=='u')]
    return reduce(lambda x,y: x+y,result)


def get_grades(stu, hw, grade_dict):
    if hw!=' ':
        return grade_dict[stu][hw];
    else:
        return 0

def add_student(i,v,grade_DB):
    grade_DB[i] = v;
    return grade_DB;





