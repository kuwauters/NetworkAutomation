from flask import Flask, render_template
import json

work_dir = '/home/kurt/NetworkAutomation/NetworkAutomation/datamodel/'
js_file = 'inventory.json'


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])

def hello():
    json_data = json.load(open(work_dir + js_file))
    return render_template('epl.html',hosts=json_data)

def contact():
    if request.method=='POST':
        if request.form['submit'] == 'build_epl':
            print 'button works'
        else:
            print 'button does not work'
if __name__ == "__main__":
    app.run()
