from flask import Flask, render_template, request, send_file
import io
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

    # Convert image to bytes and send it directly to the HTML template
    img_io = io.BytesIO()
    img.save(img_io, format='PNG')
    img_io.seek(0)

    return render_template('generated.html', qr_image=img_io)


if __name__ == '__main__':
    app.run(debug=True)