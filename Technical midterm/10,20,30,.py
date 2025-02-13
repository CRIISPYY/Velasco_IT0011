def is_palindrome(num):
    return str(num) == str(num)[::-1]

def process_line(line):
    numbers = list(map(int, line.strip().split(',')))

    total_sum = sum(numbers)
    
    if is_palindrome(total_sum):
        return f"({','.join(map(str, numbers))}) (sum {total_sum}) - Palindrome"
    else:
        return f"({','.join(map(str, numbers))}) (sum {total_sum}) - Not a palindrome"

def check_palindromes_in_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        for idx, line in enumerate(lines, start=1):
            result = process_line(line)
            print(f"Line {idx}: {result}")
filename = 'numbers.txt'
check_palindromes_in_file(filename)