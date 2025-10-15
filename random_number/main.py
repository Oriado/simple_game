from random_utils import random_number, random_element, shuffle_list
from games import guess_number

def main():
    print("=== Random number generator ===\n")
    
    print("Random number 1-100:", random_number(1, 100))
    
    print("Random element from ['a', 'b', 'c']:", random_element(['a', 'b', 'c']))
    
    print("Shuffled list [1,2,3,4,5]:", shuffle_list([1, 2, 3, 4, 5]))
    
    print("\n=== 'Guess the Number' Game ===")
    guess_number()
    
if __name__ == "__main__":
    main()    