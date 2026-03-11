def sum_of_digits(n: int) -> int:
    total = 0
    
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
        
    return total


if __name__ == "_main_":
    n = int(input())
    print(sum_of_digits(n))