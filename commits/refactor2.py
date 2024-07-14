def pixel(sym, times):
    '''接受两个参数，打印什么符号、打印多少次'''
    ans = sym * times
    print(ans, end="")


while True:
    try:
        n = int(input("height: "))
        # 限制用户输入在正整数1到8之间，包括1和8
        if 1 <= n <= 8:
            break
    except:
        pass
# 每行的操作
for row in range(n):
    # 计算需要的井号和空格的个数
    hashes = row + 1
    dots = n - hashes
    # 打印点
    pixel(" ", dots)
    # 打印井号
    pixel("#", hashes)
    # 打印中间点
    pixel(" ", 2)
    # 打印井号
    pixel("#", hashes)
    # 打印点
    pixel(" ", dots)
    # 打印换行符
    print()