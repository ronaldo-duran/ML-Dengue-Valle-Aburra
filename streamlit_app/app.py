import joblib
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title='Predicción Hospitalización Dengue', layout='wide')

st.title('Predicción de hospitalización por dengue')
st.caption('Proyecto académico con datos abiertos')

MODEL_PATH = 'best_model_formal_7030.joblib'
COLUMNS_PATH = 'model_input_columns.joblib'

@st.cache_resource
def load_artifacts():
    model = joblib.load(MODEL_PATH)
    columns = joblib.load(COLUMNS_PATH)
    return model, columns

try:
    model, required_columns = load_artifacts()
except Exception as e:
    st.error(f'No se pudieron cargar artefactos: {e}')
    st.info('Asegúrate de ejecutar primero el notebook para generar: best_model_formal_7030.joblib y model_input_columns.joblib')
    st.stop()

st.markdown('### Formulario de ingreso de datos')
st.write('Completa los campos y presiona **Predecir hospitalización**.')

# =========================================================
# Regla de UI:
# - edad_: campo numérico
# - resto de columnas (one-hot/binarias): selector Sí/No
# =========================================================
feature_values = {}

with st.form('form_prediccion'):
    st.markdown('#### Datos del paciente')

    for column_name in required_columns:
        if column_name == 'edad_':
            feature_values[column_name] = st.number_input(
                'Edad',
                min_value=0,
                max_value=120,
                value=30,
                step=1
            )
        else:
            selected_option = st.selectbox(
                f'{column_name} (Sí/No)',
                options=['No', 'Sí'],
                index=0
            )
            feature_values[column_name] = 1 if selected_option == 'Sí' else 0

    submit_prediction = st.form_submit_button('Predecir hospitalización')

if submit_prediction:
    input_df = pd.DataFrame([feature_values], columns=required_columns)
    prediction_binary = model.predict(input_df)[0]
    prediction_text = 'Hospitalización: Sí' if prediction_binary == 1 else 'Hospitalización: No'

    st.markdown('### Resultado')
    st.success(prediction_text)

    st.markdown('#### Registro ingresado')
    st.dataframe(input_df, use_container_width=True)

    result_df = input_df.copy()
    result_df['pred_binaria'] = prediction_binary
    result_df['pred_interpretacion'] = prediction_text

    csv_out = result_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label='Descargar resultado CSV',
        data=csv_out,
        file_name='prediccion_individual_dengue.csv',
        mime='text/csv'
    )

st.markdown('---')
st.write('Modelo usado: best_model_formal_7030.joblib')