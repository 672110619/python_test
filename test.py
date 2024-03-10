# 获取用户输入的字符串
user_input = input("请输入一段字符串：")

# 去掉空格并用逗号分隔
result = user_input.replace("/", ",")

# 按照每个词一行输出
words = result.split(",")

# 将每个词分段赋值给变量
word1, word2, word3, word4= words[0], words[1], words[2], words[3]

# 显示结果
#print(f"空格的个数是：{space_count}")
print(f"第一个词是：{word1}")
print(f"第二个词是：{word2}")
print(f"第三个词是：{word3}")
print(f"第四个词是：{word4}")