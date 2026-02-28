# App Streamlit - Predicción de hospitalización por dengue

## Ejecutar local

1. Ubícate en la raíz del proyecto.
2. Instala dependencias:

```bash
pip install -r streamlit_app/requirements.txt
```

3. Ejecuta la app:

```bash
streamlit run streamlit_app/app.py
```

## Requisitos de artefactos

La app requiere estos archivos en la raíz del proyecto:
- `best_model_formal_7030.joblib`
- `model_input_columns.joblib`

## Modo de uso

- La aplicación muestra un formulario para ingresar los datos del paciente.
- `edad_` se ingresa como campo numérico.
- Las columnas binarias/categóricas codificadas se diligencian con selector Sí/No.
- Al enviar, la app devuelve si el caso requiere hospitalización o no.

## Despliegue en Streamlit Community Cloud

1. Sube el proyecto a un repositorio de GitHub.
2. Entra a https://share.streamlit.io/ e inicia sesión.
3. Crea una nueva app seleccionando:
   - Repo: tu repositorio
   - Branch: principal
   - Main file path: `streamlit_app/app.py`
4. En *Advanced settings*, valida que use `streamlit_app/requirements.txt`.
5. Despliega y copia la URL pública para anexarla al entregable.
