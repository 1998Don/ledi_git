


brand = input("请输入需要整理的车型：")
car_key = []
with open('/Users/dingcong/ledi_git/car_model/' +brand +'.txt', 'r') as f:
    dict_list = f.readlines()
if '-' in dict_list[0]:
    dict_list.pop(0)  # 去掉注释
for item in dict_list:
    item = item.replace(' ' ,'').replace('\n' ,'').upper()
    car_key.append(item.split(':')[1])

car_value = []
with open('/Users/dingcong/ledi_git/car_model/' +brand +'筛别.txt', 'r') as f:
    dict_list = f.readlines()
if '-' in dict_list[0]:
    dict_list.pop(0)  # 去掉注释
for item in dict_list:
    item = item.replace(' ' ,'').replace('\n' ,'').upper()
    car_value.append(item.split(':')[1])

car = dict(zip(car_key,car_value))
with open(f'/Users/dingcong/ledi_git/车型黑话参考版/{brand}.txt', 'w') as f:
    for key in car:
        f.write(key + ' : ' + car.get(key) + '\n')
print(f"{brand}车型整理完成！")
