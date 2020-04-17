import requests,os
from urllib.request import urlretrieve

def download_image():
    url='http://gamehelper.gm825.com/wzry/hero/list'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
    }
    res_json=requests.get(url,headers=headers).json()
    rs=res_json['list']
    hero_images='hero_download'#跟目录下 定义一个路径文件变量
    
    if not os.path.exists(hero_images):#如果不存在路径，就创建路径，存在就跳过
        os.mkdir(hero_images)
    
    for image_info in rs:
        hero_name=image_info['name']#获取JSON字典里面的name数据 就是英雄人物名字
        hero_image_url=image_info['cover']#获取英雄图片URL

        file_patch=hero_images + '/' + hero_name + '.png'#下载到本地的路径及本地名字

        urlretrieve(hero_image_url,file_patch)


if __name__ == "__main__":
    download_image()