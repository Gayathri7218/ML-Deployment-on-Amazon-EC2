from flask import Flask, request, render_template_string
import joblib

app = Flask(__name__)
data = joblib.load("model.pkl")
model, names = data["model"], data["names"]

HTML = """
<h1>ML Prediction on Amazon EC2</h1>
<form method="post">
{% for field in ['Sepal length', 'Sepal width',
                 'Petal length', 'Petal width'] %}
<label>{{field}} (cm): </label>
<input type="number" name="x" step="any"
       min="0.1" max="10" required><br><br>
{% endfor %}
<button type="submit">Predict</button>
</form>
<h2>{{result}}</h2>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        try:
            values = [float(v) for v in request.form.getlist("x")]
            if len(values) != 4 or any(v <= 0 or v > 10 for v in values):
                return "Enter four valid values between 0 and 10.", 400
            prediction = model.predict([values])[0]
            result = "Predicted Flower: " + names[prediction]
        except ValueError:
            return "Invalid input.", 400
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
