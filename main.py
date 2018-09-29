from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    name = request.form['Name']
    email = request.form['Email']
    steam = request.form['Steam']
    disc = request.form['Discord']

    if name == "" or email == "":
        return 'Must include your name and email <a href="/">Go Back</a>'
    if steam == "" and disc == "":
        return 'Must include your discord, you steam, or both. <a href="/">Go Back</a>'

    f = open("sign-ups/" + name, "w")
    contents = "---------- " + name + " ----------\n"
    contents += "EMAIL: " + email + "\n"
    contents += "STEAM: " + steam + "\n"
    contents += "DISCORD: " + disc + "\n"

    f.write(contents)

    return 'Your form has been submitted! We will contact you shortly. Happy boss-fighting! <a href="/">Go Back</a>'

app.run(host='127.0.0.1', port=8282)
