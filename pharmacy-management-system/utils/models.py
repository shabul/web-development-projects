from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String)





class Meds(UserMixin,db.Model):
    med_id =db.Column(db.Integer, db.Sequence('seq_reg_id', start=1000, increment=1),primary_key=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    med_name = db.Column(db.String(25))
    price = db.Column(db.Integer)
    batch_no = db.Column(db.String(10))
    units_avbl = db.Column(db.Integer)
    exp_date = db.Column(db.Date)
    discount = db.Column(db.Integer)




## Age =- PIE chart
## Inpatient - Count - 2 cards

## docotr and his appoitments - bar chart - count of appoitments

