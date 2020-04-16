from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/informacion')
def about():
    return render_template('about.html')

@app.route('/cursos-gratuitos')
def gratis():
    return render_template('gratis.html')

@app.route('/cursos-pagos')
def pay():
    return render_template('pay.html')

@app.route('/donaciones')
def donanos():
    return render_template('donanos.html')

if __name__ == '__main__':
    app.run(debug=True)
