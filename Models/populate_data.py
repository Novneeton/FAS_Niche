import boto3
from pymongo import MongoClient
import pandas as pd

client = MongoClient(
    "mongodb+srv://Novneet:jayhanuman1@cluster0.oxi79.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE")
db = client.FAS


def populate_database():
    cursor = db['projects'].find()
    fetch_data = []
    for doc in cursor:
        fetch_data.append(doc)
    return fetch_data


def get_survey_data():
    cursor = db['surveys'].find()
    fetch_data = []
    for doc in cursor:
        fetch_data.append(doc)
    return fetch_data


def get_template_data():
    cursor = db['template_layouts'].find()
    fetch_data = []
    for doc in cursor:
        fetch_data.append(doc)
    return fetch_data


def get_report_data(formdata):
    formdata = formdata.strip()
    cursor = db['device_db'].find({"client": formdata})
    fetch_data = []
    for doc in cursor:
        fetch_data.append(doc)
    return fetch_data


def get_db_data():
    data = db['users'].find()
    fetched_data = []
    for doc in data:
        fetched_data.append(doc)
    return fetched_data


def pushData_data(report, username):
    username = username.strip()
    data = db['reports'].update_one({"client": username}, {"$set": {"report_name": report}})
    return


def get_auditor_data(option):
    data = db['auditors'].find()
    fetched_data = []
    if option == "name":
        for doc in data:
            fetched_data.append(doc['name'])
    elif option == "all":
        for doc in data:
            fetched_data.append(doc)
    return fetched_data


def get_supervisor_data(option):
    data = db['supervisors'].find()
    fetched_data = []
    if option == "name":
        for doc in data:
            fetched_data.append(doc['name'])
    elif option == "all":
        for doc in data:
            fetched_data.append(doc)
    return fetched_data


def get_client_data(option):
    data = db['client'].find()
    fetched_data = []
    if option == "name":
        for doc in data:
            fetched_data.append(doc['name'])
    elif option == "all":
        for doc in data:
            fetched_data.append(doc)
    elif type(option) is dict:
        for i in option['client']:
            i = i.strip()
            data = db['client'].find_one({"name": i})
            if data:
                fetched_data.append({"client": i, "country": data['country'], "reports": data['reports']})
    else:
        option = option.strip()
        data = db['client'].find_one({"name": option})
        if data:
            fetched_data = data['country']
    return fetched_data


def get_role_data():
    data = db['roles'].find()
    fetched_data = []
    for doc in data:
        fetched_data.append(doc)

    return fetched_data


def get_visit_data(option):
    option = option.strip()
    data = db['client_audit_details'].find_one({"client": option})
    return data


def get_project_data():
    data = db['projects'].find()
    fetched_data = []
    for doc in data:
        fetched_data.append(doc['project'])
    return fetched_data


def fill_data(project, graph):
    df = db['users'].find({"project": project})
    if df:
        for doc in df:
            update_body_query = doc
            update_body_query['graph'] = graph
            update_body = {"$set": update_body_query}
            res = db['users'].update_one({'_id': doc["_id"]}, update_body)
    return "Success"


def get_client(option):
    data = db['client'].find()
    fetched_data = []
    if option == "name":
        for doc in data:
            fetched_data.append(doc['name'])
    else:
        for doc in data:
            fetched_data.append(doc)

    return fetched_data


def client_country_data(option):
    data = db['client'].find()
    fetched_data = []
    for doc in data:
        for i in doc['countries']:
            fetched_data.append({"country": i})

    return fetched_data
