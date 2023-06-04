from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, world!'

@app.route('/trigger_report')
def trigger_report():
    return "hello"


@app.route('/get_report/<reportid>')
def get_report(report_id):
    return report_id
app.run(debug=True)