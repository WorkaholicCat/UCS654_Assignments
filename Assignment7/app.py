from flask import Flask, render_template, request
import importlib.util
import sys
import os
import zipfile

app = Flask(__name__)

module_name = "mashup_module"
file_path = os.path.join(os.path.dirname(__file__), "102303941.py")

spec = importlib.util.spec_from_file_location(module_name, file_path)
mashup = importlib.util.module_from_spec(spec)
sys.modules[module_name] = mashup
spec.loader.exec_module(mashup)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        singer = request.form["singer"]
        email = request.form["email"]
        try:
            num = int(request.form["num"])
            duration = int(request.form["duration"])
        except ValueError:
            return "Number of videos and duration must be integers."

        if num <= 10:
            return "Number of videos must be greater than 10."

        if duration <= 20:
            return "Duration must be greater than 20 seconds."

        if "@" not in email:
            return "Invalid email address."
        output_file = "mashup.mp3"
        try:
            mashup.create_mashup(singer, num, duration, output_file)
            zip_name = "mashup.zip"
            with zipfile.ZipFile(zip_name, 'w') as zipf:
                zipf.write(output_file)
            return render_template("success.html")
        except Exception as e:
            return f"Error occurred: {e}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=10000)
