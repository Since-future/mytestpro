#coding: utf8
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import pymongo
import urllib2
import urllib 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import md5
import base64
import hashlib
import xml.dom.minidom
from xmltojson import xmltojson
from xml.dom.minidom import parse, parseString
app = Flask(__name__)
def GenerateXml():
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, None, None)
    #生成request节点
    root = dom.createElement("Request")
    #添加属性
    root.setAttribute("service", "RouteService") #增加属性
    # root.setAttribute("lang", "zh-CN") #增加属性
    dom.appendChild(root) 
    #生成head节点
    # head = dom.createElement("Head")
    # headvalue = dom.createTextNode('OK')
    # head.appendChild(headvalue)
    # root.appendChild(head)
    #生成Body节点
    body = dom.createElement("Body")
    root.appendChild(body)
    #body节点下生成order节点，保存传递订单信息
    ordernode = dom.createElement("WaybillRoute")
    # #订单号
    ordernode.setAttribute("id", "11111111111")
    ordernode.setAttribute("mailno", "444993846033")
    ordernode.setAttribute("orderid", "10000001")
    ordernode.setAttribute("accept_time", "2014-11-21 17:41:39")
    ordernode.setAttribute("acceptAddress", "shenzhen")
    # ordernode.setAttribute("remark", "已收件")
    ordernode.setAttribute("opcode", "50")
    # body.appendChild(ordernode)
    body.appendChild(ordernode)
    # route = dom.createElement("Route")
    # route.setAttribute("remark", "已收件")
    # route.setAttribute("accept_time", "2014-11-21 17:41:39")
    # route.setAttribute("accept_address", "深圳")
    # route.setAttribute("opcode", "50")
    # ordernode.appendChild(route)
    m = dom.toxml('UTF-8')
    print(m)
    # ms = "<Request service='OrderService' lang='zh-CN'><Head>BSPdevelop</Head><Body><Order  orderid='10000001' express_type='1' j_province='广东省' j_city='深圳市' j_company='顺丰速运' j_contact='喵小萌' j_tel='95338' j_address='广东省深圳市福田区新洲十一街' d_province='北京' d_city='北京' d_company='一家公司' d_contact='萌小喵' d_tel='18888998899' d_address='北京市海淀区科学园科健路908' parcel_quantity='1' pay_method='1' custid='7551878519' ><Cargo name='服装' count='1' unit='台' weight='2.36' amount='2000' currency='CNY' source_area='中国'></Cargo></Order></Body></Request>"
    # checkword = "j8DzkIFgmlomPt0aLuwU"
    # mymd = hashlib.md5()
    # mymd.update(m + checkword)
    # sig = mymd.digest()
    # # sig = md5.new(ms + checkword).hexdigest()
    # # auth = base64.encodestring(sig)
    # auth = base64.b64encode(sig)
    # print(auth)
    url = "http://test.tianshidili.cn/tsdlshunfeng"
    data = {'message': m}
    req = urllib2.Request(url)
    da = urllib.urlencode(data)
    try:
        response = urllib2.urlopen(req, da)
    except urllib2.HTTPError,e:
        print e.code
        print e.read()
    
    a = response.read()
    print(a)
    # xtj = xmltojson()
    # locations = xtj.main(a)
    # print(m)
    # xtj = xmltojson()
    # locations = xtj.get_root(m)
    # print(xtj.get_element_children(locations))
    # ass = xtj.get_element_children(locations)
    # threenodes = xtj.get_element_children(ass[1])
    # myattes = xtj.get_element_attrib(threenodes[0])

    # print(myattes["remark"])
    


    # print(url)
    # req = urllib2.Request(url)
    # res = urllib2.urlopen(req);
    # data = res.read()
    # print(data)
    


if __name__ == '__main__':
    GenerateXml()