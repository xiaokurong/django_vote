#utf-8
temp = input("请输入需要转换的值 : " )
if temp[-1] in (['f','F']) :
    result = (eval(temp[:-1])-32)/1.8
    print("转换后的温度是 {:.2f}C".format(result))
elif temp[-1] in (['c','C']):
    result = (eval(temp[:-1])*1.8+32)
    print("转换后的温度是 {:.2f}F".format(result))
else:
    print("格式错误")
    

        
