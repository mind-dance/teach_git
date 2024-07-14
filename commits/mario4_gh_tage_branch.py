# qmark
def qmark():
    for i in range(4):
        print("?", end="")
    print()


# wall
def wall():
    for i in range(3):
        print("#")


# block
def block():
    for row in range(3):
        for col in range(3):
            print("#",end="")
        print()


n = int(input("height: "))
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
    # 打印换行符
    print()
