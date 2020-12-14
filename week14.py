names = ["廖挺均", "黃鑫凱", "郭星暘", "陳霆維","張宗棨","李世杰"]
dessert = ["冰淇淋", "貝果", "手搖杯", "白毫烏龍", "甜甜圈", "蛋糕"]
for i in range(len(names)):
    print("Hi,my name is",names[i],".My favorite dessert is",dessert[i])
    
start=int(input("請輸入加總開始值?"))
end=int(input("請輸入加總終止值?"))
step=int(input("請輸入遞增值?"))
sum=0
for i in range(start,end,step):
    sum=i*i
    print("i為",i,"時，累加結果為",sum)