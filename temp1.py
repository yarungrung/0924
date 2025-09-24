import math
def calculate_circle_area(radius):
    return math.pi * radius ** 2
print(calculate_circle_area(5))


# 寫一個函式，接收一個數字列表，回傳列表中的最大值
def find_maximum(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
print(find_maximum([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  # Output: 9


#寫一個程式從1印到100
for i in range(1, 101):
    print(i)
#如果數字是3的倍數，印出"Fizz"
#如果數字是5的倍數，印出"Buzz"
#如果數字同時是3和5的倍數，印出"FizzBuzz"
#否則印出數字本身
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)