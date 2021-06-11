import pymysql
import csv
import pandas as pd
import multiprocessing

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

def get_table_data(room_name,uid):
    conn = pymysql.connect(
        host='47.111.182.11',
        port=3306,
        user='develop',
        password='zKGFDXQFx467PPRc',
        db='ledi_split',
        charset='utf8'
    )
    cur = conn.cursor()
    sql = f'select message_type, message from {room_name} where uid="{uid}"'
    cur.execute(sql)
    data = cur.fetchall()
    if data != ():
        data = [[n[0],n[1]] for n in data]
        cur.close()
        conn.close()
        return data
    return 0

def exec(uid,room_list):
    with open(f'/home3/test/clue2/{uid}.csv', 'w', newline='', encoding='utf-8')as f:
        write = csv.writer(f)
        write.writerow(['room_id', '动作1', '动作2', '动作3', '动作4', '动作5', '动作6', '动作7'])
        for room in room_list:
            data = get_table_data(room,uid)
            # 规格化信息类型
            if data != 0:
                for i in range(len(data)):
                    if data[i][0] == 1:
                        data[i][0] = "弹幕: "+data[i][1]
                    elif data[i][0] == 2:
                        data[i][0] = "进入直播间"
                    elif data[i][0] == 3:
                        data[i][0] = "关注"
                    elif data[i][0] == 4:
                        data[i][0] = "点赞"
                    elif data[i][0] == 5:
                        data[i][0] = "分享"
                    elif data[i][0] == 6:
                        data[i][0] = "礼物"
                    elif data[i][0] == 7:
                        data[i][0] = "去购买"
                #得到最终信息
                data = [room.split('_')[-1]]+[i[0] for i in data]
                write.writerow(data)

if __name__ == '__main__':
    df = pd.read_excel('/home3/test/clue.xlsx',engine='openpyxl')
    uid_list = df.values
    pool = multiprocessing.Pool(40)
    room_list = get_tables('ledi_split')
    print("正在整理")
    for uid in uid_list:
        try:
            pool.apply_async(exec, (uid[0],room_list))
        except:
            print("这个用户出错了： ",uid[0])
            pass
    pool.close()  # 关闭进程池
    pool.join()
    print("执行完毕！")