from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return null

@app.route('/trigger_report')
def trigger_report():
    createreport()
    return 729381012929


@app.route('/get_report/<reportid>')
def get_report(report_id):
    
    return "Incomplete"


def createreport()
# Function to create report
app.run(debug=True)
