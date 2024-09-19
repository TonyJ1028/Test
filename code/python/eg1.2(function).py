#TempConvert1.1.py
def tempConvert(val):                 #定义 有关变量val的函数tempconvert
    if val[-1] in ['C', 'c']:         #翻译：如果 变量val的最后一位 是 C或c
        f = 1.8 * float(val[0:-1]) + 32  
        print("转换后的温度为：%.2fF"%f) #摄氏转华氏并输出
    elif val[-1] in ["F", "f"]:       #翻译：反之如果 变量val的最后一位 是 F或f
        c = (float(val[0:-1]) - 32) / 1.8
        print("转换后的温度为：%.2fC"%c) #华氏转摄氏输出
    else:                             #翻译：否则
        print("输入有误")
val = input("请输入带温度表示符号的温度值,输入n退出(例如:32C)")
while val[-1] not in ['N', 'n']:
    tempConvert(val)                  #对变量var调用函数tempconvert
    val = input("请输入带温度表示符号的温度值,输入n退出(例如:32C)")