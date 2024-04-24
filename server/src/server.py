from flask import Flask
from flask import Response
from flask import send_file
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Server ready from Flask 🌶️"

@app.route("/test/plot")
def test_plot():
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy
    from io import BytesIO

    x = numpy.random.normal(5, 2, 100)

    # Crea una figura de Matplotlib
    fig, ax = plt.subplots()
    sns.histplot(x)

    # Guarda la figura en un objeto BytesIO en memoria
    img = BytesIO()
    fig.savefig(img, format="png")
    img.seek(0)  # Regresa al comienzo del objeto de bytes

    # Cierra la figura para liberar memoria
    plt.close(fig)

    # Envía el objeto de bytes como una respuesta
    return send_file(img, mimetype="image/png")

@app.route("/test/csv")
def test_csv():
    import numpy as np
    import pandas as pd

    x = np.linspace(-np.pi, np.pi, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    df = pd.DataFrame({
        "X": x,
        "Y1": y1,
        "Y2": y2
    })

    csv = df.to_csv(index=False)

    return Response(csv, mimetype="text/csv", headers={
        "Content-disposition": "attachment; filename=test.csv"
    })

@app.route("/test/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "GET":
        message = request.args.get("message", None)
        return render_template("upload.html", message=message)
    
    if "file" not in request.files:
        return redirect(request.url)
    file = request.files["file"]
    if file.filename == "":
        return redirect(request.url)
    if file:
        # filename = secure_filename(file.filename)
        file.save(f"uploads/{file.filename}")
        return redirect("/test/upload?message=Listo")

app.run(port=5000, host="0.0.0.0")