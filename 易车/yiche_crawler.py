import json
import csv
import time
import requests
import execjs

class yiche:
  def __init__(self,):
    self.url = "https://car.yiche.com/web_api/car_model_api/api/v1/car/config_new_param?" \
              "cid=508&param="
    self.headers = {}
    self.url = ''
    self.count = 0

  def get_carId(self,brand):
    with open(f'/Users/dingcong/ledi_git/易车/{brand}carId.txt','r') as f:
      aodi_json = f.read()
    aodi_dict = eval(aodi_json)
    return aodi_dict

  def makejs(self,car_id):
    # 构建参数
    timestamp = str(time.time() * 1000).split('.')[0]
    param = '{\"cityId\":1501,' + '\"serialId":' + f'\"{car_id}\"' + '}'
    self.url = "https://car.yiche.com/web_api/car_model_api/api/v1/car/config_new_param?" \
          f"cid=508&param={param}"
    Y = "19DDD1FBDFF065D3A4DA777D2D7A81EC"
    t1 = "cid=" + str(508) + "&param=" + param + Y + timestamp  # 参数的拼接
    # 读取js文件
    with open('/Users/dingcong/ledi_git/易车/yiche.js', encoding='utf-8') as f:
      js = f.read()
    # 通过compile命令转成一个js对象
    docjs = execjs.compile(js)
    # JS执行结果
    res = docjs.call('yiche', t1)
    self.headers = {
        'x-platform': 'pc',
        'x-sign': res,
        'x-city-id': '1501',
        'x-timestamp': str(timestamp),

    }
  def get_car_info(self,brand):
      response = requests.request("GET", self.url, headers=self.headers)
      aodi6L_json = json.loads(response.text)
      # 获取配置列表
      table = aodi6L_json['data']
      # 提取车型配置参数
      # 存放最终配置列表
      peizhi_list = []
      for items in table:
          peizhi_list.append([items['name']])
          for item in items['items']:
              temp_list = [item['name']]
              for it in item['paramValues']:
                  one_str = ''
                  for i in it['subList']:
                      if i['desc'] == None:
                          one_str += i['value']
                      else:
                          one_str += i['value'] + i['desc']
                      if i['price'] != None:
                          one_str += i['price'] + '\n'
                      else:
                          one_str += '\n'
                  temp_list.append(one_str)
              peizhi_list.append(temp_list)
      with open(f'/Users/dingcong/ledi_git/易车/车型配置表/{brand}.csv', 'w', newline='', encoding='utf-8')as f:
          write = csv.writer(f)
          write.writerow([brand])
          for item in peizhi_list:
              write.writerow(item)
      print(f"{brand}参数配置整理完成")
      self.count += 1
  def exec_by_one(self,brand,cx):
      carId = yc.get_carId(brand)
      yc.makejs(carId[cx])
      yc.get_car_info(cx)

  def exec_by_brand(self,brand):
      carId = yc.get_carId(brand)
      for cx in carId:
          yc.makejs(carId[cx])
          yc.get_car_info(cx)
if __name__ == '__main__':
  yc = yiche()

  #得到品牌旗下所有车型数据
  yc.exec_by_brand("奥迪")

  # 得到品牌旗下某个车型数据
  # yc.exec_by_one("奥迪",'奥迪S6')

  print(f"全部车型整理完成,共更新车型数量: {yc.count}")





