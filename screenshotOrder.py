import cv2
import time
import os
import pymysql
import multiprocessing

class ReadVideo:
    def hand_check(self,check_dir):
        needDir = []
        dir_list = os.listdir(check_dir)
        with open('./hasDir.txt','r') as f:
            has_list = f.readlines()
        has_list = [i.strip('\n') for i in has_list]
        for item in dir_list:
            if item in has_list:
                pass
            else:
                needDir.append(item)
        if needDir == []:
            print("经检查所有直播间视频均已截取完毕，无新任务！")
            return 1
        else:
            print(f"经检查发现有新任务，待处理直播间个数为{len(needDir)}正在处理！")
            return needDir
    def auto_check(self):
        needDir = []
        conn = pymysql.connect(
        host='8.136.102.203',
        port=6001,
        user='dingcong',
        password='wdnCLPiSnh6AwUTm',
        db='dy_live',
        charset='utf8'
        )
        cur = conn.cursor()
        sql1 = 'select id from agent where brand="奥迪"'
        cur.execute(sql1)
        id_list = [n[0] for n in cur.fetchall()]
        dir_list = []
        for item in id_list:
            sql2 = f'select live_time,room_id from live where cid={item} and live_time>="2021-5-6"'
            cur.execute(sql2)
            lid = [[n[0].strftime('%Y-%m-%d'),n[1]] for n in cur.fetchall()]
            dir_list.extend(lid)
        dir_list = [[i[0].replace('-',''),i[1]] for i in dir_list]   #日期，直播间
        cur.close()
        conn.close()
        with open('./hasDir.txt','r') as f:
            has_list = f.readlines()
        has_list = [i.strip('\n') for i in has_list]
        for item in dir_list:
            dir1 = item[0]+'/'+item[1]
            dir2 = item[1]+'/'+item[0]
            if '/home2/video_data/'+dir1 in has_list:
                pass
            elif '/home2/video_data/'+dir2 in has_list:
                pass
            else:
                needDir.append(item)
        if needDir == []:
            print("经检查所有直播间视频均已截取完毕，无新任务！")
            return 1
        else:
            print(f"经检查发现有新任务，待处理直播间个数为{len(needDir)}正在处理！")
            for i in range(len(needDir)):
                if os.path.exists('/home2/video_data/' + needDir[i][0] + '/' + needDir[i][1]):
                    needDir[i] = ('/home2/video_data/' + needDir[i][0] + '/' + needDir[i][1])
                elif os.path.exists('/home2/video_data/' + needDir[i][1] + '/' + needDir[i][0]):
                    needDir[i] = ('/home2/video_data/' + needDir[i][1] + '/' + needDir[i][0])
            needDir = list(filter(lambda x : type(x) is str,needDir))
            print(f"待处理直播间如下：")
            for item in needDir:
                print(item)
            return needDir
    #传入文件夹地址，生成命名文件夹和视频地址列表
    def make_dir(self,single_dir):
        video_list = os.listdir(single_dir)
        temp = single_dir.split('/')
        if len(temp[-1]) <= 8:
            dir_name = temp[-2]
        else:
            dir_name = temp[-1]
        dir_name = '/home3/奥迪视频帧/'+dir_name
        if os.path.exists(dir_name):
            pass
        else:
            os.mkdir(dir_name)
        return sorted(video_list),dir_name+'/'
    #传入视频地址，读取视频帧并保存
    def make_img(self,single_dir,video_path,dirname):
        start_num = eval(video_path[0].split('-')[-1].split('.')[0])
        for url in video_path:
            real_dir = single_dir +'/' + url
            #读入视频文件
            start_time = time.time()
            vc = cv2.VideoCapture(real_dir)
            if vc.isOpened():
            # 判断是否正常打开
                real, frame = vc.read()
            else:
                real = False
            pre_time = time.time()
            while real and (time.time()-start_time)<=7200:
                try:
                    real, frame = vc.read()
                    time.sleep(0.1)
                    if (time.time()-pre_time)>=1:
                        cv2.imwrite(dirname + str(start_num) + '.jpg', frame)
                        # print("截图完成")
                        pre_time = time.time()
                        start_num += 1
                except:
                    pass
            vc.release()
        with open('./hasDir.txt','a') as f:
            f.write(single_dir+'\n')
        print(f"本文件夹中视频共截取{c}张图片")
    def real_run(self,single_dir):
        video_list, dirname = self.make_dir(single_dir)
        self.make_img(single_dir,video_list,dirname)
if __name__ == '__main__':
    video = ReadVideo()
    # check_dir = input("请输入要检查的路径：")
    # flag = video.hand_check(check_dir)
    pool = multiprocessing.Pool(35)
    flag = video.auto_check()
    if flag != 1:
        print("开始整理")
        for single_dir in flag:
            # video_list, dirname = video.make_dir(single_dir)
            # video.make_img(single_dir,video_list,dirname)
            pool.apply_async(video.real_run,(single_dir,))
        pool.close() # 关闭进程池
        pool.join()
        print("新任务已处理完成！")
    with open('./hasDir.txt','a') as f:
        f.write(f'----以上信息更新时间为: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}----\n')
        # 'stream-685200200990457995_or4_1797.ts','stream-685200200990457995_or4_1798.ts','stream-685200200990457995_or4_1796.ts','stream-685200200990457995_or4_1794.ts'
        'pull-f3.douyincdn.com_stream-396903805625303141_or4-1619365695709.ts','pull-f3.douyincdn.com_stream-396903805625303141_or4-1619365687661.ts','pull-f3.douyincdn.com_stream-396903805625303141_or4-1619365691652.ts'
        'pull-l3.douyincdn.com_stream-396909199161819218_or4-1619445082674.ts','pull-l3.douyincdn.com_stream-396909199161819218_or4-1619445070690.ts'