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
for row in range(3):
    for col in range(3):
        print("#",end="")
    print()