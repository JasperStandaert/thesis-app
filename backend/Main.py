from flask import Flask
from flask import request
import xml.etree.ElementTree as ET
import pandas as pd

app = Flask(__name__)
df = pd.DataFrame(columns=['Name', 'Drug interactions'])


@app.route('/')
def index():
    return 'Default Page of backend'


@app.route("/druginteractionshtml", methods=['GET'])
def druginteractionshtml_api():
    return df.to_html()


@app.route("/druginteractionsjson", methods=['GET'])
def druginteractionsjson_api():
    return df.to_json(orient='records')

#Get Specific drug info
@app.route("/query", methods=['GET'])
def getDrugInfo():
   args = request.args
   df.loc[df['Name'] == args]



def get_info():
    tree = ET.parse('/Users/stand/OneDrive/BureauBlad/Thesis/Thesis/data/database_shrunk.xml')
    root = tree.getroot()

    pos = 0
    h = []
    for drug in root:
        l = []
        name = drug.find('{http://www.drugbank.ca}name').text
        h.append(name)
        interactions = drug.find('{http://www.drugbank.ca}drug-interactions')
        for i in interactions:
            for j in i:
                descriptions = []
                if j.tag == '{http://www.drugbank.ca}name':
                    descriptions.append(j.text)
                #if j.tag == '{http://www.drugbank.ca}interaction':
                #    descriptions.append(j.text)
                l.append(descriptions)
        h.append(l)
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

app.run()

@app.route("/get_drugs", methods=['GET'])
def get_drugs():
    # Hier alle drugs binnenhalen

@app.route("/get_drug", methods=['GET'])
def get_drug(drug):
    # Hier de info van de gevraagde drug meepakken

@app.route("/add_drug", methods=['POST'])
def add_drug(drug, patient_id):
    # Hier post call om drug toe te voegen aan patient

@app.route("/remove_drug", methods=['POST'])
def remove_drug(drug, patient_id):
    # Hier post om drug te verwijderen van patient

@app.route("/add_patient", methods=['POST'])
def add_patient():
    # Hier patient toevoegen

@app.route("/remove_patient", methods=['POST'])
def remove_patient(patient_id):
    # Hier patient verwijderen

@app.route("/get_interactions", methods=['GET'])
def get_interactions(drugs):
    # Hier kijken voor interacties in de lijst

@app.route("/post_search", methods=['POST'])
def post_search(searchdata):
    # Hier search query returnen