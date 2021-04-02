import pymysql
import time

#得到不能识别的弹幕数据，返回类型：列表+字符串
def get_bad_comment():
    conn = pymysql.connect(
        host='8.136.102.203',
        port=6001,
        user='dingcong',
        password='wdnCLPiSnh6AwUTm',
        db='dy_live',
        charset='utf8'
    )
    cur = conn.cursor()
    # 获取所有type为1的弹幕
    sql1 = f'select content from danmu where type={1} and auto_type is null'  #查找原模型不能判断的弹幕
    cur.execute(sql1)
    content = [n[0] for n in cur.fetchall()]
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

def get_car_dict():
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
    sql1 = f'select content,auto_type from danmu where type={1} and auto_type is not null'
    cur.execute(sql1)
    content = dict([(n[0],n[1]) for n in cur.fetchall()])
    cur.close()
    conn.close()
    return content
if __name__ == '__main__':
    car_list = get_car_hastype()
    with open('./file_danmu/已识别车型.txt','w') as f:
        f.write(f'-----更新时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}, 已识别车型共{len(car_list)}种-----\n')
        for car in car_list:
            f.write(car+'\n')
    print("已识别车型数据更新完成！")
    comment_list = get_bad_comment()
    with open('./file_danmu/未识别弹幕.txt', 'w') as f:
        f.write(f'-----更新时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}, 未识别弹幕共{len(comment_list)}条-----\n')
        for comment in comment_list:
            f.write(comment + '\n')
    print("未识别弹幕数据更新完成！")
    model_dict = get_car_dict()
    with open('./file_danmu/原匹配弹幕-车型.txt', 'w') as f:
        f.write(f'-----更新时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}, 原匹配弹幕-车型共{len(model_dict)}条-----\n')
        for key in model_dict:
            f.write(key+' : '+model_dict.get(key)+'\n')
    print("原匹配弹幕-车型数据更新完成！")
