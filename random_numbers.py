import random
 
def append_random_numbers(numbers_list, quantity = 1):
    for i in range(0,quantity):
        numbers_list.append(round(random.uniform(0,1000), 1))

 
def main():
    randnums = [16.2, 75.1, 52.3]
    append_random_numbers(randnums)
    print(randnums)
    append_random_numbers(randnums, 3)
    print(randnums)
 
main()