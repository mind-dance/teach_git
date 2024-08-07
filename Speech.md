版本控制系统 (VCS) 是用于跟踪源代码（或其他文件和文件夹集合）更改的工具。顾名思义，这些工具有助于维护更改历史记录；此外，它们还有助于协作。VCS 通过一系列快照跟踪文件夹及其内容的更改，其中每个快照都封装了顶级目录中文件/文件夹的完整状态。VCS 还维护元数据，例如每个快照的创建者、与每个快照相关的消息等。

为什么版本控制很有用？即使您独自工作，它也可以让您查看项目的旧快照、记录进行某些更改的原因、处理并行开发的分支等等。与他人合作时，它是查看其他人所做的更改以及解决并行开发中的冲突的宝贵工具。

现代 VCS 还可以让您轻松（通常是自动）回答以下问题：

- 谁编写了这个模块？
- 此特定文件的此特定行何时被编辑？由谁编辑？为何编辑？
- 在过去的 1000 次修订中，某个单元测试何时/为何停止工作？

由于 Git 的界面是一种漏洞百出的抽象，自上而下地学习 Git（从其界面/命令行界面开始）可能会导致很多混乱。可以记住一些命令并将它们视为魔法咒语，并在出现任何问题时按照上面漫画中的方法进行操作。

尽管 Git 的界面确实丑陋，但其底层设计和理念却非常优美。丑陋的界面需要记住*，*而优美的设计则可以*理解*。因此，我们从下而上对 Git 进行了解释，从其数据模型开始，然后介绍命令行界面。一旦理解了数据模型，就可以更好地理解命令如何操作底层数据模型。

工作目录

暂存区

提交

快照

仓库

历史

# 基础
1. 第一提交

    ```
    init, status, add, commit
    ```

    

    - 初始化仓库`init`

    - 查看目前状态`status`

    - 新建一个文件

      ```python
      # qmark
      print("????")
      ```

      

    - 查看状态

    - `add`当前文件，但不提交

      ```python
      # qmark
      for i in range(4):
          print("?", end="")
      print()
      ```

      查看状态

    每次add添加的是目前的状态

    - 第一次提交，msg随便写

2. 查看历史

    ```
    log diff checkout help
    ```

    打开编辑器进行信息的编辑

    ```python
    # qmark
    def qmark():
        for i in range(4):
            print("?", end="")
        print()
    
        
    # wall
    for i in range(3):
        print("#")
    ```

    - 查看历史
    - `help`提交，查看-m参数
    - 提交
    - 对比前一个文件`diff`
    - 切换到前一个文件`checkout`

3. 撤销更改

    ```
    --amend restore checkout
    ```

- 上部分设置为`wall`函数

  ```python
  # wall
  def wall():
      for i in range(3):
          print("#")
  
  
  # block
  for row in range(3):
      for col in range(3):
          print("#",end="")
      print()
  ```

- 提交，随后切换版本

4. 分支

   创建分支

   triangle函数。立即合并

   ```python
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
   ```

   

   bugFix等待合并。

5. 切换至github

创建仓库，公开。

本地文件推送到远程。



用github编辑器完成

- issue，非法输入#2 branch合并 ；
- PR:输出有误，`.`换space

- issue，希望双门 #1 演示

- issue，代码太辣鸡，要重构 #3

```python
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
```

提交带上双开门#2
