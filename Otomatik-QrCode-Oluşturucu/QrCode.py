from turtle import fillcolor
import qrcode

qr = qrcode.QRCode(version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=5)

giden_değer= "MERHABA BU DENEME QR KODUDUR."

qr.add_data(giden_değer)
qr.make(fit=True)

resim = qr.make_image(fillcolor = "black", back_color = "white")
resim.save("ilk_qr_code.png")
