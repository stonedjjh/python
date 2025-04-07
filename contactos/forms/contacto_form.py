from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Regexp, Length

class Contacto(FlaskForm):
    nombre = StringField(
        'Nombre',
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(min=3, max=50, message="El nombre debe tener entre 3 y 50 caracteres.")
        ],
        render_kw={"class": "w-25 px-3 py-2 text-gray-700 border rounded-md focus:outline-none focus:shadow-outline"},
        filters=[lambda x: x.strip() if x else None]
    )
    apellido = StringField(
        'Apellido',
        validators=[
            DataRequired(message="El apellido es obligatorio."),
            Length(min=3, max=50, message="El apellido debe tener entre 3 y 50 caracteres.")
        ],
        render_kw={"class": "w-35 px-3 py-2 text-gray-700 border rounded-md focus:outline-none focus:shadow-outline"},
        filters=[lambda x: x.strip() if x else None]
    )
    email = EmailField(
        'Correo Electronico',
        validators=[DataRequired(message="El correo electrónico es obligatorio.")],
        render_kw={"class": "w-35 px-3 py-2 text-gray-700 border rounded-md focus:outline-none focus:shadow-outline"}
    )
    telefono = StringField(
        'Telefono',
        validators=[
            DataRequired(message="El teléfono es obligatorio."),
            Regexp(r'^\d+$', message="El teléfono debe contener solo números")
        ],
        render_kw={"class": "w-35 px-3 py-2 text-gray-700 border rounded-md focus:outline-none focus:shadow-outline"},
        filters=[lambda x: x.strip() if x else None]
    )
    guardar = SubmitField(
        'Guardar',
        render_kw={"class": "bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"}
    )
