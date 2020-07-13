from final_year.instamojoapi.func import createPayment, getResp, qrShow
from flask import Flask, request, render_template, url_for, session
from PIL import Image
app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'

@app.route('/')
def home():
    dict = { 'amt':15}
    return render_template('homepage.html')

@app.route('/pay/',methods=['GET','POST'])
def paymentProcessing():
	amount = request.form.get('Amount')
	purpose = request.form.get('Purpose')
	global url
	global requestId
	url,requestId = createPayment(amt = amount, pur = purpose)
	session['ReqId'] = requestId
	qrShow(url)
	#img = Image.open('qr.jpg')
	#img.show()
	img = 'qr.jpg'
	data = {'url':url,'amt':amount, 'img':img}
	return render_template('payment.html',data = data)


@app.route('/check/',methods=['POST','GET'])
def qrcodeshow():
	global requestId
	requestId = session['ReqId']
	stat = getResp(requestId)
	if stat == 'Completed':
		ans = 'Success'
	else:
		ans = 'Failure'
	data = {'ans':ans}
	return render_template('result.html',data = data)

if __name__ == "__main__" :
    app.run(debug=True)
