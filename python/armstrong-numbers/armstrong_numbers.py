def is_armstrong_number(n):
    n1 = n%10
    n2 = n%100//10
    n3 = n%1000//100
    n4 = n%10000//1000
    n5 = n%100000//10000
    n6 = n%1000000//100000
    n7 = n%10000000//1000000
    c = bool(n1) + bool(n2) + bool(n3) + bool(n4) + bool(n5) + bool(n6) + bool(n7)
    if c == 0:
        return True
    return n1**c + n2**c + n3**c + n4**c + n5**c + n6**c + n7**c == n
