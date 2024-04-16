from flask import Flask, render_template, request, json, jsonify

app = Flask(__name__)

@app.route('/vendedor', methods=['GET'])
def index():
    return render_template("vendedor/homevendedor.html")

# ! RUTA SHEYLA

if __name__ == '__main__':
    app.run(debug=True)
