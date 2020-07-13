from final_year.instamojoapi.func import createPayment, timeLim, qrShow
from PIL import Image
amount = float(input('Enter Amount: '))
purpose = input('Enter Purpose: ')

url , requestid = createPayment(pur = purpose , amt = amount)

qrShow(url=url)
img = Image.open('qr.jpg')
img.show()
final_status = timeLim(reqid=requestid,timer =60)
print('Final Status: {}'.format(final_status))
