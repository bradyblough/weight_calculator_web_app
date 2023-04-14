from flask import Flask, render_template, request

# creates flask app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():  # calculates user's weight on other worlds by multiplying mass by planet's gravitational acceleration
    if request.method == 'POST':
        earth_weight = request.form["earth_weight"]  # gets weight from user input
        mass = float(earth_weight) / 9.8  # calculates user's mass
        mercury = round(mass * 3.7, 2)
        venus = round(mass * 8.9, 2)
        mars = round(mass * 3.7, 2)
        jupiter = round(mass * 24.8, 2)
        saturn = round(mass * 10.4, 2)
        uranus = round(mass * 8.9, 2)
        neptune = round(mass * 11.2, 2)
        return render_template('index.html', Mercury=mercury, Venus=venus, Mars=mars, Jupiter=jupiter, Saturn=saturn,
                               Uranus=uranus, Neptune=neptune)

    else:
        return render_template('index.html')


app.run(debug=True)
