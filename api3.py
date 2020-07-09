from flask import Flask, request, render_template, url_for
import api1
app = Flask(__name__)

url = api1.createPayment("getfrompc",30)
@app.route('/')
def home():
    dict = { 'amt':15,'url':url}
    return render_template('homepage.html')

@app.route('/paymentrecieved/',methods = ['GET'])
def accept_payment():
    id  = request.args.get('payment_id')
    stat = request.args.get('payment_status')
    req = request.args.get('payment_request_id')
    dct = {'id':id,'stat':stat,'req':req}
    return render_template('index.html')

if __name__ == "__main__" :
    app.run(debug=True)