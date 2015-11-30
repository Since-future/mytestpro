#coding: utf8
from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)


def get_db():
    #创建链接
    cl = MongoClient("127.0.0.1", 27017)
    db = cl.test
    # print (db)
    return db


# def get_collection(db):
#     #选择集合(mongo中collection和database都是lazy创建的，具体可以google下)
#     collection = db['posts']
#     print ....


def insert_one_doc(db):
    #插入一个document
    posts = db.posts
    post = {"name": "lzz", "age": 25, "weight": "55"}
    post_id = posts.insert(post)
    print post_id


##查询，可以对整个集合查询，可以根ObjectId查询，可以根据某个字段查询等
# def get_all_colls(db):
#     #获得一个数据库中的所有集合名称
#     print(11111111)
#     print db.collection_names()


def insert_mulit_docs(db):
    #批量插入documents,插入一个数组
    posts = db.posts
    post = [{"name": "nine", "age": 28, "weight": "55"}, {"name": "jack", "age": 25, "weight": "55"}]
    obj_ids = posts.insert(post)
    print obj_ids


def updatename(db):
    #修改名称
    db.posts.update({"name": "bubu"}, {"name": "liuliu"}, True)


def getmama(db):
    print db.posts.find_one({"name": "bubu"})
# def get_one_doc(db):
#     #有就返回一个，没有就返回None
#     posts = db.posts
#     print posts.find_one()
#     print posts.find_one({"name": "jack"})
#     print posts.find_one({"name": "None"})
#     return


# def get_one_by_id(db):
#     #通过objectid来查找一个doc
#     posts = db.posts
#     obj = posts.find_one()
#     obj_id = obj["_id"]
#     print "_id 为ObjectId类型 :"
#     print posts.find_one({"_id": obj_id})
#     #需要注意这里的obj_id是一个对象，不是一个str，使用str类型作为_id的值无法找到记录
#     print "_id 为str类型 "
#     print posts.find_one({"_id": str(obj_id)})
#     #可以通过ObjectId方法把str转成ObjectId类型
#     from bson.objectid import ObjectId
#     print "_id 转换成ObjectId类型"
#     print posts.find_one({"_id": ObjectId(str(obj_id))})


def get_many_docs(db):
    #mongo中提供了过滤查找的方法，可以通过各
    #种条件筛选来获取数据集，还可以对数据进行计数，排序等处理
    posts = db.posts
    #所有数据,按年龄排序, -1是倒序
    all = posts.find().sort("age", -1)
    count = posts.count()
    print "集合中所有数据 %s个"%int(count)
    for i in all:
        print i
    #条件查询
    count = posts.find({"name": "lzz"}).count()
    print "lzz: %s"%count
    for i in posts.find({"name": "lzz", "age": {"$lt": 20}}):
        print i


def updatepe(db):
    #修改所有人名称
    db.posts.update({"name": "lzz"}, {"name": "amy"})
    print("==========================================")
    print "myamycount %s"%db.posts.find({"name": "amy"}).count()
    print("==========================================")

def rem(db):
    db.posts.remove({"name": "amy"})

if __name__ == '__main__':
    db = get_db()
    obj_id = insert_one_doc(db)
    obj_ids = insert_mulit_docs(db)
    # get_all_colls(db)
    # get_one_doc(db)
    # get_one_by_id(db)
    get_many_docs(db)
    updatepe(db)
    updatename(db)
    getmama(db)
    rem(db)