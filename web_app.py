from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset="UTF-8">
  <meta name="viewport"
  content='width=device-width,scale=1.0'>
  <title>Charan_web</title>
  <link rel="icon" type="image/png" href="image/thumbnail.png">
  <style>
  .container {
    position:relative;
  }
  body {
    background-image:url('/image/image1.png');
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
    
  </style>
</head>
<body>  
  <div class='container'>
    <div class="centered-word">LOGIN!</div>
    <form>
      <input class="input1" type="text" placeholder="username">
      <input class="input2" type="password" placeholder="password">    </form>
  </div> 
</body>
</html>'''

@app.route('/image/<path:filename>')
def serve_image(filename):
    return send_from_directory('/storage/emulated/0/Documents/html/', filename)
 
@app.route("/image/thumbnail.png")
def serv_thumbnail():
    return send_from_directory("/storage/emulated/0/Documents/html/", "thumbnail.png")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5717)
