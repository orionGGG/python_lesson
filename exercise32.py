the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']  # apricots杏子
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:  # for循环开始时就自动定义了变量
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []
'''创建空列表'''

# then use the range function to do 0 to 5 counts
for i in range(0, 6):  # 相当于 for( int i=0; i<6; i++)
    '''range()函数会从第一个数到最后一个数，但不包含最后一个数'''

    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)
    '''append()作用是在列表尾部追加元素'''

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")