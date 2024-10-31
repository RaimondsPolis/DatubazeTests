import sqlite3
from flask import Flask, render_template, request
from dati import pievienot_skolenu, pievienot_prieksmetu, pievienot_skolotaju, iegut_skolenus, iegut_skolotajus, iegut_prieksmetu

app = Flask(__name__)
conn = sqlite3.connect("dati.db")

@app.route("/", methods=["POST","GET"])
def index():
    skoleni_no_db = iegut_skolenus()
    print(skoleni_no_db)
    skolotaji_no_db = iegut_skolotajus()
    prieksmeti_no_db = iegut_prieksmetu()
    if request.method == "POST":
        vards = request.form['name']
        uzvards = request.form['lastname']
        skolotajs_v = request.form['sk_name']
        skolotajs_uzv = request.form['sk_lastname']
        prieksmets = request.form['prieksmets']
        if vards and uzvards:
            pievienot_skolenu(vards, uzvards)
        if skolotajs_uzv and skolotajs_v:
            pievienot_skolotaju(skolotajs_v, skolotajs_uzv)
        if prieksmets:
            pievienot_prieksmetu(prieksmets)
        dati = f"pievienotais skolēns - {vards} {uzvards}, skolotājs - {skolotajs_v} {skolotajs_uzv}, priekšmets {prieksmets}"
        return render_template("index.html", aizsutitais = dati, skoleni = skoleni_no_db, skolotaji = skolotaji_no_db, prieksmets = prieksmeti_no_db)
    #get metode
    return render_template("index.html", skoleni = skoleni_no_db, skolotaji = skolotaji_no_db, prieksmets = prieksmeti_no_db)

@app.route("/pievienot")
def pievienot():
    skolotaji = iegut_skolotajus()
    if request.method == "POST":
        print(request.form['skolotajs'])
    return render_template("pievienot.html", skolotaji = skolotaji)

@app.route("/atzimes")
def atzimes():
    return render_template("atzimes.html")

if __name__ == "__main__":
    app.run(port=5000)