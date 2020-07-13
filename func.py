import time
from instamojo_wrapper import Instamojo
from PIL import Image
import qrcode

# Authentication Details 
API_KEY = 'test_a7fe6937b28c505f371ce8ca286'
AUTH_TOKEN = 'test_a68ddfad2ea46762db39aadd1e3'
api = Instamojo(api_key=API_KEY,
                auth_token=AUTH_TOKEN,
                endpoint='https://test.instamojo.com/api/1.1/')

# Create a new Payment Request
def createPayment(pur,amt):
    """ Takes purpose of Payment and Amount to be payed string,float as input and provides the URL and Payment Request Id """
    response = api.payment_request_create( amount = amt , purpose = pur,  send_email = True , email = "tanayshah027@gmail.com")
    print('URL for payment:',response['payment_request']['longurl'])                     #print the long URL of the payment request.
    print('Payment Request ID:',response['payment_request']['id'])                       #print the unique ID(or payment request ID)
    return (response['payment_request']['longurl'],response['payment_request']['id'])    #Return Payment Request and Id

# Get response from Instamojo API Server
def getResp(reqid):
    """ Takes the Payment Request Id for the User and Returns the Current Status for that particular Payment """
    resp = api.payment_request_status(str(reqid))
    ret = resp['payment_request']['status']         # Choose the Status parameter 
    return ret

# Time limit for the payment can be set 
def timeLim(reqid,timer = 60):
    """ Time Limit for the Function, takes the Payment Reqest Id 
    and the time in seconds as wait time as inputs and returns final status """
    start = time.time()                             # Initiate the counting 
    print('You can pay whithin the next minute \n')
    el = 0
    status = 'Failed'
    while el < timer:
        x=0
        status = getResp(reqid)                     # Calling the function continuously till either the timer ends or payment is complete
        if status == 'Completed':                   # When payment is completed, this contition will be true
            print('Payment Successful')
            break                                   # exit from the While Loop
        print('-',end='')                           # Print while Waiting
        el = time.time() - start
        for i in range(10000):                      # To generate a small software delay between each cycle
            x+=1
    if status != 'Completed': print('Sorry Payment Unsuccessful')
    return status

# Displaying QR Code taking url as input
def qrShow(url):
    """ Takes the URL as input and displays the image """
    # Setting advanced parameters for QR code customisation
    qr = qrcode.QRCode( version = 1 , error_correction = qrcode.constants.ERROR_CORRECT_L, box_size=10 , border=4 )
    qr.add_data(url)                                # Adding the URL for Payment request
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # Displaying image on screen, further work on this is expected
    img.save('qr','JPEG',resolution = 200.0)                              # Displaying the Image on the Screen    
