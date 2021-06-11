import requests
from lxml import etree

def get_mid(brand):
    with open('/Users/dingcong/ledi_git/易车/carMid.txt', 'r') as f:
        carMid_json = eval(f.read())
    mid = carMid_json[brand]
    return mid

if __name__ == '__main__':
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    brand = "奥迪"
    mid = get_mid(brand)
    #得到车型页数
    url = f'https://car.yiche.com/xuanchegongju/?mid={mid}'
    r = requests.get(url, headers=header)
    tree = etree.HTML(r.text)
    page_num = tree.xpath('//div[@class="link-list pg-item"]//a/text()')
    base_url = f'https://car.yiche.com/xuanchegongju/?mid={mid}&page='
    title_list = []
    carId_list = []
    for i in range(1, len(page_num)+1):
        current_url = base_url + str(i)
        r = requests.get(current_url, headers=header)
        tree = etree.HTML(r.text)
        title_list += tree.xpath('//div[@class="search-result-list"]//div/a/p[1]/text()')
        carId_list += tree.xpath('//div[@class="search-result-list"]//div/@data-id')
    # 判断是否车型名称与车型id匹配
    if len(title_list) == len(carId_list):
        carId_dict = dict(zip(title_list, carId_list))
    with open(f'{brand}carId.txt', 'w') as f:
        f.write(str(carId_dict))
    print("车型ID获取完成，已保存")