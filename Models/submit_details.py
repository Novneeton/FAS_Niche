from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb+srv://Novneet:jayhanuman1@cluster0.oxi79.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE")
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
    db['client'].insert_one(form_data)
    return "Success"


def client_details_update(form_data):
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
    doc = db['client'].find()
    for res in doc:
        if form_data['name'] == res['name']:
            return "Client Already Added"
    db['client'].insert_one(form_data)
    return "Success"


def login(form_data=None):
    # """
    # name = request.form['fname']
    # password = request.form['password']
    # :param form_data:
    # :return:
    # """
    if form_data:
        doc = db['users'].find_one({"_id": form_data[0], "password": form_data[1]})
        if doc:
            client_count = db['client'].count()
            template_count = db['template_layout'].count()
            report_count = db['report_count'].count()
            data = {"name": doc['name'], "client_count": client_count, "template_count": template_count,
                    "report_count": report_count}
            return "Success", data
        else:
            return "Failure", "NULL"
    else:
        client_count = db['client'].count()
        template_count = db['template_layouts'].count()
        report_count = db['reports'].count()
        data = {"client_count": client_count, "template_count": template_count,
                "report_count": report_count}
        return data
