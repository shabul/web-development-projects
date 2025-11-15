from flask import Blueprint, url_for, render_template, redirect, request,jsonify
from flask_login import LoginManager,login_required
from werkzeug.security import generate_password_hash
import sqlalchemy
from utils.models import db, Meds
from pytz import timezone
from datetime import datetime,date
from utils.dashboard import row2dict


UTC = timezone('UTC')

def time_now():
    return datetime.now(UTC)


buy_medicine = Blueprint('buy_medicine', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(buy_medicine)

@buy_medicine.route('/buy_medicine_api', methods=['GET', 'POST'])
@login_required
def show():
    if True:
        x = request.args.get('res')
        print(x)
        patient_name  = request.args.get('pname') #'shsssvsgsj'   
        dob  =  datetime.strptime(request.args.get('dob'), '%Y-%m-%d').date()  
        gender  =   request.args.get('gender') #'Male'  
        room_type  =  request.args.get('roomType') #'AC'   
        insurance  =  bool(request.args.get('insurance')) #True   
        emp_type  =    request.args.get('emp_type') #'Givt' 
        contact_person  =  request.args.get('contact_person') #'shasssb'   
        phone_number  =   request.args.get('contact_person_number') #'7897'  
        dr_name  =  request.args.get('dr_name') #'jhghjfd'  
        admit_date  =  datetime.strptime(request.args.get('admit_date'), '%Y-%m-%d').date()  
        admit_time  =  datetime.strptime(request.args.get('admit_time'), '%H:%M').time()   
        minor  = bool(request.args.get('minor')) #True   
        accident  = bool(request.args.get('accident')) # False   
        print(10*"==")
        print(admit_date,admit_time,insurance)
        print(type(admit_date),type(admit_time),type(insurance))

        try:
            new_user = InPatientsData(
                patient_name  =patient_name     ,
                dob  = dob    ,
                gender  = gender    ,
                room_type  = room_type    ,
                insurance  =    insurance ,
                emp_type  =    emp_type ,
                contact_person  = contact_person    ,
                phone_number  =     phone_number,
                dr_name  =  dr_name   ,
                admit_date  =   admit_date  ,
                admit_time  = admit_time    ,
                minor  =    minor ,
                accident  =  accident   ,
            )

            db.session.add(new_user)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return jsonify({"inpatient_res":'Entered Data Already exists or mismatches with the format it takes.<br> Kindly Re-check all fields and Book again.'})

        inpatient_id_from_db = InPatientsData.query.filter_by(patient_name=patient_name).first().patient_id

        
        inpatient_reference ={}
        inpatient_reference['id'] = inpatient_id_from_db
        # appointment_reference['pname'] = pname
        # appointment_reference['doctor_name'] = doctorname
        # appointment_reference['time'] = date_time_appoinement
        print(inpatient_reference)

        # flash("Added Successfully")
        return jsonify({"inpatient_res":'Inpatient Data has been entered for {} at {} on {} with {}.<br> Inpataient ID for reference is {}<br> Thank you'.format(patient_name,admit_time,admit_date,dr_name,inpatient_id_from_db)})

    else:
        return jsonify({"inpatient_res": "Failed"})




@buy_medicine.route('/get_list_of_medicines', methods=['GET', 'POST'])
@login_required
def list_of_meds():

    db_data = Meds.query.all()

    
    meds_list = []
    for pat in db_data:
        meds_list.append(row2dict(pat))
    meds=[]
    for i in meds_list:
        meds.append(i['med_name'])

    return jsonify(meds)


@buy_medicine.route('/get_price_of_medicines', methods=['GET', 'POST'])
@login_required
def get_price_of_medicines_api():

    data  = request.get_json(force=True)
    mname = data['mname']
    units = data['units']

    print(mname,"----------")
    db_data = Meds.query.filter_by(med_name=mname).first()

    price = db_data.price

    exp_date = db_data.exp_date

    units_avbl = db_data.units_avbl

    disc = db_data.discount
    print(price,disc,units)


    if date.today() <= exp_date:
        if int(units) <= units_avbl:
            print("units",int(units),units_avbl)
            final_price = (int(units) * price) * (100 - disc)/100

            text = 'Medicine Name : {} <br> Expiry Date : {} <br> Price per unit : {} <br> Discount : {}% <br> Total Price : <b>{}<b><br><br>'.format(mname,exp_date,price,disc,final_price)


            return jsonify({"response" : 'true',
                            "data" :  text})
        else:
            return jsonify({"response" : 'false',
            "data"  : units+" units are not available in "+mname})
    else:
        return jsonify({"response" :'false',
        "data" : "Medicine got expired"})






@buy_medicine.route('/update_units', methods=['GET', 'POST'])
@login_required
def update_units():
    data  = request.get_json(force=True)
    mname = data['mname']
    units_from_user = int(data['units'])

    units = Meds.query.filter_by(med_name=mname).first().units_avbl
    
    db_data = Meds.query.filter_by(med_name=mname).first()


    db_data.units_avbl = units - units_from_user

    db.session.commit()


    


    return jsonify({"response" : "Thanks for buying "+mname+ "<br> More units available : "+str(db_data.units_avbl)+"<br> Refresh the page to buy again"})
    
    

