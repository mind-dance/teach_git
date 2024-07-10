while True:
    n = int(input("height: "))
    # 限制用户输入在正整数1到8之间，包括1和8
    if 1 <= n <= 8:
        break
# 每行的操作
for row in range(n):
    # 计算需要的井号和空格的个数
    hashes = row + 1
    dots = n - hashes
    # 打印点
    for dot in range(dots):
        print(".", end="")
    # 打印井号
    for hashe in range(hashes):
        print("#", end="")
    # 打印中间点
    print("..", end="")
    # 打印井号
    for hashe in range(hashes):
        print("#", end="")
    # 打印点
    for dot in range(dots):
        print(".", end="")
    # 打印换行符
    print()


print("我是点点！我要PR！654321"）
