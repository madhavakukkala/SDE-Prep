from flask import Flask, request, render_template_string
import datetime
import threading
import time
import pygame

app = Flask(__name__)

alarm_time = None

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Alarm Clock</title>
    <style>
        body {
            font-family: Arial;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: #f4f4f4;
        }

        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 0 10px gray;
        }

        input, button {
            padding: 10px;
            margin: 10px;
            font-size: 18px;
        }

        #clock {
            font-size: 30px;
            margin-bottom: 20px;
        }
    </style>
</head>

<body>

<div class="container">
    <h1>Alarm Clock</h1>

    <div id="clock"></div>

    <form method="POST">
        <input type="time" name="alarm" required>
        <br>
        <button type="submit">Set Alarm</button>
    </form>
</div>

<script>
function updateClock() {
    let now = new Date();

    let h = String(now.getHours()).padStart(2,'0');
    let m = String(now.getMinutes()).padStart(2,'0');
    let s = String(now.getSeconds()).padStart(2,'0');

    document.getElementById("clock").innerHTML =
        h + ":" + m + ":" + s;
}

setInterval(updateClock,1000);
updateClock();
</script>

</body>
</html>
"""


def alarm_checker():
    global alarm_time

    while True:
        if alarm_time:
            current = datetime.datetime.now().strftime("%H:%M")

            if current == alarm_time:
                print("Wake Up!")

                pygame.mixer.init()
                pygame.mixer.music.load("music.mp3")
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    time.sleep(1)

                alarm_time = None

        time.sleep(1)


@app.route("/", methods=["GET", "POST"])
def home():
    global alarm_time

    if request.method == "POST":
        alarm_time = request.form["alarm"]
        print("Alarm set for:", alarm_time)

    return render_template_string(HTML)


if __name__ == "__main__":
    threading.Thread(target=alarm_checker, daemon=True).start()
    app.run(debug=True)