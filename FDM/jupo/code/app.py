from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd

# df=pd.read_csv("cluster_house123.csv")
# model=df.drop(['ID'],axis=1)

app=Flask(__name__)
model=pickle.load(open('sample61123.pkl','rb'))


@app.route('/')
def man():
    return render_template('home.html')



@app.route('/predict',methods=['POST'])
def home():

    data12=request.form['val12']
    data13=request.form['val13']
    data14=request.form['val14']
    data15=request.form['val15']
    data16=request.form['val16']
    data17=request.form['val17']
    data18=request.form['val18']
    arr=np.array([[data12,data13,data14,data15,data16,data17,data18]])
    pred=model.predict(arr)

    return render_template('after.html',data=pred)


if __name__=="__main__":
    app.run(debug=True)