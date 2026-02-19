def superDigit(n, k):
    initial_sum = sum(int(digit) for digit in n) * k
    
    def find_super_digit(x):
        if x < 10:
            return x
        return find_super_digit(sum(int(d) for d in str(x)))
    
    return find_super_digit(initial_sum)
