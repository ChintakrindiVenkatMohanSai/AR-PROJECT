import os
from flask import Flask, render_template, request, redirect, send_from_directory

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# HOME
@app.route("/")
def home():
    return render_template("home.html")

# -------- 3D AR --------
@app.route("/upload3d")
def upload3d():
    return render_template("upload3d.html")

@app.route("/upload-model", methods=["POST"])
def upload_model():
    file = request.files["file"]
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return redirect("/ar3d/"+file.filename)

@app.route("/ar3d/<filename>")
def ar3d(filename):
    return render_template("ar3d.html", file=filename)

# -------- 2D AR --------
@app.route("/upload2d")
def upload2d():
    return render_template("upload2d.html")

@app.route("/upload-2d", methods=["POST"])
def upload_2d():
    file=request.files["file"]
    file.save(os.path.join(UPLOAD_FOLDER,file.filename))
    return redirect("/viewer2d/"+file.filename)

@app.route("/viewer2d/<filename>")
def viewer2d(filename):
    return render_template("viewer2d.html", file=filename)

# -------- WALL COLOR --------
@app.route("/wall")
def wall():
    return render_template("wall.html")

# -------- MEASUREMENT --------
@app.route("/measure")
def measure():
    return render_template("measure.html")

# Serve uploads
@app.route("/uploads/<filename>")
def uploads(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)