def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

t = int(input())

for _ in range(t):
    num = int(input())
    
    half_num = num // 2
    
    if is_prime(half_num):
        print(half_num, half_num)
    else:
        start = half_num - 1 if half_num % 2 == 0 else half_num
        for i in range(start, 2, -2):
            if is_prime(i) and is_prime(num - i):
                print(i, num - i)
                break
