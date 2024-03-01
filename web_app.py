from flask import Flask,url_for
import os

app = Flask(__name__)



@app.route('/login.charan')
def index():
    html_content= """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Animated Sunset (Code Only)</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: #e0c3fc;
            /* Adjust background color as needed to match the sky color */
        }

        .container {
            position: relative;
            width: 100vw;
            height: 100vh;
            overflow: hidden;
        }

        .sun {
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 200px;
            height: 200px;
            border-radius: 50%;
            background: radial-gradient(circle at center, rgba(255, 159, 0, 1) 0%, rgba(255, 204, 0, 0.7) 70%, rgba(255, 255, 255, 0) 100%);
            animation: sunAnim 5s ease-in-out infinite alternate;
        }

        .palm-trees {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 50%;
            background: linear-gradient(#8da9c4, #a0bec4); /* Adjust colors as needed */
            animation: palmTreesAnim 5s ease-in-out infinite alternate;
        }

        @keyframes sunAnim {
            0% {
                opacity: 1;
                transform: translateX(-50%) scale(1);
            }
            50% {
                opacity: 0.7;
                transform: translateX(-50%) scale(1.1);
            }
            100% {
                opacity: 1;
                transform: translateX(-50%) scale(1);
            }
        }

        @keyframes palmTreesAnim {
            0% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(10px);
            }
            100% {
                transform: translateY(0);
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="sun"></div>
        <div class="palm-trees"></div>
    </div>
</body>
</html>

    """
    return html_content

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')