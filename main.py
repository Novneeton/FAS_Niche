import json
import os
from flask import Flask, render_template, request, Response, redirect, flash
from werkzeug.utils import secure_filename
from Models import submit_details, populate_data, upload_data

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thenicheproject'


@app.route('/login_api', methods=['POST'])
def login_api():
    userid = request.form['userid']
    password = request.form['password']
    l = [userid, password]
    login_cred, data = submit_details.login(l)
    if login_cred == "Success":
        return_data = {"login": login_cred, "username": data}
        return return_data
    elif login_cred == "Failure":
        return_data = {"login": login_cred}
        return return_data


@app.route('/country_reports_api', methods=['GET'])
def country_reports_api():
    data = populate_data.get_client_data("all")
    return Response(json.dumps(data), mimetype='application/json')


@app.route('/')
def login():
    # generate_report.report()
    return render_template('login.html')


@app.route('/templates/login_data', methods=['POST', 'GET'])
def login_data():
    if 'userid' in request.form.keys():
        userid = request.form['userid']
        password = request.form['password']
        l = [userid, password]
        login_cred, data = submit_details.login(l)
        if login_cred == "Success":
            return render_template('index.html', output_data=data)
        elif login_cred == "Failure":
            data = "Wrong Credentials Entered. Please enter correct password or email_id"
            return render_template('login.html', output_data=data)
    else:
        data = submit_details.login()
        return render_template('index.html', output_data=data)


@app.route('/templates/login_new')
def login_new():
    # generate_report.report()
    return render_template('login_new.html')


@app.route('/templates/get_client_country_data')
def get_client_country_data():
    df = populate_data.client_country_data()
    df = df.to_dict(orient="records")
    return Response(json.dumps(df), mimetype='application/json')


@app.route('/templates/database_data')
def database_data():
    df = populate_data.populate_database()
    df = df.to_dict(orient="records")
    return Response(json.dumps(df), mimetype='application/json')


@app.route('/templates/upload_template', methods=['POST'])
def upload_template():
    if request.method == 'POST':
        try:
            f = request.files['logo']
        except:
            f = request.files['watermark']
        filename = secure_filename(f.filename)
        f.save(os.path.join('./dump_files', filename))
        upload_data.upload_to_database(filename)
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/templates/get_data')
def get_data():
    filename = upload_data.get_data_s3()
    return redirect(filename, code=302)


@app.route('/templates/mail_body')
def mail_body():
    return render_template('mail_body.html')


@app.route('/templates/create_user')
def create_user():
    return render_template('create_user.html')


@app.route('/templates/user_options')
def user_options():
    return render_template('user_options.html')


@app.route('/templates/role_management')
def role_management():
    return render_template('role_management.html')


@app.route('/templates/client_management')
def client_management():
    return render_template('client_management.html')


@app.route('/templates/audit_details')
def audit_details():
    return render_template('audit_details.html')


@app.route('/templates/device_validation')
def device_validation():
    return render_template('device_validation.html')


@app.route('/templates/master_uploads')
def master_uploads():
    data = populate_data.get_client_data("all")
    return render_template('master_uploads.html', output_data=data)


@app.route('/templates/edit_template')
def edit_template():
    return render_template('edit_template.html')


@app.route('/templates/api_test', methods=['GET'])
def api_test():
    name = request.args.to_dict(flat=False)
    output_name = name["'client_name'"][0]
    return output_name


@app.route('/templates/project_management')
def project_management():
    return render_template('project_management.html')


@app.route('/handle_client_data', methods=['POST', 'GET'])
def handle_client_data():
    name = request.form.to_dict(flat=False)
    try:
        if name['meal'][0] == 'New Client':
            return render_template('client.html')
        else:
            return render_template('client_work.html')
    except:
        form_data = request.args.to_dict(flat=False)
        return render_template('client_work.html', output_data=form_data["'client_name'"][0])


@app.route('/client_report', methods=['GET'])
def client_report():
    form_data = request.args.to_dict(flat=False)
    output_name = {"name": form_data["'client_name'"][0]}
    output_name = {"countries": populate_data.get_client_data(output_name)}
    return render_template('client_report.html', output_data=output_name)


@app.route('/handle_role_data', methods=['POST', 'GET'])
def handle_role_data():
    name = request.form.to_dict(flat=False)
    if name['activity'][0] == 'Add New User':
        if name['user'][0] == 'Client':
            return render_template('client.html')

    if name['activity'][0] == 'Edit Previous User':
        if name['user'][0] == 'Client':
            data = [{"user_name": populate_data.get_client_data("name")}, {"role": ["Client"]}]
        if name['user'][0] == 'Supervisor':
            data = [{"user_name": populate_data.get_supervisor_data("name")}, {"role": ["Supervisor"]}]
        if name['user'][0] == 'Auditor':
            data = [{"user_name": populate_data.get_auditor_data("name")}, {"role": ["Auditor"]}]
        # if name['user'][0] == 'user':
        #     data = populate_data.get_user()
        # if name['user'][0] == 'Admin':
        #     data = populate_data.get_admin()
        return render_template('edit_option.html', output_data=data)


@app.route('/populate_table_data', methods=['POST', 'GET'])
def populate_table_data():
    name = request.form.to_dict(flat=False)
    if name['role'][0] == 'Auditor':
        data = populate_data.get_auditor_data("all")
        return render_template('populate_table_data.html', output_data=data)
    if name['role'][0] == 'Client':
        data = name['user_name'][0]
        return render_template('client_work.html', output_data=data)
    if name['role'][0] == 'Supervisor':
        data = populate_data.get_supervisor_data("all")
        return render_template('populate_table_data.html', output_data=data)


@app.route('/handle_data', methods=['POST', 'GET'])
def handle_data():
    file_data = request.files.to_dict(flat=False)
    try:
        if 'logo' in file_data.keys():
            f = request.files['logo']
            filename = secure_filename(f.filename)
            f.save(os.path.join('./dump_files', filename))
            upload_data.upload_to_database(filename)
        if 'watermark' in file_data.keys():
            f = request.files['watermark']
            filename = secure_filename(f.filename)
            f.save(os.path.join('./dump_files', filename))
            upload_data.upload_to_database(filename)
    except:
        pass
    data = request.form.to_dict(flat=False)
    geo = False
    sos = False
    mail = False
    visit = False
    if "geo" in data.keys():
        geo = True
    if "sos" in data.keys():
        sos = True
    if "mail" in data.keys():
        mail = True
    if "visit" in data.keys():
        visit = True
    client_details = {'name': data['fname'][0], 'country': data['country'], 'geo': geo, 'sos': sos, 'mail': mail,
                      'visit': visit, 'db_name': data['project_database_name'][0],
                      "header_band": data['header_band'][0],
                      'button_background': data["button_bg"][0], 'button_foreground': data["button_fg"][0],
                      'background':
                          data['bg'][0], "text": data['txt'][0]}
    post_data = submit_details.client_details_update(client_details)
    if post_data == "Success":
        out_data = {"name": data['fname'][0], "countries": data['country']}
        return render_template('audit_details.html', output_data=out_data)
    else:
        flash(post_data)
        return render_template('client.html')


@app.route('/client_date', methods=['POST', 'GET'])
def client_date():
    data = request.form.to_dict(flat=False)


@app.route('/templates/profile')
def profile():
    # generate_report.report()
    return render_template('profile.html')


@app.route('/templates/templates')
def templates():
    data = populate_data.get_template_data()
    project_data = populate_data.get_project_data()
    auditor_data = populate_data.get_auditor_data()
    data[0]['project_data'] = project_data
    data[0]['auditor_data'] = auditor_data
    return render_template('templates.html', output_data=data)


@app.route('/templates/report_management', methods=['GET'])
def report_management():
    form_data = request.args.to_dict(flat=False)
    data = populate_data.get_report_data(form_data["'client_name'"][0])
    cycle_data = []
    for i in range(int(data[0]['cycles'])):
        cycle_data.append("Cycle " + str(i+1))
    data.append({"cycle_list": cycle_data})
    return render_template('report_management.html', output_data=data)


@app.route('/templates/reports_options', methods=['GET', 'POST'])
def reports_options():
    form_data = request.args.to_dict(flat=False)
    output_name = form_data["'client_name'"][0]
    return render_template('reports.html', output_data=output_name)


@app.route('/templates/visit_options')
def visit_options():
    return render_template('visit_options.html')


@app.route('/templates/select_report')
def select_report():
    return render_template('select_report.html')


@app.route('/templates/filter_details', methods=['GET', 'POST'])
def filter_details():
    data = request.form.to_dict(flat=False)
    form_data = request.args.to_dict(flat=False)
    populate_data.pushData_data(data['report_name'][0], form_data["'client_name'"][0])
    output_name = form_data["'client_name'"][0]
    output_name = output_name.strip()
    return render_template('filter_details.html', output_data=output_name)


@app.route('/templates/assign_role')
def assign_role():
    out_data = populate_data.get_client_data("all")
    return render_template('assign_role.html', output_data=out_data)


@app.route('/templates/assign_role_2', methods=['POST'])
def assign_role_2():
    data = request.form.to_dict(flat=False)
    out_data = populate_data.get_client_data(data)
    # for country_list in out_data:
    #     for countries in country_list:
    #         all_countries
    return render_template('assign_role_2.html', output_data=out_data)


@app.route('/templates/role_options')
def role_options():
    return render_template('role_options.html')


@app.route('/templates/report_options')
def report_options():
    return render_template('report_options.html')


@app.route('/templates/basic_client_table')
def basic_client_table():
    out_data = populate_data.get_client_data("all")
    return render_template('basic_client_table.html', output_data=out_data)


@app.route('/templates/basic_user_table')
def basic_user_table():
    out_data = populate_data.get_role_data()
    return render_template('basic_user_table.html', output_data=out_data)


@app.route('/templates/grid_details', methods=['POST', 'GET'])
def grid_details():
    data = request.form.to_dict(flat=False)
    form_data = request.args.to_dict(flat=False)
    field_data = populate_data.get_report_data(form_data["'client_name'"][0])
    data = {"client_name": form_data["'client_name'"][0], "fields": field_data[0]['fields']}
    return render_template('grid_details.html', output_data=data)


@app.route('/templates/graph_details', methods=['POST'])
def graph_details():
    data = request.form.to_dict(flat=False)
    form_data = request.args.to_dict(flat=False)
    out_data, grids = [], []
    for i in range(len(data['dbase'])):
        grids.append("Grid " + str(i+1))
    out_data.append({'client': (form_data["'client_name'"][0]).strip(), 'grids': grids})
    return render_template('graph_details.html', output_data=out_data)


@app.route('/templates/client_option')
def client_option():
    data = populate_data.get_client("name")
    return render_template('edit_option.html', output_data=data)


@app.route('/charts', methods=['POST'])
def charts():
    return render_template('chartjs.html')


@app.route('/templates/client')
def client():
    return render_template('client.html')


@app.route('/templates/visit_management')
def visit_management():
    form_data = request.args.to_dict(flat=False)
    country_data = populate_data.get_client_data(form_data["'client_name'"][0])
    all_data = populate_data.get_visit_data(form_data["'client_name'"][0])
    output_name = {"name": form_data["'client_name'"][0],
                   "countries": country_data, "all_data": all_data['audit_details']}
    return render_template('visit_management.html', output_data=output_name)


@app.route('/templates/visit_reopen')
def visit_reopen():
    # generate_report.report()
    return render_template('visit_reopen.html')


@app.route('/templates/basic_table')
def basic_table():
    # generate_report.report()
    data = populate_data.get_db_data()
    return render_template('basic_table.html', output_data=data)

if __name__ == '__main__':
    app.run()
