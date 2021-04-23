import pymysql
import time
import json
#得到不能识别的弹幕数据，返回类型：列表+字符串
def get_bad_comment(brand):
    # 将txt中弹幕与车型的字典读取出来
    car_dict = []
    with open('/Users/dingcong/ledi_git/file_danmu/品牌-直播间.txt', 'r') as f:
        dict_list = f.readlines()
    if '-' in dict_list[0]:
        dict_list.pop(0)  # 去掉注释
    for item in dict_list:
        item = item.replace(' ', '').replace('\n', '')
        car_dict.append(item.split(':'))
    for i in range(len(car_dict)):
        car_dict[i][1] = map(int, car_dict[i][1].strip().split(','))  # 返回的是迭代器
    car_dict = dict(car_dict)
    room_list = car_dict[brand]
    conn = pymysql.connect(
        host='8.136.102.203',
        port=6001,
        user='dingcong',
        password='wdnCLPiSnh6AwUTm',
        db='dy_live',
        charset='utf8'
    )
    cur = conn.cursor()
    content = []
    # 获取所有type为1的对应品牌的弹幕
    for room in room_list:
        sql1 = f'select content from danmu where type={1} and auto_type is null and lid={room}'  #查找原模型不能判断的弹幕
        cur.execute(sql1)
        content.extend([n[0] for n in cur.fetchall()])
    cur.close()
    conn.close()
    return content

#得到已经识别的车型数据并去重，返回类型：集合+字符串
def get_car_hastype():
    conn = pymysql.connect(
        host='8.136.102.203',
        port=6001,
        user='dingcong',
        password='wdnCLPiSnh6AwUTm',
        db='dy_live',
        charset='utf8'
    )
    cur = conn.cursor()
    # 获取所有type为1的原匹配车型
    sql1 = f'select auto_type from danmu where type={1} and auto_type is not null'
    cur.execute(sql1)
    content = set([n[0] for n in cur.fetchall])
    content.discard('')
    cur.close()
    conn.close()
    return content

#获取对应车型的识别弹幕
def get_car_dict(brand):
    # 将txt中弹幕与车型的字典读取出来
    car_dict = []
    with open('/Users/dingcong/ledi_git/file_danmu/品牌-直播间.txt','r') as f:
        dict_list = f.readlines()
    if '-' in dict_list[0]:
        dict_list.pop(0)  #去掉注释
    for item in dict_list:
        item = item.replace(' ','').replace('\n','')
        car_dict.append(item.split(':'))
    for i in range(len(car_dict)):
        car_dict[i][1] = map(int,car_dict[i][1].strip().split(','))   #返回的是迭代器
    car_dict = dict(car_dict)
    room_list = car_dict[brand]
    conn = pymysql.connect(
        host='8.136.102.203',
        port=6001,
        user='dingcong',
        password='wdnCLPiSnh6AwUTm',
        db='dy_live',
        charset='utf8'
    )
    cur = conn.cursor()
    # 获取所有type为1的对应品牌原匹配车型
    content = []
    for room in room_list:
        sql1 = f'select content,auto_type from danmu where type={1} and auto_type is not null and lid={room}'
        cur.execute(sql1)
        content.extend([(n[0],n[1]) for n in cur.fetchall()])
    cur.close()
    conn.close()
    return dict(content)
if __name__ == '__main__':
    # car_list = get_car_hastype()
    # with open('./file_danmu/已识别车型.txt','w') as f:
    #     f.write(f'-----更新时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}, 已识别车型共{len(car_list)}种-----\n')
    #     for car in car_list:
    #         f.write(car+'\n')
    # print("已识别车型数据更新完成！")
    brand = input("请输入要获取的车型：")
    comment_list = get_bad_comment(brand)
    with open(f'./file_danmu/未识别弹幕-{brand}.txt', 'w') as f:
        f.write(f'-----更新时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}, 品牌{brand}, 未识别弹幕共{len(comment_list)}条-----\n')
        for comment in comment_list:
            f.write(comment + '\n')
    print("未识别弹幕数据更新完成！")
    model_dict = get_car_dict(brand)
    with open(f'./file_danmu/原匹配弹幕-车型-{brand}.txt', 'w') as f:
        f.write(f'-----更新时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}, 品牌{brand}, 原匹配弹幕-车型共{len(model_dict)}条-----\n')
        for key in model_dict:
            f.write(key+' : '+model_dict.get(key)+'\n')
    print("原匹配弹幕-车型数据更新完成！")
