from flask import Flask
from flask import request
import pandas as pd
import xml.etree.ElementTree as ET
from structure.Drug import Drug
from structure.Interaction import Interaction
from structure.Patient import Patient
from structure.Product import Product

app = Flask(__name__)

df = pd.DataFrame(columns=['Name', 'Description', 'Indication', 'Interactions', 'Products'])

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