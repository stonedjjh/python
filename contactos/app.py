from flask import Flask, render_template, redirect, request
from flask_wtf.csrf import CSRFProtect
from connect import db
from models import User
from forms.contacto_form import Contacto

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
csrf = CSRFProtect(app)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def welcome():
    return "Welcome to the Home Page"

@app.route("/crear_contacto")
def nuevo_contacto():    
    return render_template("crear_contacto.html", form=Contacto())

@app.route("/listar_contactos")
def listar_contactos():
    users = User.query.all()
    return render_template("listar_contactos.html", contactos=users)


@app.route("/guardar_contacto", methods=['GET', 'POST'])
def guardar_contacto():    
    form = Contacto()
    if form.validate_on_submit():
        if request.method == "POST":
            user = User(
                nombre=request.form["nombre"],
                apellido=request.form["apellido"],
                email=request.form["email"],
                telefono=request.form["telefono"]
            )
            db.session.add(user)
            db.session.commit()
        return redirect("/listar_contactos")
    return render_template("crear_contacto.html", form=form)

@app.route("/borrar_contacto/<int:id>", methods=["GET", "POST"])
def user_delete(id):
    user = db.get_or_404(User, id)
    if user:
        db.session.delete(user)
        db.session.commit()        
    return redirect("/listar_contactos")

@app.route("/success")
def success():
    return "Formulario enviado correctamente"


if __name__ == "__main__":
    app.run(debug=True)
