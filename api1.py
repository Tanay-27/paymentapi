from instamojo_wrapper import Instamojo
from PIL import Image
API_KEY = 'test_a7fe6937b28c505f371ce8ca286'
AUTH_TOKEN = 'test_a68ddfad2ea46762db39aadd1e3'
api = Instamojo(api_key=API_KEY,
                auth_token=AUTH_TOKEN,
                endpoint='https://test.instamojo.com/api/1.1/')

# Create a new Payment Request
def createPayment(pur,amt):
    response = api.payment_request_create(
        amount=amt,
        purpose=pur,
        #send_email=True,
        email="tanayshah027@gmail.com",
        redirect_url="https://amvmpayment-api.heroku.com/paymentrecieved/"
        )
# print the long URL of the payment request.
#print(response['payment_request']['longurl'])
# print the unique ID(or payment request ID)
#print(response['payment_request']['id'])
    return response['payment_request']['longurl']
