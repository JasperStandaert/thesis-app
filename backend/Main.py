from flask import Flask
from flask import request
import xml.etree.ElementTree as ET
import pandas as pd

app = Flask(__name__)
df = pd.DataFrame(columns=['Name', 'Drug interactions'])


@app.route('/')
def index():
    return '<h1>Index Page</h1>'


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