def main():
    car_dict = []
    with open('/Users/dingcong/ledi_git/car_model/保时捷筛别.txt','r') as f:
        dict_list = f.readlines()
    if '-' in dict_list[0]:
        dict_list.pop(0)  #去掉注释
    for item in dict_list:
        item = item.replace(' ','').replace('\n','')
        car_dict.append(item.split(':'))
    for i in range(len(car_dict)):
        car_dict[i][1] = car_dict[i][1].upper()
    car = dict(car_dict)
    with open('/Users/dingcong/ledi_git/car_model/保时捷筛别.txt', 'w') as f:
        for key in car:
            f.write(key + ' : ' + car.get(key) + '\n')

main()