from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String

#Flaskの立ち上げ
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///flask.sqlite'#DBへの絶対パス

#SQLAlchemyでデータベース定義
db = SQLAlchemy(app)

#SQLiteのDBテーブル情報 #ID,YOURNAME,AGEのカラム作成
class FLASKDB(db.Model):
    __tablename__ ='flask_table'
    ID=db.Column(Integer, primary_key=True)
    YOURNAME = db.Column(String(32))
    AGE=db.Column(Integer)

#DBの作成

db.create_all()

#127.0.0.1:5000に遷移したときの処理

@app.route('/')
def rroute():
    return render_template('index.html')

#127.0.0.1/DBINFO0:5000に遷移したときの処理
@app.route('/DBINFO',methods=['POST','GET'])
def bokinbox():
    if request.method == 'POST':
        yourname = request.form['yourname']
        age = request.form['age']
        flask = FLASKDB(YOUNAME=yourname,AGE=age)
        db.session.commit()
        db.session.close()
        FLASKDB_infos=db.session.query(FLASKDB.ID,FLASKDB.YOURNAME,FLASKDB.AGE).all()
        return render_template('db_info.html',FLASKDB_infos=FLASKDB_infos)

#python app立ち上げ
if __name__ == '__main__':
    app.run()