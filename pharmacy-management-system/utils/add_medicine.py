from flask import Blueprint, url_for, render_template, redirect, request,flash,jsonify
from flask_login import LoginManager,login_required
from werkzeug.security import generate_password_hash
import sqlalchemy
from utils.models import db, Meds
from pytz import timezone
import datetime

UTC = timezone('UTC')

def time_now():
    return datetime.now(UTC)


add_medicine = Blueprint('add_medicine', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(add_medicine)

@add_medicine.route('/add_medicine_api', methods=['GET', 'POST'])
@login_required
def show():
    # if request.method == 'POST':
    if True ==True:
        med_name = request.args.get('mname')
        price = request.args.get('price')
        batch_id = request.args.get('batchID')
        units_avbl = request.args.get('units')
        discount = request.args.get('disc')
        exp_date =datetime.datetime.strptime(request.args.get('expDate'), '%Y-%m').date()
        print(10*"==")
        print(exp_date)
        print(type(exp_date))
        try:
            new_user = Meds(
                med_name=med_name,
                price=price,
                batch_no  = batch_id,
                units_avbl = units_avbl,
                discount = discount,
                exp_date = exp_date,
            )

            db.session.add(new_user)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return jsonify({"appoint_res":'Entered Data Already exists or mismatches with the format it takes.<br> Kindly Re-check all fields and Book again.'})

        med_id_from_db = Meds.query.filter_by(med_name=med_name).first().med_id

        
        med_reference ={}
        med_reference['id'] = med_id_from_db
        med_reference['med_name'] = med_name
        
        print(med_reference)
        # flash('Successfully booked med')
        return jsonify({"appoint_res":'{} Medicine has been added in our DB with {} ID.<br> Thank you'.format(med_name,med_id_from_db)})
    
    else:
        return jsonify({"appoint_res":"Failed"})