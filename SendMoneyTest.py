import qrcode
import CaptureImage

qr = qrcode.QRCode()
qr.add_data('{"userId":"123", "amount":"125","transaction":"debit","transact_time":"DatetimeWithNanoseconds(2022, 7, 8, 9, 40, 39, 131031, tzinfo=datetime.timezone.utc)"}')
qr.make()
img = qr.make_image()
img.save('test1.png')


# qr.add_data('{"userId":"124", "amount":"142","transaction":"debit","transact_time":"DatetimeWithNanoseconds(2022, 7, 8, 9, 40, 39, 131031, tzinfo=datetime.timezone.utc)"}')
# qr.make()
# img = qr.make_image()
# img.save('test2.png')
#
#
# qr.add_data('{"userId":"125", "amount":"108","transaction":"debit","transact_time":"DatetimeWithNanoseconds(2022, 7, 8, 9, 40, 39, 131031, tzinfo=datetime.timezone.utc)"}')
# qr.make()
# img = qr.make_image()
# img.save('test3.png')

# qr.add_data('{"userId":"126", "amount":"80","transaction":"credit","transact_time":"DatetimeWithNanoseconds(2022, 7, 8, 9, 40, 39, 131031, tzinfo=datetime.timezone.utc)"}')
# qr.make()
# img = qr.make_image()
# img.save('test4.png')