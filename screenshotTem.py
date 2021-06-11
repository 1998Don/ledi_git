import cv2
import time
import os
import multiprocessing

class ReadVideo:
    #传入文件夹地址，生成命名文件夹和视频地址列表
    def make_dir(self,single_dir):
        video_list = os.listdir(single_dir)
        temp = single_dir.split('/')
        if len(temp[-1]) <= 8:
            dir_name = temp[-2]
        else:
            dir_name = temp[-1]
        dir_name = './'+dir_name
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
                        pre_time = time.time()
                        start_num += 1
                except:
                    pass
            vc.release()
    def real_run(self,single_dir):
        video_list, dirname = self.make_dir(single_dir)
        self.make_img(single_dir,video_list,dirname)
if __name__ == '__main__':
    video = ReadVideo()
    pool = multiprocessing.Pool(2)
    room = ['6955099386389252876','6955444566107425548']
    print("开始整理")
    for single_dir in room:
        pool.apply_async(video.real_run,(single_dir,))
    pool.close() # 关闭进程池
    pool.join()
    print("新任务已处理完成！")