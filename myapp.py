from flask import Flask, render_template, request
import segno

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code_image = None
    if request.method == 'POST':
        qr_text = request.form['qr_text']
        qr_code = segno.make_qr(qr_text)
        qr_code.save('static/img/qr_code.png', scale=8, border=1)
        qr_code_image = 'static/img/qr_code.png'

    return render_template('index.html', qr_code=qr_code_image)



if __name__ == '__main__':
    app.run(debug=True)


