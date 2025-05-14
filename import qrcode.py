import qrcode
import qrcode.constants
#datos para incluir en el codigo QR
datos = "https://music.amazon.com.mx/"

#Creamos un  onjeto QRcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    
#agg datos al codigo QR
qr.add_data(datos)
qr.make(fit=True)

#Generar la imagen del Codigo QR
img = qr.make_image(fill_color="red", back_color="white")

#Guardar la imagen
img.save ("Codigo_qr.png")
print("Codigo QR generado correctamente")