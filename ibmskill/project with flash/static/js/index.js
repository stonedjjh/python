class TablaLibros extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: "open" });
    this.data = [];
  }

  static get observedAttributes() {
    return ["data"];
  }

  attributeChangedCallback(name, oldValue, newValue) {
    if (name === "data") {
      try {
        this.data = JSON.parse(newValue);
        this.render();
      } catch (error) {
        console.error("Error al analizar el JSON:", error);
        this.data = [];
        this.render();
      }
    }
  }

  connectedCallback() {
    this.render();
  }

  render() {
    this.shadowRoot.innerHTML = `
      <style>
        table {
          width: 100%;
          border-collapse: collapse;
        }
        th, td {
          border: 1px solid black;
          padding: 8px;
          text-align: left;
        }
        th {
          background-color: #f2f2f2;
        }
        /* Estilos para los botones */
        button {
          padding: 2px 10px;
          margin: px;
          border: none;
          border-radius: 4px;
          cursor: pointer;
          font-size: 0.8rem;
        }

        button:disabled {
          background-color: #cccccc;
          color: #666666;
          cursor: not-allowed;
        }

        button.devolver {
          background-color: red;
          color: white;
          font-weight: bold;
        }
        button.prestar {
          background-color: green;
          color: white;
          font-weight: bold;
        }

        /* Estilos hover */
        button:hover {
          opacity: 0.8;
        }

      </style>
      ${this.getTableTemplate()}
    `;
  }

  getTableTemplate() {
    //Comprobar si el json que recibe tiene un mensaje.
    if (this.data.hasOwnProperty("message")) {
      return `<p>${this.data.message}</p>`;
    }
    if (this.data.length === 0) {
      return "<p>Sin Información</p>";
    }

    let tableRows = this.data
      .map(
        (item, index) => `
      <tr>
        <td>${item.id}</td>
        <td>${item.autor}</td>
        <td>${item.titulo}</td>
        <td>${item.isbn}</td>
        <td>${item.disponible ? "Disponible" : "No Disponible"}</td>
        <td>
          <button class="devolver" ${
            item.disponible ? "disabled" : ""
          }>Devolver</button>
          <button class="prestar" ${
            item.disponible ? "" : "disabled"
          } onclick="prestarLibro(${item.id})">Prestar</button>    
        </td>
      </tr>
    `
      )
      .join("");

    return `
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Autor</th>
            <th>Título</th>
            <th>ISBN</th>
            <th>Disponibilidad</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          ${tableRows}
        </tbody>
      </table>
    `;
  }
}

customElements.define("tabla-libros", TablaLibros);

async function listarLibros() {
  try {
    const response = await fetch("/listar");
    if (!response.ok) {
      throw new Error(`Error HTTP! estado: ${response.status}`);
    }
    const data = await response.json();
    //Seleccionar el web component que ya fue creado en el html.
    const tabla = document.querySelector("tabla-libros");
    //Añadir el atributo data al web component.
    tabla.setAttribute("data", JSON.stringify(data));
  } catch (error) {
    console.error("Error al obtener la lista de libros:", error);
  }
}

async function prestarLibro(id) {
  try {
    const response = await fetch(`/prestar/${id}`);
    if (!response.ok) {
      throw new Error(`Error HTTP! estado: ${response.status}`);
    }
    const data = await response.json();
    console.log(data);
    //Comprobar si la operacion ha tenido exito.
    if (data.success) {
      alert(data.message);
    } else {
      alert(data.message);
    }
    //Actualizar la tabla
    listarLibros();
  } catch (error) {
    console.error("Error al prestar el libro:", error);
  }
}
