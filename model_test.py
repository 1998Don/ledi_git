import jieba

with open('./file_danmu/test3.txt','r') as f:
    danmu = f.readlines()
danmu = [item.replace('\n','') for item in danmu]

car_class = []
with open('/Users/dingcong/ledi_git/file_danmu/奔驰筛别.txt','r') as f:
    dict_list = f.readlines()
if '-' in dict_list[0]:
    dict_list.pop(0)  #去掉注释
for item in dict_list:
    item = item.replace(' ','').replace('\n','')
    car_class.append(item.split(':'))
for i in range(len(car_class)):
    car_class[i][1] = car_class[i][1].strip().split(',')
car_class = dict(car_class)

car_class1 = []
with open('/Users/dingcong/ledi_git/file_danmu/奔驰.txt','r') as f:
    dict_list = f.readlines()
if '-' in dict_list[0]:
    dict_list.pop(0)  #去掉注释
for item in dict_list:
    item = item.replace(' ','').replace('\n','').upper()
    car_class1.append(item.split(':'))
car_class1 = dict(car_class1)
#弹幕处理--字符串
flag = 0
for item in danmu:
    item = item.strip().replace(' ','').replace('。','').replace('、','').replace('?','').upper()
    #一轮筛别
    for name in car_class:
        name_list = car_class.get(name)
        for name2 in name_list:
            if name2 in item:
                print(item + ' : ' + car_class1.get(name))
                flag = 1
                break
    if flag == 1:
        flag = 0
    else:
        print(item + ' : ' +"未识别")


