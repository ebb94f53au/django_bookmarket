import urllib.request
import re
import pymysql
urls='https://www.qidian.com/'
html=urllib.request.urlopen(urls).read().decode('utf-8')
urllist=re.findall('<div class="name-box"><a class="name" href="//(.+?)" target="_blank" data-eid="qd_A117"',html)
# db= pymysql.connect(host="localhost",user="root",
#  	password="ebb94f53au",db="bookmarket",port=3306)
# cur = db.cursor()
type={}
tnum=1
urllist=[]
names=[]
for i in urllist:
    print(i)
    h=urllib.request.urlopen('https://'+i).read().decode('utf-8')
    bookid=i.split('/info/')[1]
    name=re.findall('《(.*?)》',h)[0]
    if name in names:
        continue;
    else:
        names.append(name)
    t=re.findall('著_(.*?)_起点中文网',h)[0]
    if not t in type:
        type[t]=tnum
        sql1 = "insert into myapp_booktype(typename,isDelete) values('"+t+"',False)"
        #cur.execute(sql1)
        with open('type.txt','a')as f:
            f.write(sql1+'\n')
        f.close()
        tnum+=1
    img=re.findall('<a class="J-getJumpUrl"(?:.*?)<img src="//(.*?)">',h)[0]
    salesnums=re.findall('<i id="monthCount">(.*?)</i>',h)
    if len(salesnums)==0:
        salesnums=3000
    else:
        salesnums=salesnums[0]
    price=re.findall('<em id="todayNum">(.*?)</em>',h)
    if len(price)==0:
        price=30
    else:
        price=price[0]
    nums=re.findall('<i id="recCount">(.*?)</i>',h)[0]
    info=re.findall('<p class="intro">(.*?)</p>',h)[0]
    print(price)
    sql_insert ="insert into myapp_book(name,bookid,booktype_id,img,price,mprice,info,nums,salesnums,iswonderf,isDelete) values('"+str(name)+"','"+str(bookid)+"','"+str(type[t])+"','"+str(img)+"','"+str(price)+"','1000','"+str(info)+"','"+str(nums)+"','"+str(salesnums)+"',True,False)"
    print(sql_insert)
    with open('data.txt', 'a')as f:
        f.write(sql_insert + '\n')
    f.close()
#     cur.execute(sql_insert)
#
# db.commit()

print(type)
