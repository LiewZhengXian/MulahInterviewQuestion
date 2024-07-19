from flask import Flask, render_template, jsonify
import csv
import os
app = Flask(__name__)

def read_csv():
    data = []
    csv_path = os.path.join(app.root_path,'Table_Input.csv')
    with open(csv_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    data = read_csv()
    return jsonify(data)

if __name__ == '__main__':
    app.run()