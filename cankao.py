import pymysql
import csv

#得到经销商id
def get_name_id(name):
    conn = pymysql.connect(
        host='47.111.182.11',
        port=3306,
        user='develop',
        password='zKGFDXQFx467PPRc',
        db='ledi_master_sys',
        charset='utf8'
    )
    cur = conn.cursor()
    sql = f'select id from agent where nick_name like "%{name}%"'
    cur.execute(sql)
    id = cur.fetchall()
    if id != ():
        return id[0][0]
    return 0

def get_data(id):
    conn = pymysql.connect(
        host='47.111.182.11',
        port=3306,
        user='develop',
        password='zKGFDXQFx467PPRc',
        db='ledi_master_sys',
        charset='utf8'
    )
    cur = conn.cursor()
    sql = f'select all_audience_count, all_digg_count, all_comment_count, all_clue_count from live where cid={id} and live_time>="2021-4-6" and live_time<="2021-5-6"'
    cur.execute(sql)
    data = cur.fetchall()
    if data != ():
        data = [[n[0],n[1],n[2],n[3]] for n in data]
        cur.close()
        conn.close()
        return data
    return 0
def compute(data_list):
    sum_audience = 0
    sum_digg = 0
    sum_comment = 0
    sum_clue = 0
    for i in data_list:
        if i[0] is None:
            i[0] = 0
        elif i[1] is None:
            i[1] = 0
        elif i[2] is None:
            i[2] = 0
        elif i[3] is None:
            i[3] = 0
        sum_audience += i[0]
        sum_digg += i[1]
        sum_comment += i[2]
        sum_clue += i[3]
    sum_list = [sum_audience,sum_digg,sum_comment,sum_clue]
    return sum_list

if __name__ == '__main__':
    name_list = [
        '永达奥迪丽水店',
        '杭州德奥奥迪',
        '桐乡德奥奥迪',
        '温州红源奥迪',
        '城西德奥奥迪',
        '温州联奥奥迪',
        '杭州捷骏奥迪',
        '温州瓯通',
        '福州原动力',
        '永达奥迪湖州店',
        '通立奥迪',
        '东营金奥奥迪',
        '银座汽车奥迪',
        '恒信奥龙奥迪',
        '奥吉通国门',
        '南通益昌奥迪',
        '亳州远景',
        '永达奥诚奥迪',
        '新奥驰泰',
        '新元素雅麓'
    ]
    print("开始执行")
    with open('/Volumes/Don_disk/乐的一天/参考数据/20210514参考数据.csv', 'w', newline='', encoding='utf-8')as f:
        write = csv.writer(f)
        write.writerow(['经销商','观看总人次/月', '点赞总数/月', '总评论数/月', '总线索数/月'])
        for name in name_list:
            id = get_name_id(name)
            if id != 0:
                data = get_data(id)
                if data != 0:
                    finish_list = compute(data)write.writerow([name]+finish_list)

                pass
            else:
                print(f'此经销商不存在: {name}')
    print("执行完毕！")
