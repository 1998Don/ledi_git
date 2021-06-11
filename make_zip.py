import zipfile
import requests
import pandas as pd
import os
import shutil

def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    print(r)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
    else:
        print('This is not zip')

def get_file():
    #请求头
    header = {
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
                'Accept-Encoding': 'gzip, deflate'
            }
    #获取数据源
    df=pd.read_excel('副本压缩包.xlsx')
    data = df.values
    print(f"共有{len(data)}条数据信息")
    basis_dir = '/Volumes/Don_disk/乐的一天/1111/'
    for file in data:
        #得到文件夹日期
        date_ = file[-1].split('/')[-1].split('_')[1]
        zip = requests.get(file[-1],headers=header).content
        with open(basis_dir+date_+'.zip','wb') as f:
            f.write((zip))
    print('整理完成')
def make_run(path):
    save_path = '/Volumes/Don_disk/乐的一天/历史直播数据集/'
    paths = os.listdir(path)
    print("数据整理中.......")
    for item in paths:
        if '.' in item:
            continue
        # print(item)
        files = os.listdir(path+item)
        for file in files:
            if '._' in file:
                continue
            # print(file)
            dir_name = file.split('_')[1]
            file_name = item+'_'+file.split('_')[-1]
            if not os.path.exists(save_path + dir_name):
                os.mkdir(save_path + dir_name)
            shutil.copyfile(path+item+'/'+file, save_path+dir_name+'/'+file_name)
    print("数据整理完成！")



if __name__ == '__main__':
    make_run('/Volumes/Don_disk/乐的一天/1111/')