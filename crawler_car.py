import json
import requests
import re
import html
from bs4 import BeautifulSoup
#将直播中弹幕与车型的字典存入txt中
# def dict_write_txt(dict_):
#     with open('宝马.txt','a+') as f:
#         f.seek(0)
#         if f.read():
#             f.write("----------以下为追加内容----------\n")
#         else:
#             f.seek(2)
#         for key in dict_:
#             value = ','.join(dict_.get(key))
#             f.write(key+' : '+value+'\n')
class crawler_car:
    def web_bmw(self):
        url = 'https://www.bmw.com.cn/content/dam/bmw/marketCN/bmw_com_cn/model-finder/index.html'
        r = requests.get(url).content.decode()
        regx = r'data-car-model-name="(.*)">'
        result = set(re.findall(regx,r))
        with open('./车型/宝马车型.txt','w') as f:
            # f.write(f"\n-----本次宝马更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item+'\n')
        print(f"宝马车型更新成功！共更新{len(result)}种车型")

    def web_benchi(self):
        url = 'https://www.mercedes-benz.com.cn/bin/mbcn/getvehicleModelData.oneweb.json'
        r = json.loads(requests.get(url).content.decode())
        car_list = r['bodStyle']
        with open('./车型/奔驰车型.txt','w') as f:
            for item in car_list:      #每一个item为一个车型字典
                if item['bodyStyleChineseName']:
                    # f.write(f"--------以下车型中文名为: {item['bodyStyleChineseName']}, 英文名为: {item['bodyStyleName']}--------\n")
                    for car_class in item['class']:
                        for car_modal in car_class['modal']:
                            f.write(car_modal['modalChineseName']+'\n')
        with open('./车型/奔驰车型.txt','r') as f:
            len_ = f.readlines()
        print(f"奔驰车型更新成功！共更新{len(len_)}种车型")

    def web_yiqidazhong(self):
        url = 'https://vw.faw-vw.com/models/'
        r = requests.get(url).content.decode()
        regx = r'<img alt="(.*)" title'
        result = set(re.findall(regx, r))
        with open('./车型/一汽大众车型.txt', 'w') as f:
            # f.write(f"\n-----本次一汽大众更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"一汽大众车型更新成功！共更新{len(result)}种车型")

    def web_dongfeng(self):
        car_l = []
        url = 'https://www.dongfeng-honda.com/'
        r = requests.get(url).content.decode()
        soup = BeautifulSoup(r,'lxml')
        car_list = soup.find(name='section',attrs={'class':'sitemap'})
        car_list = car_list.find(name='ul').find(name='ul')
        for car in car_list:
            car_l.append(str(car.string))
        car_l = list(set(car_l))
        car_l.remove('\n')
        for item in car_l:
            if '<' in item:
                car_l.remove(item)
        with open('./车型/东风本田车型.txt', 'w') as f:
            # f.write(f"\n-----本次东风本田更新车型共{len(car_l)}种-----\n\n")
            for item in car_l:
                f.write(item + '\n')
        print(f"东风本田车型更新成功！共更新{len(car_l)}种车型")

    def web_shangqidazhong(self):
        url = 'https://www.svw-volkswagen.com/model/'
        r = requests.get(url).content.decode()
        regx = r'<div class="carname" data-v-7f36f923>(.*?)</div>'
        result = set(re.findall(regx, r))
        with open('./车型/上汽大众车型.txt', 'w') as f:
            # f.write(f"\n-----本次上汽大众更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"上汽大众车型更新成功！共更新{len(result)}种车型")

    def web_baoshijie(self):
        car_list = []
        url = 'https://www.porsche.cn/china/zh/models/'
        r = requests.get(url).content.decode()
        r = html.unescape(r)
        regx = r'<div class="m-14-model-name">(.*?)</div>'
        result = set(re.findall(regx, r))
        for item in result:
            item = item.replace(' ','').replace("<nobr>",'').replace("</nobr>",'')
            car_list.append(item)
        with open('./车型/保时捷车型.txt', 'w') as f:
            # f.write(f"\n-----本次保时捷更新车型共{len(car_list)}种-----\n\n")
            for item in car_list:
                f.write(item + '\n')
        print(f"保时捷车型更新成功！共更新{len(car_list)}种车型")

    def web_lkss(self):
        url = 'http://www.lexus.com.cn/models/overview'
        r = requests.get(url).content.decode()
        regx = r'<strong class="lh-700">(.*?)</strong>'
        result = set(re.findall(regx, r))
        result.discard('金融服务')
        result.discard('车型筛选')
        result.discard('YACHT')
        with open('./车型/雷克萨斯车型.txt', 'w') as f:
            # f.write(f"\n-----本次雷克萨斯更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"雷克萨斯车型更新成功！共更新{len(result)}种车型")

    def web_volvo(self):
        url = 'https://www.volvocars.com/zh-cn/cars/%E8%BD%A6%E5%9E%8B%E6%A6%82%E8%A7%88'
        r = requests.get(url).content.decode()
        regx = r'<h5 class="h5">(.*?)</h5>'
        result = set(re.findall(regx, r))
        with open('./车型/沃尔沃车型.txt', 'w') as f:
            # f.write(f"\n-----本次沃尔沃更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"沃尔沃车型更新成功！共更新{len(result)}种车型")
    def web_aodi(self):
        url = 'https://www.audi.cn/cn/web/zh/models.html'
        r = requests.get(url).content.decode()
        regx = r'<span class="audi-copy-m audi-modelfinder__car-model-body-type">(.*?)</span>'
        result = set(re.findall(regx, r))
        with open('./车型/奥迪车型.txt', 'w') as f:
            # f.write(f"\n-----本次奥迪更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"奥迪车型更新成功！共更新{len(result)}种车型")
if __name__ == '__main__':
    print('''
----本系统用于更新以下品牌车型数据，更新后的文件存于本文件同级的车型文件夹中----
请输入指定指令更新指定品牌数据：
1、奥迪 2、宝马 3、奔驰 4、沃尔沃 5、雷克萨斯 6、保时捷 7、东风本田 8、上汽大众 9、一汽大众
0、退出
    ''')
    car = crawler_car()
    while True:
        flag = eval(input("请输入需要更新的车型指令："))
        if flag == 1:
            car.web_aodi()
        elif flag == 2:
            car.web_bmw()
        elif flag == 3:
            car.web_benchi()
        elif flag == 4:
            car.web_volvo()
        elif flag == 5:
            car.web_lkss()
        elif flag == 6:
            car.web_baoshijie()
        elif flag == 7:
            car.web_dongfeng()
        elif flag == 8:
            car.web_shangqidazhong()
        elif flag == 9:
            car.web_yiqidazhong()
        elif flag == 0:
            break
