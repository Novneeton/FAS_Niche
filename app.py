from flask import Flask, render_template, request
from Models import submit_details

# from scripts import generate_report
app = Flask(__name__)


@app.route('/login')
def login():
    # generate_report.report()
    return render_template('login.html')


@app.route('/create')
def account():
    # generate_report.report()
    return render_template('create_account_1.html')


@app.route('/index')
def home():
    # generate_report.report()
    return render_template('index.html')


@app.route('/submit_details')
def submission():
    # generate_report.report()
    submit_details.details()


@app.route('/login_data', methods=['POST', 'GET'])
def login_data():
    userid = request.form['userid']
    password = request.form['password']
    l = [userid, password]
    login_cred = submit_details.login(l)
    if login_cred == "Success":
        return render_template('index.html')


@app.route('/handle_data', methods=['POST', 'GET'])
def handle_data():
    name = request.form['fname']
    address1 = request.form['address1']
    address2 = request.form['address2']
    address3 = request.form['address3']
    city = request.form['city']
    country = request.form['country']
    try:
        supervisor_id = request.form['supervisorID']
    except:
        supervisor_id = ''
    try:
        auditor_id = request.form['auditorId']
    except:
        auditor_id = ''
    try:
        client_id = request.form['clientId']
    except:
        client_id = ''
    password = request.form['password']
    mail = request.form['mail']
    l = [name, address1, address2, address3, city, country, supervisor_id, auditor_id, client_id, password, mail]
    submit_details.details(l)
    if supervisor_id != "":
        return render_template('supervisor.html')
    if auditor_id != "":
        return render_template('auditor.html')
    if client_id != "":
        return render_template('client.html')


@app.route('/create_collection')
def create_collection():
    # generate_report.report()
    return render_template('create_collection.html')


@app.route('/profile')
def profile():
    # generate_report.report()
    return render_template('profile.html')


@app.route('/auditor_index')
def auditor_index():
    # generate_report.report()
    return render_template('auditor_index.html')


@app.route('/supervisor_index')
def supervisor_index():
    # generate_report.report()
    return render_template('supervisor_index.html')


@app.route('/templates')
def templates():
    # generate_report.report()
    return render_template('templates.html')


@app.route('/reports')
def reports():
    # generate_report.report()
    return render_template('reports.html')


@app.route('/reports_view')
def reports_view():
    # generate_report.report()
    return render_template('reports_view.html')


@app.route('/client')
def client():
    # generate_report.report()
    return render_template('client.html')


@app.route('/client_index')
def client_index():
    # generate_report.report()
    return render_template('client_index.html')


@app.route('/auditor')
def auditor():
    # generate_report.report()
    return render_template('auditor.html')


@app.route('/supervisor')
def supervisor():
    # generate_report.report()
    return render_template('supervisor.html')


@app.route('/basic_table')
def basic_table():
    # generate_report.report()
    return render_template('basic_table.html')


@app.route('/verify', methods=["POST"])
def verify():
    email = request.form["email"]
    msg = Message('OTP', sender='username@gmail.com', recipients=[email])
    msg.body = str(otp)
    mail.send(msg)


@app.route('/validate', methods=["POST"])
def validate():
    user_otp = request.form['otp']
    if otp == int(user_otp):
        return "<h3> Email  verification is  successful </h3>"
        return "<h3>failure, OTP does not match</h3>"


if __name__ == '__main__':
    app.run()
