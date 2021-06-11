import requests
import pandas as pd
import os

#请求头
header = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate'
        }
#获取数据源
df=pd.read_excel('三家经销商互动数据.xlsx')
data = df.values
print(f"共有{len(data)}条数据信息")
basis_dir = '/Volumes/Don_disk/乐的一天/互动数据文件/'
for file in data:
    if not os.path.exists(basis_dir+str(file[1])):
        os.mkdir(basis_dir+str(file[1]))
    xls = requests.get(file[-1],headers=header).content
    with open(basis_dir+str(file[1])+f'/{file[3]}.xls','wb') as f:
        f.write((xls))
print('整理完成')

