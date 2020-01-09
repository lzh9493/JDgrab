# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:26:32 2020

@author: lzh12
"""

import requests
import re

#登录后才能访问的网页
ur='https://search.jd.com/Search?keyword=%E7%94%B5%E8%A7%86%E6%9C%BA&enc=utf-8&wq=%E7%94%B5%E8%A7%86%E6%9C%BA&pvid=7292c86957654f7b83282176ac0d011f'
head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
            }
#浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = r'__jdu=15780251186351151305178; shshshfpa=9cad7ac9-acc3-786d-c588-867c0d90f89c-1578025119; shshshfpb=9cad7ac9-acc3-786d-c588-867c0d90f89c-1578025119; areaId=9; unpl=V2_ZzNtbUsES0V2DxUAfhsJDGIBG1sRVkEVJQESBitNXQRvBBoPclRCFnQUR1RnGFgUZgsZWUBcQhFFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsdWgxmABZdQl5EF3EIRlB7G10BZwUbbXJQcyVFAENRfB9YNWYzE20AAx8SdwtEXTYZWANuAhFZQldKEncMRlR%2fGV4EYwMUVHJWcxY%3d; ipLoc-djd=9-674-24075-51846; user-key=4dccdf4b-3cd0-4fe6-884d-d5fcb86c2be1; __jdv=122270672|baidu|-|organic|not set|1578448657427; pinId=UEtomfFDRL1Baxrw-gtETbV9-x-f3wj7; pin=jd_53e3e9d6f2018; unick=jd_156525fts; _tp=CcDyqVZALp%2BCWekrdbpauSdgjjoOlb0THQ9qJqJtp1A%3D; _pst=jd_53e3e9d6f2018; o2State={%22webp%22:true%2C%22lastvisit%22:1578535037553}; TrackID=1XRbciD8T5UioA9feUg_AQeEmFBCLs18sJRmpLWKJg-JMmPjebcp86gCBsggUE-I5eN9Oi4uajTo3Z-3LC905MxDE4lmnte28i3dU1R6bZPg; thor=1847F1432BDE1FED0ADA13B28EFED68790A868210EA50B2E9F4B7155338418DC58CFAB7BF9579E49F6EBA8A07EEE6B2BE159A82996F21AE956243D7B2D79A5A655B85B5BF9F86F4EE23D60D432ACE702D4631FEC99FBF0C92D8E688584E0F9C0C3A30761D1B211729453BFF1FDD91B5EA43238A6D889B70066F320C6EBD454DA820E465494DC029AB13C1F99ACC6E0D652D009B1EADD6E584DA713C2352F6D59; ceshi3.com=000; __jda=122270672.15780251186351151305178.1578025119.1578448657.1578535037.11; __jdb=122270672.22.15780251186351151305178|11.1578535037; __jdc=122270672; shshshfp=ef8d5d2b38a764fc9c25b01874ac14f6; shshshsID=f8c739a9c7ec142fbc60a6d287164754_10_1578535673648; 3AB9D23F7A4B3C9B=57O5JUNAVQWKDDNMIR5OJVXZUDLSL6FN5GUIV7XUST5OXINZHQIXVCM2C3WQMF3YJLWVD33G3SDWMY5IYDZQPZINY4'

#把cookie字符串处理成字典，以便接下来使用
cookies_jar = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies_jar[key] = value
strhtml = requests.get(ur,headers=head,cookies=cookies_jar)
strhtml.encoding='utf-8'

pattern_goodswebcode=re.compile('<li+.*data-sku="(.*?)"')
string=strhtml.text
goodswebcodes=pattern_goodswebcode.findall(string)

cpu_list=[]
pattern_cpu=re.compile(r'<dt>CPU</dt>+[\s\S]*?<dd>+(.*?)</dd>[\s\S]*?</dl>')

for goodswebcode in goodswebcodes:
    ur_now='https://item.jd.com/'+goodswebcode+'.html'
    strhtml = requests.get(ur_now)
    string=strhtml.text
    CPU=pattern_cpu.findall(string)
    cpu_list.append(CPU)