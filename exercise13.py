# 用命令行运行 python exercise13.py first 2nd 3rd
# 在vs code终端直接传入参数，无法直接运行，不用命令行这sb就不知道你穿了参数，很jb怪
# 想要运行传入参数的py文件得按f5呼出命令行，然后你写入到lanuch.json中的arg才有效，像个sb
# 所以我选择pycharm
from sys import argv

script, first, second, third = argv

# script直接就是目标位置不用再定义了
# 其他相当于三个变量 fir,sec,thi
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
