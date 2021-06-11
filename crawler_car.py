import json
import requests
import re
import html
from bs4 import BeautifulSoup
from lxml import etree
#将直播中弹幕与车型的字典存入txt中
# # def dict_write_txt(dict_):
# #     with open('宝马.txt','a+') as f:
# #         f.seek(0)
# #         if f.read():
# #             f.write("----------以下为追加内容----------\n")
# #         else:
# #             f.seek(2)
# #         for key in dict_:
# #             value = ','.join(dict_.get(key))
# #             f.write(key+' : '+value+'\n')
#将txt中弹幕与车型的字典读取出来
# def dict_read_txt():
#     car_dict = []
#     with open('/Users/dingcong/ledi_git/file_danmu/原匹配弹幕-车型.txt','r') as f:
#         dict_list = f.readlines()
#     if '-' in dict_list[0]:
#         dict_list.pop(0)  #去掉注释
#     for item in dict_list:
#         item = item.replace(' ','').replace('\n','')
#         car_dict.append(item.split(':'))
#     car_dict = dict(car_dict)
#     print(json.dumps(car_dict,ensure_ascii=False,indent=1))   #格式化输出--json
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
    #法拉利
    def web_ferrari(self):
        url = 'https://www.ferrari.com/zh-CN/auto/car-range'
        r = requests.get(url).content.decode()
        tree = etree.HTML(r)
        content = tree.xpath('//span[@class="BtnAction__text__2vvCUxFa"]/text()')
        result = set(filter(lambda x : x != '打造您的专属座驾' and x != '咨询详情' and x !='订阅法拉利电子通讯',content))
        result = [i.replace('探索法拉利','').replace('探索','').replace('DISCOVER THE FERRARI','').strip() for i in result]
        with open('./车型/法拉利车型.txt', 'w') as f:
            # f.write(f"\n-----本次奥迪更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"法拉利车型更新成功！共更新{len(result)}种车型")
    #长安
    def web_changan(self):
        url = 'https://www.changan.com.cn/'
        '''
            a = $x('//h6[@dd]/text()');
            var arr = [];
            for(var i =0;i<a.length;i++){
                arr.push(a[i].data);
            };
            copy(arr)
        '''
    #吉利
    def web_jili(self):
        url = 'https://www.geely.com/'
        header = {
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        r = requests.get(url,headers=header).content.decode()
        tree = etree.HTML(r)
        result = set(tree.xpath('//p[@style="cursor:text"]/text()'))
        with open('./车型/吉利车型.txt', 'w') as f:
            # f.write(f"\n-----本次吉利更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"吉利车型更新成功！共更新{len(result)}种车型")
    #长城
    def web_changcheng(self):
        url = 'https://www.gwm.com.cn/'
        header = {
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        r = requests.get(url,headers=header).content.decode()
        tree = etree.HTML(r)
        result = set(tree.xpath('//a//@data-title'))
        result = set(filter(lambda x : len(x) < 12,result)) #通过车型长度筛掉无用信息
        with open('./车型/长城车型.txt', 'w') as f:
            # f.write(f"\n-----本次长城更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"长城车型更新成功！共更新{len(result)}种车型")
    #比亚迪
    def web_byd(self):
        url = 'http://www.bydauto.com.cn/sites/REST/resources/v1/search/sites/BYD_AUTO/types/BydModelView/assets?fields=name,id,createdby,updatedby,ImmediateParents,isShowHeader,wetherListed,title,carSort,title1,descBefore,desc,desc1,desc2Before,desc2,desc3,desc4,image,testDrive,image1,powerType,tiBefore,tiPrice,tiAfter&field:subtype:equals=MotorDetails&orderBy=carSort:desc'
        header = {
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        car_class = json.loads(requests.get(url,headers=header).content.decode())['items']
        result = []
        for car in car_class:
            result.append(car['title'])
        result = set(result)
        with open('./车型/比亚迪车型.txt', 'w') as f:
            # f.write(f"\n-----本次比亚迪更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"比亚迪车型更新成功！共更新{len(result)}种车型")
    #上汽通用
    def web_sqty(self):
        url_cadillac = 'https://www.cadillac.com.cn/'
        url_xfl = 'https://www.chevrolet.com.cn/'
        url_bk = 'https://www.buick.com.cn/'
        header = {
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        r1 = requests.get(url_cadillac,headers=header).content.decode() #凯迪拉克
        tree1 = etree.HTML(r1)
        result = set(tree1.xpath('//div[@class="headLayout"]//p/text()'))
        r2 = requests.get(url_xfl, headers=header).content.decode() #雪弗兰
        tree2 = etree.HTML(r2)
        result |= set(tree2.xpath('//div[@class="all"]//p/span[1]/text()'))
        r3 = requests.get(url_bk, headers=header).content.decode()  #别克
        tree3 = etree.HTML(r3)
        result |= set(tree3.xpath('//ul[@class="pt-dual"]//a/text()'))
        with open('./车型/上汽通用车型.txt', 'w') as f:
            # f.write(f"\n-----本次上汽通用更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"上汽通用车型更新成功！共更新{len(result)}种车型")

    #一汽丰田
    def web_yqft(self):
        url = 'https://www.ftms.com.cn/website/Car/brandModels'
        header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        car_class = json.loads(requests.get(url, headers=header).content.decode())['data']
        result = []
        for car in car_class:
            if car['car_series'] != []:
                for item in car['car_series']:
                        result.append(item['name'])
        result = set(result)
        with open('./车型/一汽丰田车型.txt', 'w') as f:
            # f.write(f"\n-----本次一汽丰田更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"一汽丰田车型更新成功！共更新{len(result)}种车型")

    # 奇瑞
    def web_qr(self):
        url = 'https://www.chery.cn/'
        header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        r = requests.get(url, headers=header).content.decode()
        tree = etree.HTML(r)
        result = set(tree.xpath('//ul[@class="clearfix"]/li[position()<3]/p[position()>1]/a/text()'))
        with open('./车型/奇瑞车型.txt', 'w') as f:
            # f.write(f"\n-----本次奇瑞更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"奇瑞车型更新成功！共更新{len(result)}种车型")

    # 广汽丰田
    def web_gqft(self):
        url = 'https://www.gac-toyota.com.cn/'
        header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        r = requests.get(url, headers=header).content.decode()
        tree = etree.HTML(r)
        result = set(tree.xpath('//ul[@class="clearfix car-ul font16"]/li/a/text()'))
        with open('./车型/广汽丰田车型.txt', 'w') as f:
            # f.write(f"\n-----本次广汽丰田更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"广汽丰田车型更新成功！共更新{len(result)}种车型")

    # 广汽本田
    def web_gqbt(self):
        url = 'https://www.ghac.cn/'
        header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        r = requests.get(url, headers=header).content.decode()
        tree = etree.HTML(r)
        result = set(tree.xpath('//div[@class="left"]/dl[1]/dd/a[@data-action="click"]/text()'))
        with open('./车型/广汽本田车型.txt', 'w') as f:
            # f.write(f"\n-----本次广汽丰田更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"广汽本田车型更新成功！共更新{len(result)}种车型")

    # 广汽本田
    def web_gqbt(self):
        url = 'https://www.ghac.cn/'
        header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        r = requests.get(url, headers=header).content.decode()
        tree = etree.HTML(r)
        result = set(tree.xpath('//div[@class="left"]/dl[1]/dd/a[@data-action="click"]/text()'))
        with open('./车型/广汽本田车型.txt', 'w') as f:
            # f.write(f"\n-----本次广汽丰田更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"广汽本田车型更新成功！共更新{len(result)}种车型")

    # 北京现代
    def web_bjxd(self):
        url = 'https://www.beijing-hyundai.com.cn/'
        header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        r = requests.get(url, headers=header).content.decode()
        tree = etree.HTML(r)
        result = set(tree.xpath('(//div[@class="swiper-wrapper"])[10]//a/p/text()'))
        with open('./车型/北京现代车型.txt', 'w') as f:
            # f.write(f"\n-----本次北京现代更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"北京现代车型更新成功！共更新{len(result)}种车型")

    # 特斯拉
    def web_bjxd(self):
        url = 'https://www.tesla.cn/api/tesla/header/html/v0'
        header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        r = requests.get(url, headers=header).content.decode()
        tree = etree.HTML(r)
        result = set(tree.xpath('(//ol[@data-region="legacy_menu_support"])[1]/li[position()<6]/a/text()'))
        with open('./车型/特斯拉车型.txt', 'w') as f:
            # f.write(f"\n-----本次特斯拉更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"特斯拉车型更新成功！共更新{len(result)}种车型")

    # 蔚来
    def web_weilai(self):
        url = 'https://ir.nio.com/'
        header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        r = requests.get(url, headers=header).content.decode()
        tree = etree.HTML(r)
        result = set(tree.xpath('(//ul[@class="menu clearfix menu--level-1"])[1]/li/a/text()'))
        with open('./车型/蔚来车型.txt', 'w') as f:
            # f.write(f"\n-----本次蔚来更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"蔚来车型更新成功！共更新{len(result)}种车型")

    # 小鹏
    def web_xiaop(self):
        url = 'https://www.xiaopeng.com/'
        header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        r = requests.get(url, headers=header).content.decode()
        tree = etree.HTML(r)
        result = set(tree.xpath('(//ul[@class="list"])[1]/li[1]/div/ul/li/a/text()'))
        with open('./车型/小鹏车型.txt', 'w') as f:
            # f.write(f"\n-----本次小鹏更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"小鹏车型更新成功！共更新{len(result)}种车型")

    # 理想
    def web_lx(self):
        url = 'https://www.lixiang.com/'
        header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        r = requests.get(url, headers=header).content.decode()
        tree = etree.HTML(r)
        result = set(tree.xpath('//ul[@class="chj-header-link-panel"]/li[1]/a/text()'))
        with open('./车型/理想车型.txt', 'w') as f:
            # f.write(f"\n-----本次理想更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"理想车型更新成功！共更新{len(result)}种车型")
    # 捷豹
    def web_jb(self):
        url = 'https://www.jaguar.com.cn/jaguar-range/index.html'
        header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        r = requests.get(url, headers=header).content.decode()
        tree = etree.HTML(r)
        result = set(tree.xpath('//div[@class="FooterNav__footerWrapper fontSmooth "]/div[@class="FooterNav__navWrapper el"][1]/ul/li[position()<8]/a/text()'))
        with open('./车型/捷豹车型.txt', 'w') as f:
            # f.write(f"\n-----本次捷豹更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"捷豹车型更新成功！共更新{len(result)}种车型")
    # 凯迪拉克
    def web_cadillac(self):
        url_cadillac = 'https://www.cadillac.com.cn/'
        header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        r= requests.get(url_cadillac,headers=header).content.decode() #凯迪拉克
        tree = etree.HTML(r)
        result = set(tree.xpath('//div[@class="headLayout"]//p/text()'))
        with open('./车型/凯迪拉克车型.txt', 'w') as f:
            # f.write(f"\n-----本次凯迪拉克更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"凯迪拉克车型更新成功！共更新{len(result)}种车型")

    # 英菲尼迪
    def web_infiniti(self):
        url = 'https://www.infiniti.com.cn/vehicles/shop-infiniti-now.html'
        header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        r = requests.get(url, headers=header).content.decode()
        tree = etree.HTML(r)
        result = set(tree.xpath(
            '//ul[@class="list-item"]/li/div/div/div/h3/a/text()'))
        with open('./车型/英菲尼迪车型.txt', 'w') as f:
            # f.write(f"\n-----本次英菲尼迪更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"英菲尼迪车型更新成功！共更新{len(result)}种车型")
    # 林肯
    def web_infiniti(self):
        url = 'https://www.lincoln.com.cn/'
        header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        r = requests.get(url, headers=header).content.decode()
        tree = etree.HTML(r)
        result = set(tree.xpath(
            '(//div[@class="col-sm-3 footer-list"])[1]/div[@class="content-accordion"]/p/a/text()'))
        with open('./车型/林肯车型.txt', 'w') as f:
            # f.write(f"\n-----本次林肯更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"林肯车型更新成功！共更新{len(result)}种车型")
    # 玛莎拉蒂
    def web_infiniti(self):
        url = 'https://www.maserati.com/cn/zh'
        header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        r = requests.get(url, headers=header).content.decode()
        tree = etree.HTML(r)
        result = set(tree.xpath(
            '(//ul[@class="footer-element footer-element-column footer-line-links"])[1]/li/a/text()'))
        with open('./车型/玛莎拉蒂车型.txt', 'w') as f:
            # f.write(f"\n-----本次玛莎拉蒂更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"玛莎拉蒂车型更新成功！共更新{len(result)}种车型")
    # 迈凯伦
    def web_mclarencars(self):
        url = 'https://www.mclarencars.cn/'
        header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }
        r = requests.get(url, headers=header).content.decode()
        tree = etree.HTML(r)
        result = set(tree.xpath(
            '//div[@class="model-category-wrapper"]/div/div/div/div/div/span/text()'))
        with open('./车型/迈凯伦车型.txt', 'w') as f:
            # f.write(f"\n-----本次迈凯伦更新车型共{len(result)}种-----\n\n")
            for item in result:
                f.write(item + '\n')
        print(f"迈凯伦车型更新成功！共更新{len(result)}种车型")
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