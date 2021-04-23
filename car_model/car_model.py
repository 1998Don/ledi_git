import jieba
import os
class car_class:
    def __init__(self,brand):
        self.brand = brand
    # 读取对应汽车品牌的类型
    def read_car_class(self):
        car_class = []
        with open('./car_model/'+self.brand+'.txt', 'r') as f:
            dict_list = f.readlines()
        if '-' in dict_list[0]:
            dict_list.pop(0)  #去掉注释
        for item in dict_list:
            item = item.replace(' ','').replace('\n','')
            car_class.append(item.split(':'))
        return dict(car_class)
    # 读取对应汽车品牌的类型的别名
    def read_car_class_key(self):
        car_class_key = []
        with open('./car_model/'+self.brand+'筛别.txt', 'r') as f:
            dict_list = f.readlines()
        if '-' in dict_list[0]:
            dict_list.pop(0)  #去掉注释
        for item in dict_list:
            item = item.replace(' ','').replace('\n','')
            car_class_key.append(item.split(':'))
        for i in range(len(car_class_key)):
            car_class_key[i][1] = car_class_key[i][1].strip().split(',')
        return dict(car_class_key)
    def read_danmu(self):
        with open('./file_danmu/test1.txt', 'r') as f:
            danmu = f.readlines()
        danmu = [item.replace('\n','') for item in danmu]
        return danmu
    def danmu_recognition(self,car_class,car_class_key,danmu):
        print(danmu)
        #弹幕处理--字符串
        flag = 0
        for item in danmu:
            item = item.strip().replace(' ','').replace('。','').replace('、','').replace('?','').upper()
            #一轮筛别
            for name in car_class_key:
                name_list = car_class_key.get(name)
                for name2 in name_list:
                    if name2 in item and flag == 0:
                        print(item + ' : ' + car_class.get(name))
                        flag = 1
                        break
            if flag == 1:
                flag = 0
            else:
                print(item + ' : ' +"未识别")

if __name__ == '__main__':
    print("当前文件路径为: "+os.getcwd())
    brand = input("请输入要识别的弹幕所属品牌：")
    if brand in ['奔驰','benchi']:
        brand = '奔驰'
    elif brand in ['宝马','baoma']:
        brand = '宝马'
    elif brand in ['奥迪','aodi']:
        brand = '奥迪'
    elif brand in ['一汽大众','dazhong','dz']:
        brand = '一汽大众'
    elif brand in ['雷克萨斯','leikesasi','lkss']:
        brand = '雷克萨斯'
    elif brand in ['保时捷','baoshijie','bsj']:
        brand = '保时捷'
    model = car_class(brand)    #创建模型实例
    car_class = model.read_car_class()  #获取该品牌车型信息
    car_class_key= model.read_car_class_key()   #获取该品牌车型别名
    danmu = model.read_danmu()
    model.danmu_recognition(car_class,car_class_key,danmu)



