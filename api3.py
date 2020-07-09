from flask import Flask, request, render_template, url_for
import api1
app = Flask(__name__)

from instamojo_wrapper import Instamojo

app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))
API_KEY = 'test_a7fe6937b28c505f371ce8ca286'
AUTH_TOKEN = 'test_a68ddfad2ea46762db39aadd1e3'
api = Instamojo(api_key=API_KEY,
                auth_token=AUTH_TOKEN,
                endpoint='https://test.instamojo.com/api/1.1/')

response = api.payment_request_create(
    amount=25,
    purpose="app test",
    send_email=True,
    email="tanayshah027@gmail.com",
    redirect_url="https://amvmpayments-api.herokuapp.com/paymentrecieved",
    )

@app.route('/')
def home():
    dict = { 'amt':15}
    return render_template('homepage.html')

@app.route('/paymentrecieved',methods = 'GET')
def accept_payment():
    idm  = request.args.get('payment_id')
    stat = request.args.get('payment_status')
    req = request.args.get('payment_request_id')
    dct = {'id':idm,'stat':stat,'req':req}
    return f"<h1>{stat}</h1>"

if __name__ == "__main__" :
    app.run(debug=True)