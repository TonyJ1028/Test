# Calculator
method = ""

while method != "exit":
    # 提示用户选择运算类型
    method = input("Which calculation do you want to do? (plus, minus, multiply, division, or type 'exit' to quit): ")

    # 检查是否输入了有效的运算方法
    if method in ["plus", "minus", "multiply", "division"]:
        while True:  # 嵌套循环，重复执行当前运算
            # 让用户输入两个数字
            a = float(input("Please insert the first number: "))
            b = float(input("Please insert the second number: "))

            # 根据用户选择的运算方法进行计算
            if method == "plus":
                result = a + b
            elif method == "minus":
                result = a - b
            elif method == "multiply":
                result = a * b
            elif method == "division":
                if b != 0:
                    result = a / b
                else:
                    print("Division by 0 is not allowed!")
                    continue  # 跳过这次循环，重新提示输入

            # 输出计算结果
            print("The result is: %.4f" % result)

            # 提示用户是否继续当前运算
            repeat = input("Do you want to perform another '%s' operation? (yes to continue, no to return to main menu): " % method)
            if repeat.lower() != "yes":
                break  # 如果用户选择不继续，退出当前运算，返回主菜单

    elif method == "exit":
        print("Goodbye!")
    else:
        print("Invalid input! Please enter 'plus', 'minus', 'multiply', 'division', or 'exit'.")
