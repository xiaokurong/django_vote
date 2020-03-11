import requests
import json
with open('herolist.json','rt',encoding="utf-8") as f:
    herolist = json.load(f)
    for i in herolist:
        # print(i['ename'],i['cname'],i['title'],i['skin_name'])
        try:
            # print(i['ename'],i['cname'],i['title'],i['skin_name'])
            urls = "http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/"
            hero_urls= urls+str(i['ename'])+"/"+str(i['ename'])+"-bigskin-1.jpg"
            print(hero_urls)
            img=requests.get(hero_urls)
            if img.status_code==200 :
                open(str(i['cname'])+'.jpg','wb').write(img.content)
        except Exception as error:
            print ('dict error******',i['ename'])