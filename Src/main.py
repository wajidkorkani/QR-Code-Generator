import qrcode

# Data you want to encode
print("Enter url to generate qr code image: ")
data = input()

# Create qr object
qr = qrcode.QRCode(
    version=1,  # size of the QR Code (1–40), higher = bigger and more data
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box in pixels
    border=4,     # border thickness (boxes)
)

qr.add_data(data)
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color="black", back_color="white")

# Save image
img.save("qr_code.png")
