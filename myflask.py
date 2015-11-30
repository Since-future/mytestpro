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
    root.setAttribute("service", "OrderService") #增加属性
    root.setAttribute("lang", "zh-CN") #增加属性
    dom.appendChild(root) 
    #生成head节点
    head = dom.createElement("Head")
    headvalue = dom.createTextNode('PLY')
    head.appendChild(headvalue)
    root.appendChild(head)
    #生成Body节点
    body = dom.createElement("Body")
    root.appendChild(body)
    #body节点下生成order节点，保存传递订单信息
    ordernode = dom.createElement("Order")
    #订单号
    ordernode.setAttribute("orderid", "my00003")
    # #寄件公司名称
    # ordernode.setAttribute("j_company", "")
    # #寄件方联系人
    # ordernode.setAttribute("j_contact", "")
    # #寄件方联系电话
    # ordernode.setAttribute("j_tel", "")
    # #寄件方手机
    ordernode.setAttribute("j_mobile", "18620558165")
    # #寄件方所在省份
    # ordernode.setAttribute("j_province", "")
    # #寄件方所在城市
    # ordernode.setAttribute("j_city", "")
    # #寄件人所在县区
    # ordernode.setAttribute("j_county", "")
    # #寄件方详细地址
    ordernode.setAttribute("j_address", "广州市大学城北国家数字基地创业楼A401")
    #到件方公司名称
    ordernode.setAttribute("d_company", "天食地力")
    #到件方联系人
    ordernode.setAttribute("d_contact", "天食地力")
    #到件方联系电话
    ordernode.setAttribute("d_tel", "18620558165")
    #到件方手机
    ordernode.setAttribute("d_mobile", "18620558165")
    #到件方详细地址
    ordernode.setAttribute("d_address", "广州市大学城北国家数字基地创业楼A401")
    #快件产品类别
    ordernode.setAttribute("express_type", "3")
    #付款方式
    ordernode.setAttribute("pay_method", "1")
    #包裹数
    ordernode.setAttribute("parcel_quantity", "1")
    #备注
    #ordernode.setAttribute("remark", "sdsdasdasdasdas")
    body.appendChild(ordernode)
    addmonnode = dom.createElement("AddedService")
    addmonnode.setAttribute("name", "COD")
    addmonnode.setAttribute("value", '198.00')
    addmonnode.setAttribute("value1", "6236683320006442636")
    ordernode.appendChild(addmonnode)
    m = dom.toxml('UTF-8')
    # ms = "<Request service='OrderService' lang='zh-CN'><Head>BSPdevelop</Head><Body><Order  orderid='10000001' express_type='1' j_province='广东省' j_city='深圳市' j_company='顺丰速运' j_contact='喵小萌' j_tel='95338' j_address='广东省深圳市福田区新洲十一街' d_province='北京' d_city='北京' d_company='一家公司' d_contact='萌小喵' d_tel='18888998899' d_address='北京市海淀区科学园科健路908' parcel_quantity='1' pay_method='1' custid='7551878519' ><Cargo name='服装' count='1' unit='台' weight='2.36' amount='2000' currency='CNY' source_area='中国'></Cargo></Order></Body></Request>"
    checkword = "lsxf0h0HVVn9aHli"
    mymd = hashlib.md5()
    mymd.update(m + checkword)
    sig = mymd.digest()
    # sig = md5.new(ms + checkword).hexdigest()
    # auth = base64.encodestring(sig)
    auth = base64.b64encode(sig)
    print(auth)
    url = "http://218.17.248.244:11080/bsp-oisp/sfexpressService"
    data = {'xml': m, 'verifyCode': auth}
    req = urllib2.Request(url)
    da = urllib.urlencode(data)
    response = urllib2.urlopen(req, da)
    a = response.read()
    print(a)
    # xtj = xmltojson()
    # locations = xtj.main(a)
    # print(locations["ERROR"])
    # locations["Head"]
    # print(m)
    xtj = xmltojson()
    print(xtj)
    backdom = xtj.get_root(a)
    twonodes = xtj.get_element_children(backdom)
    threenodes = xtj.get_element_children(twonodes[1])
    myattr = xtj.get_element_attrib(threenodes[0])
    print(myattr["orderid"])
    print(myattr["mailno"])


    # print(myattes["remark"])
    


    # print(url)
    # req = urllib2.Request(url)
    # res = urllib2.urlopen(req);
    # data = res.read()
    # print(data)
    

def GetyuantongXml():
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None, None, None)
    #生成request节点
    root = dom.createElement("RequestOrder")
    dom.appendChild(root) 

    #生成clientID节点
    clientID = dom.createElement("clientID")
    clientIDval = dom.createTextNode('TEST')
    clientID.appendChild(clientIDval)
    root.appendChild(clientID)

    #生成logisticProviderID节点
    logisticProviderID = dom.createElement("logisticProviderID")
    logisticProviderIDval = dom.createTextNode("YTO")
    logisticProviderID.appendChild(logisticProviderIDval)
    root.appendChild(logisticProviderID)

    #生成txLogisticID节点(clientid+订单号)
    txLogisticID = dom.createElement("txLogisticID")
    txLogisticIDval = dom.createTextNode("LP07082300225709")
    txLogisticID.appendChild(txLogisticIDval)
    root.appendChild(txLogisticID)

    # #生成tradeNo节点
    # tradeNo = dom.createElement("tradeNo")
    # tradeNoval = dom.createTextNode("2007082300225709")
    # tradeNo.appendChild(tradeNoval)
    # root.appendChild(tradeNo)

    #生成mailNo节点
    mailNo = dom.createElement("mailNo")
    mailNoval = dom.createTextNode("124579546621")
    mailNo.appendChild(mailNoval)
    root.appendChild(mailNo)

    # #生成totalServiceFee节点
    # totalServiceFee = dom.createElement("totalServiceFee")
    # totalServiceFeeval = dom.createTextNode("0.0")
    # totalServiceFee.appendChild(totalServiceFeeval)
    # root.appendChild(totalServiceFee)

    # #生成codSplitFee节点
    # codSplitFee = dom.createElement("codSplitFee")
    # codSplitFeeval = dom.createTextNode("0.0")
    # codSplitFee.appendChild(codSplitFeeval)
    # root.appendChild(codSplitFee)

    #生成orderType节点
    orderType = dom.createElement("orderType")
    orderTypeval = dom.createTextNode("1")
    orderType.appendChild(orderTypeval)
    root.appendChild(orderType)

    #生成serviceType节点
    serviceType = dom.createElement("serviceType")
    serviceTypeval = dom.createTextNode("0")
    serviceType.appendChild(serviceTypeval)
    root.appendChild(serviceType)

    #生成flag节点
    # flag = dom.createElement("flag")
    # flagval = dom.createTextNode("0")
    # flag.appendChild(flagval)
    # root.appendChild(flag)

    """
    生成发货方信息sender节点
    """
    sender = dom.createElement("sender")
    root.appendChild(sender)


    #生成name
    name = dom.createElement("name")
    nameval = dom.createTextNode("张三")
    name.appendChild(nameval)
    sender.appendChild(name)

    #生成postCode
    postCode = dom.createElement("postCode")
    postCodeval = dom.createTextNode("510000")
    postCode.appendChild(postCodeval)
    sender.appendChild(postCode)

    #生成mobile
    mobile = dom.createElement("mobile")
    mobileval = dom.createTextNode("18620558165")
    mobile.appendChild(mobileval)
    sender.appendChild(mobile)

    #生成prov
    prov = dom.createElement("prov")
    provval = dom.createTextNode("广东省")
    prov.appendChild(provval)
    sender.appendChild(prov)

    #生成city
    city = dom.createElement("city")
    cityval = dom.createTextNode("广州市")
    city.appendChild(cityval)
    sender.appendChild(city)



    #生成address
    address = dom.createElement("address")
    addressval = dom.createTextNode("白云区天河北路123号")
    address.appendChild(addressval)
    sender.appendChild(address)
 
    """
    收货方信息receiver节点
    """
    receiver = dom.createElement("receiver")
    root.appendChild(receiver)

    #生成name
    name = dom.createElement("name")
    nameval = dom.createTextNode("张三")
    name.appendChild(nameval)
    receiver.appendChild(name)

    #生成postCode
    postCode = dom.createElement("postCode")
    postCodeval = dom.createTextNode("310013")
    postCode.appendChild(postCodeval)
    receiver.appendChild(postCode)
    
    #生成mobile
    mobile = dom.createElement("mobile")
    mobileval = dom.createTextNode("18620558165")
    mobile.appendChild(mobileval)
    receiver.appendChild(mobile)

    #生成prov
    prov = dom.createElement("prov")
    provval = dom.createTextNode("广东省")
    prov.appendChild(provval)
    receiver.appendChild(prov)

    #生成city
    city = dom.createElement("city")
    cityval = dom.createTextNode("广州市")
    city.appendChild(cityval)
    receiver.appendChild(city)

    

    #生成address
    address = dom.createElement("address")
    addressval = dom.createTextNode("白云区天河北路123号")
    address.appendChild(addressval)
    receiver.appendChild(address)
    """ 添加商品属性 """
    items = dom.createElement("items")
    root.appendChild(items)
    item = dom.createElement("item")
    items.appendChild(item)

    #生成itemName
    itemName = dom.createElement("itemName")
    itemNameval = dom.createTextNode("智能手表")
    itemName.appendChild(itemNameval)
    item.appendChild(itemName)

    #生成itemName
    number = dom.createElement("number")
    numberval = dom.createTextNode("1")
    number.appendChild(numberval)
    item.appendChild(number)

    #生成special
    special = dom.createElement("special")
    specialval = dom.createTextNode("0")
    special.appendChild(specialval)
    root.appendChild(special)


    m = dom.toxml('UTF-8')
    # ms = "<Request service='OrderService' lang='zh-CN'><Head>BSPdevelop</Head><Body><Order  orderid='10000001' express_type='1' j_province='广东省' j_city='深圳市' j_company='顺丰速运' j_contact='喵小萌' j_tel='95338' j_address='广东省深圳市福田区新洲十一街' d_province='北京' d_city='北京' d_company='一家公司' d_contact='萌小喵' d_tel='18888998899' d_address='北京市海淀区科学园科健路908' parcel_quantity='1' pay_method='1' custid='7551878519' ><Cargo name='服装' count='1' unit='台' weight='2.36' amount='2000' currency='CNY' source_area='中国'></Cargo></Order></Body></Request>"
    partnerId = "123456"
    mymd = hashlib.md5()
    mymd.update(m + partnerId)
    sig = mymd.digest()
    # sig = md5.new(ms + checkword).hexdigest()
    # auth = base64.encodestring(sig)
    auth = base64.b64encode(sig)
    print(auth)
    # urlm = urllib.quote(m)
    url = "http://58.32.246.92:9081/ordws/Vip16Servlet"
    data = {'logistics_interface': m, 'data_digest': auth, 'type': 'offline', 'clientId': 'TEST'}
    req = urllib2.Request(url)
    da = urllib.urlencode(data)
    response = urllib2.urlopen(req, da)
    a = response.read()
    print(a)
    # xtj = xmltojson()
    # locations = xtj.main(a)
    # print(locations["ERROR"])
    # locations["Head"]
    # print(m)
    xtj = xmltojson()
    print(xtj)
    backdom = xtj.main(a)
    print(backdom["success"])
    # print(backdom["reason"])


    # print(myattes["remark"])
    


    # print(url)
    # req = urllib2.Request(url)
    # res = urllib2.urlopen(req);
    # data = res.read()
    # print(data)


if __name__ == '__main__':
    GetyuantongXml()