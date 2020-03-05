import pickle
import sys
import ast
import pandas as pd
import json
import mysql.connector


as_object = eval(sys.argv[1])

mlflag = as_object["Ml"]
flag = as_object["flag"]

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="venky",
    port=3306,
    database="notebook"
)
mycursor = mydb.cursor()

if flag == 'flagDate':
    query = """SELECT Id,V1,V2,v3,V4,V5,V6,V7,V8,V9,V10,v11,V12,V13,V14,V15,V16,V17,V18,v19,V20,V21,V22,V23,V24,V25,V26,v27,V28,nAmount,nTime  FROM creditcard2 where  PDate = %s  """
    dateexa = (as_object["PDate"],)

elif flag == 'flagId':
    query = " ""SELECT Id,V1,V2,v3,V4,V5,V6,V7,V8,V9,V10,v11,V12,V13,V14,V15,V16,V17,V18,v19,V20,V21,V22,V23,V24,V25,V26,v27,V28,nAmount,nTime  FROM creditcard2 where Id = %s  """
    dateexa = (as_object["Id"],)

else:
    print("please enter correct Id or Date")

mycursor.execute(query, dateexa)
myresult = mycursor.fetchall()

modelprediction = []
data = []

loaded_model = pickle.load(
    open(r'E:\\testing\\MachineLearning\\creditcard.pkl', 'rb'))
loaded_model1 = pickle.load(
    open(r'E:\\testing\\MachineLearning\\creditcardrandom.pkl', 'rb'))
for i in myresult:
    modeldect = {'id': ' ', 'prediction': ' '}
    modeldect['id'] = i[0]
    j = i[1:]
    k = list(j)

    for i in range(0, len(k)):
        k[i] = float(k[i])

    if mlflag == 'Logistic':
        result = loaded_model.predict([k])
    else :
        result = loaded_model1.predict([k])

    modeldect['prediction'] = result[0]
    modelprediction.append(modeldect)
print(modelprediction)
