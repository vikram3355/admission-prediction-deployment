from flask import Flask, request, render_template
import pickle as pk
import numpy as np

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        # ting input with name = fname in HTML json
        GRE_Scores = request.form.get("GRE_Scores")
        # ting input with name = lname in HTML json
        TOEFL_Scores = float(request.form.get("TOEFL_Scores"))
        University_Rating = float(request.form.get("University_Rating"))
        SOP = float(request.form.get("SOP"))
        LOR = float(request.form.get("LOR"))
        CGPA = float(request.form.get("CGPA"))
        Research_experiance = request.form.get("Research_experiance")

        filename = r'C:\Users\vsmal\admission predict\admission_model.pk'
        loaded_model1 = pk.load(open(filename, 'rb'))
        if Research_experiance=="yes":
            yes=1;
            no=0;
        else:
            yes=0;
            no=1;



        predictionresult = loaded_model1.predict([[GRE_Scores,TOEFL_Scores,University_Rating,SOP,LOR,CGPA,yes]])

        return "The Chances of admission is " + str(np.round(predictionresult[0],decimals=2)*100)+"%"
        #render_template("index.html")
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)