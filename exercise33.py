i = 0
numbers = []

while i < 6:
    print(f"At the top of the loop i is {i}")
    numbers.append(i)

    i += 1
    print("Numbers now: ", numbers)  # 可以直接打印数组内的全部内容
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
