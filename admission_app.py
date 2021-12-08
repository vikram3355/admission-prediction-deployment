from flask import Flask, request, render_template,jsonify
import pickle as pk
import numpy as np

# Flask constructor
application = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@application.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        # ting input with name = fname in HTML json
        GRE_Scores = float(request.json["GRE_Scores"])
        # ting input with name = lname in HTML json
        TOEFL_Scores = float(request.json["TOEFL_Scores"])
        University_Rating = float(request.json["University_Rating"])
        SOP = float(request.json["SOP"])
        LOR = float(request.json["LOR"])
        CGPA = float(request.json["CGPA"])
        Research_experiance = request.json["Research_experiance"]

        filename = 'admission_model.pk'
        loaded_model = pk.load(open(filename, 'rb'))
        if Research_experiance=="yes":
            yes=1;
            no=0;
        else:
            yes=0;
            no=1;



        predictionresult = loaded_model.predict([[GRE_scores,TOEFL_Scores,University_Rating,SOP,CGPA,yes]])

        result="The Chances od admission is " + str(np.round(predictionresult[0],decimals=2))*100 + "%"
        render_template("index.html")
    return render_template("index.html")


if __name__ == '__main__':
    application.run(debug=True)