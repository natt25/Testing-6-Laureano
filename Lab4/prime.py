import math

# verifica si es un primo positivo
def isPrime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for check in range(3, int(math.sqrt(number)) + 1, 2):
        if number % check == 0:
            return False
    return True

def isPrime2(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for check in range(3, int(math.sqrt(number)) + 1, 2):
        if number % check == 0:
            return False
    return True

def test():
    assert isPrime(1) == False
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(4) == False
    assert isPrime(5) == True
    assert isPrime(20) == False
    assert isPrime(21) == False
    assert isPrime(22) == False
    assert isPrime(23) == True
    assert isPrime(24) == False
    # You can add more tests here
    pass

def stats(lst):
    min_val = None
    max_val = None
    freq = {}
    for i in lst:
        if min_val is None or i < min_val:
            min_val = i
        if max_val is None or i > max_val:
            max_val = i
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    lst_sorted = sorted(lst)
    if len(lst_sorted) % 2 == 0:
        middle = len(lst_sorted) // 2
        median = (lst_sorted[middle] + lst_sorted[middle - 1]) / 2
    else:
        median = lst_sorted[len(lst_sorted) // 2]

    mode_times = None
    for i in freq.values():
        if mode_times is None or i > mode_times:
            mode_times = i
    mode = []
    for (num, count) in freq.items():
        if count == mode_times:
            mode.append(num)

    print("list = " + str(lst))
    print("min = " + str(min_val))
    print("max = " + str(max_val))
    print("median = " + str(median))
    print("mode(s) = " + str(mode))

def test_stats():
    stats([1, 2, 2, 3, 4, 4, 4, 5, 6])
    stats([10, 20, 20, 30, 40, 50, 50, 50, 60, 70])

test_stats()

def check(n):
    print("isPrime(" + str(n) + ") = " + str(isPrime(n)))

check(1)
check(2)
check(3)
check(4)
check(5)
check(20)
check(21)
check(22)
check(23)
check(24)
