# app.py
from flask import Flask, render_template, request, jsonify, send_file
import requests
import os
import subprocess

app = Flask(__name__, static_url_path='/static')

UPLOAD_FOLDER= 'uploads'
ONTOLOGY_FOLDER= 'ontologies'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ONTOLOGY_FOLDER'] = ONTOLOGY_FOLDER

ALLOWED_EXTENSIONS ={'yaml', 'json'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def root():
    return render_template('root.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file and allowed_file(file.filename):
        filename = file.filename 
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        outputFilename = os.path.splitext(os.path.basename(filename))[0]+'.ttl'
        outputFilePath = os.path.join(app.config['ONTOLOGY_FOLDER'], outputFilename)
        file.save(filepath)
        try:
            res = subprocess.run(['java', '-jar', 'openapi_ontology_converter.jar', filepath, app.config['ONTOLOGY_FOLDER']], check=True, capture_output=True, text=True)
            if os.path.isfile(outputFilePath):
                # return jsonify({
                #     "stdout": res.stdout,
                #     "stderr": res.stderr
                # }), 200
                return send_file(outputFilePath, as_attachment=True)
        except subprocess.CalledProcessError as e:
            return jsonify({
                "error": "Server could not process file. Check the file for inconsistencies"
                }), 500
        return 200
    else:
        return jsonify({
            "error": "Wrong input file format (use .yaml or .json formats)"
        }), 406

@app.route('/importtodatabase', methods=['POST'])
def handle_uploaded_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    else:
        forward_url = 'http://172.20.0.6:7200/repositories/main/statements'
        file_content = file.read()
        response = requests.post(
            forward_url,
            headers={'Content-Type': 'text/turtle'},
            data=file_content
        )
        if(response.status_code == 204):
            return jsonify({"message":"File successfully imported to GraphDB"}), 200
        else:
            return jsonify({"message":"File could not be imported to GraphDB"}), 500
    
    

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)