from PIL import Image
import zbarlight
import json
from Transaction import TransactionStat


def checkScanner():
    file_path = 'test1.png'
    with open(file_path, 'rb') as image_file:
        image = Image.open(image_file)
        image.load()

    codes = zbarlight.scan_codes(['qrcode'], image)
    print('QR codes: %s' % codes)

    decoded_val = {}

    for val in codes:
        decoded_val = val.decode()

    # decoded_val = json.dumps(decoded_val.replace())
    # print(decoded_val)
    txnVal = json.loads(decoded_val)
    print(txnVal)

    txnResponse = TransactionStat.checkTransaction(txnVal)

    if txnResponse['status_code'] == 200:
        print("\n\n\t\tTransaction Completed\n\n")
        TransactionStat.checkBalance()
    else:
        print("\n\n\t\tTransaction Failed! Please try again\n\n")
        TransactionStat.checkBalance()


checkScanner()
