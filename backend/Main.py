from flask import Flask
from flask import request
from flask import json
from flask import make_response
import pandas as pd
import xml.etree.ElementTree as ET
from structure.Drug import Drug
from structure.Interaction import Interaction
from structure.Patient import Patient
from structure.Product import Product

app = Flask(__name__)

df = pd.DataFrame(columns=['Name', 'Description', 'Indication', 'Interactions', 'Products'])

drugs1 = []
drugs2 = []
drugs3 = []
patient1 = Patient("Jansenss", "Marc", 48, "Pancreatitis", drugs1)
patient2 = Patient("Kimpen", "Robbe", 23, "Luiheid", drugs2)
patient3 = Patient("Jacobs", "An", 32, "Diabetes", drugs3)

patients = [patient1, patient2, patient3]

@app.route('/')
def index():
    return '<h1>Thesis backend :)</h1>'

@app.route("/drugs")
def druginteractionshtml_api():
    return df.to_html()

@app.route("/drugsjson", methods=['GET'])
def druginteractionsjson_api():
    return df.to_json(orient='records')

@app.route("/query")
def getDrugInfo():
   args = request.args
   print(args)

@app.route("/Patient/<int:patient_id>")
def getPatientDrugs(patient_id):
    if(patients[patient_id]):
        data = []
        for drug in patients[patient_id].medication:
            data.append(drug.__dict__)

        response = make_response(json.dumps(data))
        return response

@app.route("/Patient/Interactions/<int:patient_id>")
def getPatientInteractions(interactions):
    data = []
    for interaction in interactions:
        i = {
            'drug1': interaction.drugA,
            'drug2': interaction.drugB,
            'description': interaction.description
        }
        data.append(i)
                
        response = make_response(json.dumps(data))
        return response
@app.route("/search")
def searchDrug(drugName):
    drug = []
    if(drugName in df):
        drug.append(df.loc[drugName])

    response = make_response(json.dumps(drug))
    return response



def get_info():
    tree = ET.parse('/Users/stand/OneDrive/BureauBlad/Thesis/Thesis/data/database_shrunk.xml')
    root = tree.getroot()

    pos = 0 
    h = []
    for drug in root:
        l = []
        x = []
        name = drug.find('{http://www.drugbank.ca}name').text
        h.append(name)
        desc = drug.find('{http://www.drugbank.ca}description').text
        h.append(desc)
        indication = drug.find('{http://www.drugbank.ca}indication').text
        h.append(indication)

        # Retrieve interactions
        interactions = drug.find('{http://www.drugbank.ca}drug-interactions')
        if(interactions):
            for i in interactions:
                for j in i:
                    intName = ""
                    intDesc = ""
                    if j.tag == '{http://www.drugbank.ca}name':
                        intName = j.text
                    if j.tag == '{http://www.drugbank.ca}description':
                        intDesc = j.text
                    interaction = Interaction(name, intName, intDesc)
                    l.append(interaction)
        else:
            l.append(0)

        h.append(l)
        products = drug.find('{http://www.drugbank.ca}products')
        if(products):
           for p in products:
               for j in p:
                   productName = ""
                   dosage = ""
                   strength = ""
                   route = ""
                   if j.tag == '{http://www.drugbank.ca}name':
                        productName = j.text
                   if j.tag == '{http://www.drugbank.ca}dosage-form':
                        dosage = j.text
                   if j.tag == '{http://www.drugbank.ca}strength':
                        strength = j.text
                   if j.tag == '{http://www.drugbank.ca}route':
                        route = j.text
                   prod = Product(productName, dosage, strength, route)
               x.append(prod)
        else:
            x.append(0)
        h.append(x)

        df.loc[pos] = h
        h = []
        pos += 1

@app.before_first_request
def init():
    get_info()
    print("collected")

app.run()