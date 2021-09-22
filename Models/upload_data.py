import os
import boto3
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://Novneet:jayhanuman1@cluster0.oxi79.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE")
db = client.FAS


def upload_to_database(filename, upload_type=None):
    data = db['creds'].find_one()
    s3_bucket = 'niche-fas'
    s3 = boto3.resource(
        service_name='s3',
        region_name='ap-south-1',
        aws_access_key_id=data['aws_access_key_id'],
        aws_secret_access_key=data['aws_secret_access_key']
    )
    file_content = open(os.path.join('./dump_files', filename), 'rb')
    if upload_type == 'template':
        s3.Bucket(s3_bucket).put_object(Key="/template/" + filename, Body=file_content)
        object = s3.Bucket(s3_bucket).Object("/template/" + filename)
        object.Acl().put(ACL='public-read')
        # convert_data("/template/" + filename)
        return filename
    else:
        s3.Bucket(s3_bucket).put_object(Key="" + filename, Body=file_content)
        object = s3.Bucket(s3_bucket).Object(filename)
        object.Acl().put(ACL='public-read')
        # convert_data(filename)


def get_data_s3():
    s3 = boto3.resource(
        service_name='s3',
        region_name='ap-south-1',
        aws_access_key_id='AKIAUOOE62N2GCX6J65F',
        aws_secret_access_key='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'
    )
    my_bucket = s3.Bucket('fas-niche')
    unsorted = []
    for file in my_bucket.objects.filter():
        unsorted.append(file)
    last_file = unsorted[0]
    for i in range(1, len(unsorted)):
        if unsorted[i].last_modified > last_file.last_modified:
            last_file = unsorted[i]

    return "https://fas-niche.s3.ap-south-1.amazonaws.com/" + last_file.key
