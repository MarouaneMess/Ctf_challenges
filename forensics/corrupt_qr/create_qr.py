import qrcode

# Define the message (the flag) to be encoded
flag = "shellmates{c0rrupt3d_qr_Ch4Ll3ng3}"

# Create the QR Code
qr = qrcode.QRCode(
    version=1,  # Control the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code
    border=4,  # Border size
)
qr.add_data(flag)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("original_qr.png")
