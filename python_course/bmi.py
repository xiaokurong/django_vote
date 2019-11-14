weight,height=eval(input("请输入体重KG和身高米 :" ))
bmi = weight/pow(height,2)
print("BMI结果： {:.2f}".format(bmi))
print("国际指标 国内指标")
who,nat="",""
if bmi< 18.5 :
    who,nat="BMI 偏瘦","偏瘦"
elif 18.5<=bmi and bmi<24 :
    who,nat="BMI 正常","正常"
elif  24<=bmi<25 :
    who,nat="BMI 正常", "偏胖"
elif 25<bmi<28 :
    who,nat="BMI 偏胖",  "偏胖"
elif 28<=bmi<30:
    who,nat="BMI 偏胖", "肥胖"
elif bmi>=30:
    who,nat="BMI 肥胖", "肥胖"

print("最终结果：{},{}".format(who,nat))
