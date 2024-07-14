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


# triangle
def tag(n):
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


# double triangle        
def dtag(n):
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


n = int(input("height: "))
dtag(n)