import pymysql
import csv

def get_tables(database):
    conn = pymysql.connect(
        host='47.111.182.11',
        port=3306,
        user='develop',
        password='zKGFDXQFx467PPRc',
        db=database,
        charset='utf8'
    )
    cur = conn.cursor()
    try:
        sql = 'SHOW TABLES'
        cur.execute(sql)
        result = cur.fetchall()
        result = [i[0] for i in result]
        result.remove('dou_yin_live_room_interactive_message')
        return result
    except:
        print("获取数据库表异常，请重试")
        return
    finally:
        conn.close()

def get_data(room_name):
    conn = pymysql.connect(
        host='47.111.182.11',
        port=3306,
        user='develop',
        password='zKGFDXQFx467PPRc',
        db='ledi_split',
        charset='utf8'
    )
    cur = conn.cursor()
    sql = f'select room_id, uid, capture_time, message_type, message from {room_name}'
    cur.execute(sql)
    data = cur.fetchall()
    if data != ():
        data = [[n[0],n[1],n[2].strftime('%Y-%m-%d-%H-%M-%S'),n[3],n[4]] for n in data]
        cur.close()
        conn.close()
        return data
    return 0





if __name__ == '__main__':
    print("正在执行")
    # 获得所有直播间数据表名-返回列表
    tables_name = get_tables('ledi_split')
    #遍历所有直播间
    for room_name in tables_name:
        #获得单个直播间所有信息
        data = get_data(room_name)
        #规格化信息类型
        if data != 0:
            for i in range(len(data)):
                if data[i][3] == 1:
                    data[i][3] = "弹幕: "+data[i][4]
                elif data[i][3] == 2:
                    data[i][3] = "进入直播间"
                elif data[i][3] == 3:
                    data[i][3] = "关注"
                elif data[i][3] == 4:
                    data[i][3] = "点赞"
                elif data[i][3] == 5:
                    data[i][3] = "分享"
                elif data[i][3] == 6:
                    data[i][3] = "礼物"
                elif data[i][3] == 7:
                    data[i][3] = "去购买"
            #得到最终信息
            data = [i[:-1] for i in data]
            data = sorted(data, key=lambda x: str(x[1]))
            with open(f'/Volumes/Don_disk/乐的一天/线索数据/{data[0][0]}.csv', 'w', newline='',encoding='utf-8')as f:
                write = csv.writer(f)
                write.writerow(['直播ID', '用户ID', '时间', '动作'])
                for item in data:
                    write.writerow(item)
    print("执行完毕！")


# zhiboriqi
