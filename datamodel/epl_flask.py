from flask import Flask, render_template
import json

work_dir = '/home/kurt/NetworkAutomation/NetworkAutomation/datamodel/'
js_file = 'inventory.json'


app = Flask(__name__)

@app.route("/")
def hello():
    json_data = json.load(open(work_dir + js_file))
    return render_template('epl.html',hosts=json_data)

if __name__ == "__main__":
    app.run()
