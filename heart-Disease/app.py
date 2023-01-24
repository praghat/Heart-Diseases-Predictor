from flask import Flask, render_template,request
import numpy as np
import pickle

#creating constructor
app=Flask(__name__, template_folder='template',static_folder='static')
model=pickle.load(open('./model/model.pickle', 'rb'))
# print(model)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''v1 = request.form['age']
    v2 = request.form['bp']
    v3 = request.form['chol']
    v4 = request.form['bs']
    v5 = request.form['ecg']
    v6 = request.form['ca']
    v7 = request.form['thal']'''

    features = [int(x) for x in request.form.values()]
    final_feature = [np.array(features)]
    pred = model.predict(final_feature)

    out = pred

    
    if int(out)== 1:
        predi ='Yes,your heart needs care!!!!Please do consult the Doctor'
    else:
        predi ='Hurray!!!!Your heart is hale and healthy'            
    return render_template("ans.html", prediction = predi)



if __name__ == '__main__':
    app.run(debug=True)