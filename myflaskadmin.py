#coding: utf8
from flask import Flask, url_for
from flask.ext.admin import Admin, BaseView, expose


class myview(BaseView):
    @expose('/')
    def getindex(self):
        url = url_for('.test')
        return self.render('index.html', url=url)


    @expose('/test/')
    def test(self):
        return self.render('test.html')

app = Flask(__name__)
admin = Admin(app)
admin.add_view(myview(name='hello'))
admin.add_view(myview(name='hello1', endpoint='a', category='fello'))
admin.add_view(myview(name='hello2', endpoint='a1', category='fello'))
admin.add_view(myview(endpoint='testadmin'))
# url_for('testadmin.index')
app.run()