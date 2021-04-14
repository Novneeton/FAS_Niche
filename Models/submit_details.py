from pymongo import MongoClient

client = MongoClient("mongodb+srv://Novneet:jayhanuman1@cluster0.oxi79.mongodb.net/test")
db = client.FAS


def details(form_data):
    """
    name = request.form['fname']
    address1 = request.form['address1']
    address2 = request.form['address2']
    address3 = request.form['address3']
    city = request.form['city']
    country = request.form['country']
    supervisor_id = request.form['supervisorID']
    password = request.form['password']
    mail = request.form['mail']
    :param form_data:
    :return:
    """
    if form_data[6] != '':
        insert_text = {"name": form_data[0],
                       "address": form_data[1] + form_data[2] + form_data[3],
                       "city": form_data[4], 'country': form_data[5], 'supervisor_id':
                           form_data[6], 'password': form_data[9], 'email': form_data[10]}
        db['supervisors'].insert_one(insert_text)
    elif form_data[7] != '':
        insert_text = {"name": form_data[0],
                       "address": form_data[1] + form_data[2] + form_data[3],
                       "city": form_data[4], 'country': form_data[5], 'supervisor_id':
                           form_data[7], 'password': form_data[9], 'email': form_data[10]}
        db['auditors'].insert_one(insert_text)
    else:
        insert_text = {"name": form_data[0],
                       "address": form_data[1] + form_data[2] + form_data[3],
                       "city": form_data[4], 'country': form_data[5], 'supervisor_id':
                           form_data[8], 'password': form_data[9], 'email': form_data[10]}
        db['client'].insert_one(insert_text)


def login(form_data):
    """
    name = request.form['fname']
    password = request.form['password']
    :param form_data:
    :return:
    """
    doc = db['admins'].find_one({"user": form_data[0], "password": form_data[1]})
    if doc:
        return "Success"
    else:
        return "Failure"
