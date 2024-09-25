def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def gcd_of_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result

n = int(input("Enter the number of numbers: "))
numbers = []
for i in range(n):
    numbers.append(int(input("Enter number {}: ".format(i+1))))

result = gcd_of_list(numbers)
print("The GCD of the numbers is", result)