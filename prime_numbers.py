
def is_prime(number):
    if number <= 1:
        return False

    if number >= 2:
        for i in range(2, int(number / 2) + 1):
            if number % i == 0:
                return False
    
    return True

if __name__ == "__main__":
    prime = is_prime(4)
    print(prime)

    prime_numbers = []

    for i in range(1, 250):
        if is_prime(i):
            prime_numbers.append(i)
            print(f"{i} is prime")

    print(", ".join(str(n) for n in prime_numbers))  # convert each to string

    # Save to results.txt
    with open("results.txt", "w") as f:
        f.write("\n".join(str(n) for n in prime_numbers))

    print("\nResults have been saved to results.txt")

