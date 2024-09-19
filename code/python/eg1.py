#TempConvert.py
val = input("请输入带温度表示符号的温度值(例如:32C)") #变量val 赋予定义 输入内容
if val[-1] in ['C', 'c']:                        #如果 变量val最后一位 是 C或c
    f = 1.8 * float(val[0:-1]) + 32              
    print("转换后的温度为：%.2fF"%f)                #摄氏转华氏并输出
elif val[-1] in ["F", "f"]:                      #反之如果 变量val的最后一位 是 C或c
    c = (float(val[0:-1]) - 32) / 1.8
    print("转换后的温度为：%.2fC"%c)                #华氏转摄氏输出
else:                                            #否则
    print("输入有误")
