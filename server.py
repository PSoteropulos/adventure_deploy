from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def awaken():
    return render_template("awaken.html")

@app.route("/askbarmaid")
def askbarmaid():
    return render_template("askbarmaid.html")

@app.route("/leavetavern")
def leavetavern():
    return render_template("leavetavern.html")

@app.route("/pickfight")
def pickfight():
    return render_template("pickfight.html")

@app.route("/bouncer")
def bouncer():
    return render_template("bouncer.html")

@app.route("/lantern")
def lantern():
    return render_template("lantern.html")

@app.route("/dagger")
def dagger():
    return render_template("dagger.html")

@app.route("/prybarmaid")
def prybarmaid():
    return render_template("prybarmaid.html")

@app.route("/furtherconversation")
def furtherconversation():
    return render_template("furtherconversation.html")

@app.route("/doordart")
def doordart():
    return render_template("doordart.html")

@app.route("/standground")
def standground():
    return render_template("standground.html")

@app.route("/forest_edge")
def forest_edge():
    return render_template("forest_edge.html")

@app.route("/wait")
def wait():
    return render_template("wait.html")

@app.route("/intotheforest")
def intotheforest():
    return render_template("intotheforest.html")

@app.route("/wait2")
def wait2():
    return render_template("wait2.html")

@app.route("/approach")
def approach():
    return render_template("approach.html")    

@app.route("/dadjoke")
def dadjoke():
    return render_template("dadjoke.html")    

@app.route("/demand")
def demand():
    return render_template("demand.html")    

@app.route("/runaway")
def runaway():
    return render_template("runaway.html")    



if __name__ == "__main__":
    app.run(debug=True)