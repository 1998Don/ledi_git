import requests
from lxml import etree

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}
base_url = 'https://car.yiche.com/xuanchegongju/'
title_list = []
mid_list = []
r = requests.get(base_url, headers=header)
tree = etree.HTML(r.text)
title_list += tree.xpath('//div[@class="brand-list"]//div[@class="brand-list-item"]//div[@class="item-brand"]/@data-name')
mid_list += tree.xpath('//div[@class="brand-list"]//div[@class="brand-list-item"]//div[@class="item-brand"]/@data-id')

#判断是否车型名称与车型mid匹配
if len(title_list) == len(mid_list):
    carMid_dict = dict(zip(title_list,mid_list))
with open('carMid.txt','w') as f:
    f.write(str(carMid_dict))
print("易车网车型MID获取完成，已保存")