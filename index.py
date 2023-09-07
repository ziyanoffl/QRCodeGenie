# index.py (Python script)

from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    link = request.form['link']
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('static/qrcode.png')  # Save the QR code image
    return render_template('generated.html')


if __name__ == '__main__':
    app.run(debug=True)
