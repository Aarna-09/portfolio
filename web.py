
from flask import Flask, render_template, request

web = Flask(__name__)

@web.route('/')
def layout():
    return render_template("./layout.html")

@web.route('/design')
def design():
    return render_template("./design.html")

@web.route('/create')
def create():
    return render_template("./create.html")

@web.route('/upload', methods=['POST','GET'])
def upload():
    if request.method == "POST":
        Firstname = request.form.get("Firstname")
        Lastname = request.form.get("Lastname")
        Schoolname = request.form.get("Schoolname")
        Collegename = request.form.get("Collegename")
        Email = request.form.get("Email")
        Skills1 = request.form.get("Skills1")
        Skills2 = request.form.get("Skills2")
        Skills3 = request.form.get("Skills3")
        WriteaboutYourself = request.form.get("WriteaboutYourself")

        print("Firstname:", Firstname)
        print("Lastname:", Lastname)
        print("Schoolname:", Schoolname)
        print("Schoolname:", Collegename)
        print("Email:", Email)
        print("Skills1:", Skills1)
        print("Skills2:", Skills2)
        print("Skills3:", Skills3)
        print("WriteaboutYourself:", WriteaboutYourself)

    return "Form submitted successfully"

if __name__ == "__main__":
    web.run(debug=True)