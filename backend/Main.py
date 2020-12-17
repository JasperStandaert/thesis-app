from flask import Flask
from flask import request
import pandas as pd
import xml.etree.ElementTree as ET
from structure.Drug import Drug
from structure.Interaction import Interaction
from structure.Patient import Patient
from structure.Product import Product

app = Flask(__name__)
df = pd.DataFrame(columns=['Name', 'Description', 'indication', '' 'Drug interactions'])
drugs = []


@app.route('/')
def index():
    return '<h1>Index Page</h1>'


@app.route("/druginteractionshtml")
def druginteractionshtml_api():
    return df.to_html()


@app.route("/druginteractionsjson", methods=['GET'])
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
        p = []
        name = drug.find('{http://www.drugbank.ca}name').text
        h.append(name)
        desc = drug.find('{http://www.drugbank.ca}description').text
        h.append(desc)
        indication = drug.find('{http://www.drugbank.ca}indication').text
        h.append(indication)
        interactions = drug.find('{http://www.drugbank.ca}drug-interactions')
        for i in interactions:
            for j in i:
                if j.tag == '{http://www.drugbank.ca}name':
                   intName = j.text
                if j.tag == '{http://www.drugbank.ca}description':
                    intDesc = j.text
                interaction = Interaction(intName, intDesc)
                l.append(interaction)
        h.append(l)
        products = drug.find('{http://www.drugbank.ca}products')
        for p in products:
            for j in p:
                if j.tag == '{http://www.drugbank.ca}name':
                    productName = j.text
                if j.tag == '{http://www.drugbank.ca}dosage-form':
                    dosage = j.text
                if j.tag == '{http://www.drugbank.ca}strength':
                    strength = j.text
                if j.tag == '{http://www.drugbank.ca}route':
                    route = j.text
                prod = Product(productName, dosage, strength, route)
                p.append(prod)
        h.append(p)


        # l = []
        # interactions = drug.find('{http://www.drugbank.ca}food-interactions')
        # for i in interactions:
        #     for j in i:
        #         if j.tag == '{http://www.drugbank.ca}name':
        #             l.append(j.text)
        # h.append(l)
        df.loc[pos] = h
        h = []
        pos += 1

    print(df.head())

    # result = df.to_json(orient="split")
    # parsed = json.loads(result)
    # return json.dumps(parsed, indent=4)
    # return df


@app.before_first_request
def test():
    get_info()
    print("collected")