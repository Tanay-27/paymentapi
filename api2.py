#from PIL import Image
from final_year.instamojoapi.api1 import createPayment
import qrcode
# Enter amount and purpose,
# in deployment stage this  will be automated
#amt = float(input('Enter Amount: '))
#pur = input('Enter Purpose: ')
def qrshow(pur,amt):
    amt = 25
    pur = "Med"

    # calling the createPayment function
    url = createPayment(pur,amt)

    # setting advanced parameters for QR code customisation
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
    # adding the URL for Payment request
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # displaying image on screen, further work on this is expected
    img.show()
    return url