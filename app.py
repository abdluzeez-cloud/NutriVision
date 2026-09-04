from flask import Flask, render_template, request, jsonify
app=Flask(__name__)
FOODS={"apple":("Apple",95,0.5,25,0.3),"banana":("Banana",105,1.3,27,0.4),"chicken":("Chicken Breast",165,31,0,3.6),"rice":("Cooked Rice",205,4.3,44.5,0.4),"egg":("Egg",78,6.3,0.6,5.3),"salad":("Green Salad",80,2,10,4),"oatmeal":("Oatmeal",150,5,27,3),"yogurt":("Greek Yogurt",120,17,7,3)}
@app.route("/")
def home(): return render_template("index.html")
@app.route("/calculator")
def calculator(): return render_template("calculator.html")
@app.route("/scanner")
def scanner(): return render_template("scanner.html")
@app.route("/dashboard")
def dashboard(): return render_template("dashboard.html")
@app.route("/meals")
def meals(): return render_template("meals.html")
@app.route("/about")
def about(): return render_template("about.html")
@app.post("/api/calculate")
def calculate():
 d=request.get_json(); age=float(d["age"]); w=float(d["weight"]); h=float(d["height"]); sex=d["sex"]; activity=float(d["activity"]); goal=d["goal"]
 bmr=10*w+6.25*h-5*age+(5 if sex=="male" else -161); tdee=bmr*activity; target=max(1200,round(tdee+{"lose":-400,"maintain":0,"gain":300}[goal])); bmi=w/(h/100)**2
 return jsonify(bmr=round(bmr),tdee=round(tdee),target=target,bmi=round(bmi,1))
@app.post("/api/scan")
def scan():
 name=request.form.get("food","salad").lower(); x=FOODS.get(name,FOODS["salad"])
 return jsonify(name=x[0],calories=x[1],protein=x[2],carbs=x[3],fat=x[4],demo=True)
if __name__=="__main__": app.run(debug=True)
