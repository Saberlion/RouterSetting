# -*- coding: utf8 -*-
#
import urllib2, base64
from settings import *

if __name__ == '__main__':  

    # 请求地址
    reboot_url = 'http://' + ip+'/userRpm/SysRebootRpm.htm?Reboot=%D6%D8%C6%F4%C2%B7%D3%C9%C6%F7'
    reboot_ref ='/userRpm/SysRebootRpm.htm'
    
    wan_static_url = 'http://' + ip +'/userRpm/WanStaticIpCfgRpm.htm?wantype=1&ip='+wan_static_ip+'&mask='+wan_static_mask+'&gateway=' +wan_static_gateway+'&mtu='+wan_static_mtu+'&dnsserver='+wan_static_dnsserver+'&dnsserver2='+wan_static_dnsserver+'&downBandwidth=0&upBandwidth=0&Save=%B1%A3+%B4%E6'
    wan_static_ref ='/userRpm/WanStaticIpCfgRpm.htm'
    
    pppoe_url ='http://' + ip +'/userRpm/PPPoECfgRpm.htm?wan=0&wantype=2&acc='+pppoe_usename+'&psw='+pppoe_password+'&confirm=' +pppoe_password+'&specialDial=100&SecType=0&sta_ip=0.0.0.0&sta_mask=0.0.0.0&linktype=1&waittime=15&Save=%B1%A3+%B4%E6'
    pppoe_ref ='/userRpm/PPPoECfgRpm.htm'
    
    wifi_psw_url ='http://' + ip +'/userRpm/WlanSecurityRpm.htm?vapIdx=1&secType=3&pskSecOpt=2&pskCipher=3&pskSecret='+wifi_psw +'&interval=86400&wpaSecOpt=3&wpaCipher=1&radiusIp=&radiusPort=1812&radiusSecret=&intervalWpa=86400&wepSecOpt=3&keytype=1&keynum=1&key1=&length1=0&key2=&length2=0&key3=&length3=0&key4=&length4=0&Save=%B1%A3+%B4%E6'
    wifi_psw_ref ='/userRpm/WlanSecurityRpm.htm'
    
    auth = 'Basic ' + base64.b64encode(login_user+':'+login_pw)
    print auth
    heads = { 'Referer' : 'http://' + ip + '/userRpm/SysRebootRpm.htm',
             'Authorization' : auth
    }
    
    while 1:
        print u'输入序号设置\n1.设置静态IP\n2.设置PPPOE \n3.设置wifi密码\n4.重启路由器\n5.退出'
        choice = input()
        if choice == 1:
            url = wan_static_url
            ref = wan_static_ref
        if choice == 2:
            url = pppoe_url
            ref = pppoe_ref
        if choice == 3:
            url = wifi_psw_url
            ref = wifi_psw_ref
        if choice == 4:
            url = reboot_url
            ref = reboot_ref
        if choice == 5:
            break
        if len(url)==0&len(ref)==0:
            continue
        heads = { 'Referer' : 'http://' + ip + ref,'Authorization' : auth }
        request = urllib2.Request(url, None, heads)
        try:
            response = urllib2.urlopen(request)
        except  urllib2.HTTPError   as e    :
            print   u'验证错误\n\n'
            continue
        except  urllib2.URLError   as e    :
            print u'连接错误，请确保正确连接到路由器\n\n'
            continue
        # print response.read().decode('gb2312').encode('utf8')
