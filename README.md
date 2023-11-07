## SimpleQRs Overview

__SimpleQRs__ is an online web application built with Flask in Python.<br>
It offers everyone a platform where they can generate a QR code for anything, from text notes to web links for free.

Head over to [the SimpleQRs website](https://simpleqrs.pythonanywhere.com) and try it out today!


### For Developers
We'll start with creating a virtual environment in Python with:<br>
```Python
# Windows
python -m venv my_env
```
then activate it with:<br>
```Python
# Windows
my_env\Scripts\activate
```
We will then install the required dependencies which are __Flask__ and __segno__.<br>
*__Segno__ is a Python library that provides functionality for creating QR codes.*<br>
```Python
# Windows
python -m pip install Flask
python -m pip install segno
```

In the project directory, we will create a file named `myapp.py`.<br>
In the file we will have the following code:
```Python
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

```

The Flask app above takes the value of `qr_code` as an input from the user, creates a QR code, and saves it in the `img` directory in the `static` folder.

We will then create two folders, namely; `templates` and `static`.<br>
In the `templates` folder, we will create a file named `index.html` which will contain the code below:<br>
```HTML
        <p>Create a QR code by inputting a link or text into the form provided below.</p>
        <form method="POST">
            <label for="qr_text"></label>
            <input type="text" name="qr_text" id="qr_text" required placeholder="Text or Link">
            <button type="submit">Generate Code</button>
        </form>

        {% if qr_code %}
        <div class="image">
            <img src="{{ qr_code }}" alt="QR Code">
        </div>
        <div class="buttons">
            <div class="share">
                <button type="button" onclick="shareQRCodeAsImage()">Share as Image</button>
            </div>

            <div class="download">
                <button type="submit"><i class="fa-solid fa-cloud-arrow-down"></i> Download</button>
            </div>
        </div>
        {% endif %}
    </div>
```

Then another one file named `index.css` in the `static/css` directory, where we will style our page.

By running the file with<br>
```Python
# Windows
python myapp.py
```
and heading to `http://127.0.0.1:5000/`, we can view the form, and use it to generate our QR code(s) which will be displayed on the page after successful generation.

Alternatively, you can create a `.gitignore` file in the project directory, and add the virtual environment you created like I did below:<br>
```Python
# In the .gitignore
myvenv/
```
This tells git that it should ignore the files and folders in the `.gitignore` file when pushing the code to __GitHub__.