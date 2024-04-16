from flask import Flask, request, redirect, url_for, send_from_directory, render_template_string

app = Flask(__name__)

valid_credentials = {
    "charanwb": "crn5717"
}

@app.route('/ch', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in valid_credentials and valid_credentials[username] == password:
            return redirect("https://www.python.org/")
        else:
            error = 'Invalid username or password'

    html = '''<!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content='width=device-width, initial-scale=1.0'>
        <title>Charan_web</title>
        <link rel="icon" type="image/png" href="/image/thumbnail.png">
        <style>
            .container {
                position:relative;
            }
            body {
                background-image:url('/background-image/unplash_buddha.png');
                background-repeat:no-repeat;
                background-attachment:fixed;
                background-size:cover;
            }
            .centered-word{
                position:absolute;
                font-family:'Courier New', monospace;
                font-size:4rem;
                transform:translate(50% ,100%);
            }
            input {
                height:2vh;
                padding:20px;
                border-radius:20px;
            }
            input.input1{
                position: absolute;
                transform: translate(50% ,400%);
            }
            input.input2{
                position:absolute;
                transform:translate(50% ,550%);
            }
            button {
                height: 50px;
                width: 100px;
                background-color: #4CAF50;
                color: white;
                border-radius: 20px;
                border: none;
                cursor: pointer;
                position: absolute;
                transform: translate(-50%, 850%);
                left: 50%;
            }
        </style>
    </head>
    <body>
    <div class='container'>
        <div class="centered-word">LOGIN!</div>
        {% if error %}
        <div style="color: red; position: absolute; transform: translate(50%, 100%);">{{ error }}</div>
        {% endif %}
        <form method="post">
            <input class="input1" type="text" name="username" placeholder="username">
            <input class="input2" type="password" name="password" placeholder="password">
            <button type="submit">Go</button>
        </form>
    </div>
    </body>
    </html>'''
    return render_template_string(html, error=error)

@app.route('/background-image/<path:filename>')
def serve_background_image(filename):
    return send_from_directory('/storage/emulated/0/Download/', filename)

@app.route("/image/thumbnail.png")
def serve_thumbnail():
    return send_from_directory("/storage/emulated/0/Documents/html/", "thumbnail.png")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
