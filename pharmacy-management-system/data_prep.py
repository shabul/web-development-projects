import pandas as pd
from datetime import datetime
import pickle

import random

def gen_dob(count):
    op = []
    for c in range(count):
        x = datetime.strptime(str( random.choice(range(1,27))) +"/"+ str( random.choice(range(1,12))) + "/" + str( random.choice(range(1973,2022))) , '%d/%m/%Y').date()
        op.append(x)
    return op


def gen_app_date(count):
    op = []
    for c in range(count):
        x = datetime.strptime( str( random.choice(range(1,12))) + "/" + str( random.choice(range(2023,2024))) , '%m/%Y').date()
        op.append(x)
    return op


def gen_app_time(count):
    op = []
    for c in range(count):
        x = datetime.strptime(str( random.choice(range(0,23))) +":"+ str( random.choice(range(0,59)))  , '%H:%M').time()
        op.append(x)
    return op



def gen_room_type(count):
    return [random.choice(['AC','Non AC','ICU',"General"]) for c in range(count)]



def gen_ins_type(count):
    return [random.choice([True,False]) for c in range(count)]




def gen_minor(count):
    return [random.choice([True,False]) for c in range(count)]




def gen_accident(count):
    return [random.choice([True,False]) for c in range(count)]


def gen_gender(count):
    return [random.choice(['Male','Female']) for c in range(count)]


def gen_emp_type(count):
    return [random.choice(['Business','Private Employee','Govt Employee']) for c in range(count)]



def gen_units(count):
    return [random.choice(range(10,1000)) for c in range(count)]


def gen_price(count):
    return [random.choice(range(1,80)) for c in range(count)]


def gen_disc(count):
    return [random.choice(range(1,75)) for c in range(count)]


def gen_batchid(count):
    return [str(random.choice(range(15454542,45465465120)))  for c in range(count)]


# def gen_batchid(count):
#     l = ["Diabetes","Blood Pressure","Thyroid","Asthma","Cancer","Heart Disease"]
    
#     return [",".join(random.sample(l, random.choice([1,2,3,4,5])))  for c in range(count)]







## Insert into DB\

from utils.models import db, Users,Meds



    


app_data = pd.DataFrame()
count = 35

app_data['med_name'] = ['Lignocaine HCl injection I.P 1%',
 'Lignocaine +nifedipine ointment',
 'Prilocaine lignocaine',
 'Alprazolam tab I.P 0.25 mg,',
 'Alprazolam tab I.P 0.5 mg',
 'Amitriptyline tab I.P 10 mg',
 'Midazolam',
 'Midazolam nasal spray 5mg/ml',
 'Propantheline tab 15 mg',
 'Paracetamol suppository 100 mg',
 'Paracetamol inj 500 mg',
 'Paracetamol tab 650 mg',
 'Paracetamol tab 1000 mg',
 'Paracetamol drops 100 mg/ml',
 'Diclofenac sodium spray',
 '"Diclofenac sodium +',
 '10mg)"',
 'Diclofenac potassium tab 75 mg,',
 'Diclofenac potassium tab 100 mg',
 'Diclofenac potassium gel 1 %',
 'Piroxicam',
 'Piroxicam Tab I.P',
 'Mefenamic acid syr 100 mg/5ml',
 'Mefenamic acid DT 500 mg',
 'Mefenamic acid spray',
 'Mefenamic acid capsules I.P 250 mg',
 'Aceclofenac gel',
 'Serratiopeptidase I.P',
 'Lornoxicam tab 8 mg,',
 'Lornoxicam tab 4 mg',
 'Etoricoxib tab 60 mg,',
 'Etoricoxib tab 90mg,',
 'Etoricoxib tab 120 mg',
 'Tramadol tab 50 mg,',
 'Tramadol inj 100 mg/ml',
 ]

app_data['price'] = gen_price(count)

app_data['batch_id'] = gen_batchid(count)

app_data['units'] = gen_units(count)
app_data['exp_date'] = gen_app_date(count)

app_data['discount'] = gen_disc(count)



def med_data_ingestion():
    for i in app_data.to_dict(orient=('records')):
        rec =Meds(
                    med_name=i['med_name'],
                    price=i['price'],
                    batch_no  =i[ 'batch_id'],
                    units_avbl =i[ 'units'],
                    exp_date =i['exp_date'],
                    discount =i['discount'],
                    
                )



        db.session.add(rec)
        db.session.commit()
        
    return "Added data to Meds DB"
    
 