import qrcode
import image
qr = qrcode.QRCode(
    version =10, #version determines the size and complication of qr code meaning varying the number will generate different qr codes
    box_size= 5, #size of box where qr will be displayed
    border = 2   #white part of the image, border in all 4 sides with white colour

)

data = "https://github.com/daksh20000"   #data to be stored inside the qr

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="green", back_colour = "white" )
img.save("testqr.png")