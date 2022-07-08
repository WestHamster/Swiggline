<h1>Swiggline</h1>


#### What can it do?
1. Solve the bank unavailability issue
2. Increase the user time on platform
3. Alternative payment method

#### Functionalities
1. Add money to Wallet
2. Send money from Wallet

<br />
<br />


#### User Journey
#### Send Money
1. Food is being delivered to the user, and they've opted for COD.
2. Once the delivery guy comes in, they can show the QR code containing the 
details of the customer and the amount that needs to be paid.
3. The user scans the QR code, the amount is debited from the wallet which will contain upto Rs.1000.
4. Once debited, the user can show the Transaction Successful message to the DE and they can capture 
the screenshot for the same.
5. Once the user connects to the internet, the wallet balance is synced with the server and the transaction 
containing the details is updated.


#### Add Money
1. Wallet of a user can be recharged with any source possible.
2. User needs to be online in order to recharge.
3. Future possibilities of user asking for coupon/voucher could be used.

<br />
<br />

#### How to test?

#### Installation
1. start a virtual environment
2. pip3 -m install requirements.txt
3. If you face any issue with installation or regarding zbarlight, refer appendix below.

#### Send Money

1. Run SendMoneyTest.py with any one of the input.
2. Run SendMoney.py

<br />
<br />

#### Future enhancements

1. Adding tkinter to make a proper app 
2. How to add image functionality? 
   1. Hold the QR code in front of the camera 
   2. Run CaptureImage.py
   3. Add the image path to SendMoney.py
3. Adding support for AddMoney

<br />
<br />
<br />

#### Appendix
1. For firebase-admin, if on M1 mac:
   1. xcode-select --install
   2. arch -arch x86_64 </usr/bin/python3> -m pip install firebase-admin
   3. pip3 install firebase-admin
2. While installing zbarlight: https://github.com/Polyconseil/zbarlight/issues/16
3. Added the firebase service account key to test the flow.
