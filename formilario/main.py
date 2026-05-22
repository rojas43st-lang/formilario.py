from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.responses import FileResponse

app = FastAPI()

# Ruta principal
@app.get("/", response_class=HTMLResponse)
def inicio():

    return FileResponse("index.html")

# Ruta captura información
@app.post("/login")
def login(
    usuario: str = Form(...),
    password: str = Form(...)
):

    # Validar contraseña
    if password == "1234":

        return HTMLResponse(
            f"<h1>Bienvenido {usuario}</h1>"
        )

    else:

        return RedirectResponse(
            url="/",
            status_code=303
        )