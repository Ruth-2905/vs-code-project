def is_even(number):
    if number <= 1:
        return False
    
    if number % 2 == 0:
        return True
    
    return False


def get_even_numbers(num):
    even_numbers = []
    if num <= 1:
        return even_numbers
    
    for i in range(2, num + 1):
        if i % 2 == 0:
            even_numbers.append(i)
            print(f"{i} is even")
    return even_numbers 

if __name__ == "__main__":
    even_nums = get_even_numbers(100)
    print(even_nums) 
    #print(is_even(9)) 

    