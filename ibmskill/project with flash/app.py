"""
Este módulo define una aplicación web Flask para gestionar una biblioteca de libros.

Funcionalidades:
- Listar libros.
- Prestar libros.
- Devolver libros.
- Guardar libros.

"""

from flask import Flask, request, jsonify, render_template

import clase_libro


app = Flask(__name__)
mi_biblioteca = clase_libro.Biblioteca()  # Se crea la instancia de biblioteca

libros_inicio = [
    ["Cien años de soledad", "Gabriel García Márquez", "978-0307474727", True],
    ["1984", "George Orwell", "978-0451524935", True],
    ["Orgullo y prejuicio", "Jane Austen", "978-0141439518", True],
    ["El señor de los anillos", "J.R.R. Tolkien", "978-0618260231", True],
    ["Matar un ruiseñor", "Harper Lee", "978-0061120084", True],
    ["Don Quijote de la Mancha", "Miguel de Cervantes", "978-8420471899", True],
    ["El guardián entre el centeno", "J.D. Salinger", "978-0316769174", True],
    ["Crimen y castigo", "Fyodor Dostoevsky", "978-0679734505", True],
    ["En busca del tiempo perdido", "Marcel Proust", "978-0141180331", True],
    ["Ulises", "James Joyce", "978-0679722762", True],
]
for libro in libros_inicio:
    mi_biblioteca.agregar_clase_libro(
        clase_libro.Libro(libro[0], libro[1], libro[2], libro[3])
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/listar")
def listar():
    return mi_biblioteca.mostrar_libros()


@app.route("/prestar/<int:id>")
def prestar(id):
    result=mi_biblioteca.prestar_libro(id)
    if result:
        return jsonify({"message": "Libro prestado", "success": True})
    elif result is None:
        return jsonify({"message": "ID de libro incorrecto.", "success": False})
    else:
        return jsonify({"message": "El libro no está disponible", "success": False})

@app.route("/devolver/<int:id>")
def devolver(id):
    result=mi_biblioteca.devolver_libro(id)
    if result:
        return jsonify({"message": "Libro devuelto", "success": True})
    elif result is None:
        return jsonify({"message": "ID de libro incorrecto.", "success": False})
    else:
        return jsonify({"message": "El libro no está disponible", "success": False})    

@app.route("/guardar", methods=["POST"])
def guardar():
    titulo = request.form.get("titulo")
    isbn = request.form.get("isbn")
    autor = request.form.get("autor")
    disponible = request.form.get("disponible") == "true"

    if not all([titulo, isbn, autor, disponible is not None]):
        return jsonify({"message": "Faltan datos", "success": False})

    try:
        mi_biblioteca.agregar_clase_libro(
            clase_libro.Libro(titulo, autor, isbn, disponible)
        )
        return jsonify({"message": "Libro guardado", "success": True})
    except Exception as e:
        return jsonify({"message": f"Error al guardar el libro: {e}", "success": False})

app.run(host="0.0.0.0", port=8000, debug=True)

