from random import randrange
import sys

def read_file(filepath):
    with open(filepath) as f:
        return f.readlines()

def pick_random(array):
    index = randrange(len(array))
    return array[index]

def split_in_half(perro):
    size = len(perro)//2
    first_half = randrange(2) == 0
    return perro[:size].rstrip() if first_half else perro[size:].rstrip()

def generate_venezuelan_name():
    names = read_file('nombres.txt')
    random_splitted = split_in_half(pick_random(names))
    random_splitted_2 = split_in_half(pick_random(names))
    return (random_splitted + random_splitted_2).title()

def generate_venezuelan_name_with_base(first, second):
    random_splitted = split_in_half(first)
    random_splitted_2 = split_in_half(second)
    return (random_splitted + random_splitted_2).title()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(generate_venezuelan_name())
    elif len(sys.argv) == 3:
        print(generate_venezuelan_name_with_base(sys.argv[1], sys.argv[2]))
        
        
    

