# prime_number 
def prime_checker(number):
    is_prime = True

    # 从 2 开始期间只要有一个数被除等于 0 那就不是 prime
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

