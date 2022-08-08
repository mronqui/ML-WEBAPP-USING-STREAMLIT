from flask import Flask,render_template,jsonify,request
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)
@app.route('/')
def hello_flask():
    return 'Hello Flask'

@app.route('/inicio')
def show_home():
    return render_template('index.html')

#@app.route('/url_variables/<string:name>/<int:age>')
#def url_variables(name,age):
 #   if age<18:
  #      return jsonify(message='Lo siento '+ name +' no autorizado'), 401 # modifica el texto a json que es el lenguaje de la web
   # else:
    #    return jsonify(message='Bienvenido ' + name), 200

@app.route('/<string:country>/<string:variety>/<float:aroma>/<float:aftertaste>/<float:acidity>/<float:body>/<float:balance>/<float:moisture>') # se dice al Flask el tipo de datos que va a recibir segun el test.py
def result(country,variety,aroma,aftertaste,acidity,body,balance,moisture):
    cols= ['country_of_origin','variety','aroma','aftertaste','acidity','body','balance','moisture'] # cabecera de pandas
    data=[country,variety,aroma,aftertaste,acidity,body,balance,moisture] # datos
    posted=pd.DataFrame(np.array(data).reshape(1,8),columns=cols) # se creo el archivo
    # falta abrir el archivo pickle
    loaded_model=pickle.load(open('../models/coffee_model.pkl','rb'))
    result=loaded_model.predict(posted)
    text_result=result.tolist()[0]
    if text_result=='Yes':
        return jsonify(message='Es un cafe de especialidad'), 200
    else:
        return jsonify(message='No es un cafe de especialidad'), 200

if __name__=='__main__':
    app.run(debug=True,host='127.0.0.1',port=5000) #plataforma 127.0.0.1
