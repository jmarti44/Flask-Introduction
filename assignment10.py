from flask import Flask
from flask import request
from markupsafe import escape
from flask import render_template
from flask import make_response
from flask import session
import random

#http://localhost:5000/

app = Flask(__name__)


@app.route("/assignment10.html",methods = ["GET","POST"])
def server():
   
    guess = None
    fname = None
    lname = None
    if (request.method == "GET"):
        fname = request.args.get("fname")
        lname = request.args.get("lname")
    #will only execute with the guessing form
    if(request.method == "POST"):
        correctNum = request.form.get("ran")
        guess = request.form.get("guess")
        if correctNum != guess: 
            return (render_template("wrong.html",guess = guess, ran = correctNum ))
        elif correctNum == guess:
            return "Congrats! You guessed correctly. Thanks for playing!"
    if fname is not None:
        #capitalizing values
        firstName = fname.upper()
        lastName = lname.upper()
        #generating random number which will be saved for the ran key
        randomNum = random.randint(1,5)
        return render_template("next.html",fname = firstName, lname = lastName, ran = randomNum)

    if request.method == "GET":      
        return render_template("assignment10.html", fname = fname, lname = lname)