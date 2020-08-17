from sys import argv#从sys中调入argv函数

scrpit, filename = argv#script为目标位置，将argv中的参数用变量filename表示
txt = open(filename)#创建内容与filename一样的文件对象

print(f"Here's your file {filename}")#将文件
print(txt.read())#读取txt文件对象，并打印其内容

print("Type the filename again:")#提示再次输入
file_again = input(">")  #输入要读取的文件并储存为file_again,""内是注释

txt_again = open(file_again)#同txt

print(txt_again.read())#打印txt的文件内容