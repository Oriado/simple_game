import random

def random_number(start, end):
    return random.randint(start, end)

def random_element(lst):
    if not lst:
        return None
    return random.choice(lst)

def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled

if __name__ == ("__main__"):
    print("Random number 1-10: ", random_number(1,100))
    print("Random element from [1,2,3]:", random_element([1, 2, 3]))
    print("Shuffled list [1,2,3,4]:", shuffle_list([1, 2, 3, 4]))