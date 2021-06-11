import pymysql
import time

def get_car_brand():
    conn = pymysql.connect(
        host='8.136.102.203',
        port=6001,
        user='dingcong',
        password='wdnCLPiSnh6AwUTm',
        db='dy_live',
        charset='utf8'
    )
    cur = conn.cursor()
    brand_list = ['奥迪','宝马','奔驰','沃尔沃','大众','保时捷','雷克萨斯','东风本田']
    brand_dict = {}
    for brand in brand_list:
        sql1 = f'select id from agent where brand="{brand}"'
        cur.execute(sql1)
        id = [n[0] for n in cur.fetchall()]
        temp_list = []
        for item in id:
            sql2 = f'select id from live where cid={item}'
            cur.execute(sql2)
            lid = [n[0] for n in cur.fetchall()]
            temp_list.extend(lid)
        brand_dict[brand] = map(str,temp_list)     #将列表中的数字转成字符串，返回的是迭代器
    cur.close()
    conn.close()
    with open('./file_danmu/品牌-直播间.txt','w') as f:
        for key in brand_dict:
            try:
                value = ','.join(brand_dict.get(key))
                f.write(key+' : '+value+'\n')
            except:
                print(brand+'error')
    print("品牌与车型关系数据已整理完成！")
get_car_brand()