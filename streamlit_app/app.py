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
    st.stop()

st.markdown('### Cargar datos para predicción')
st.write('Sube un CSV con las mismas columnas de entrada del modelo entrenado.')

uploaded = st.file_uploader('Archivo CSV de entrada', type=['csv'])

if uploaded is not None:
    input_df = pd.read_csv(uploaded)
    st.markdown('#### Vista previa del archivo cargado')
    st.dataframe(input_df.head(), use_container_width=True)

    prepared_df = input_df.reindex(columns=required_columns, fill_value=0)

    if st.button('Predecir'):
        pred_binary = model.predict(prepared_df)
        pred_text = np.where(pred_binary == 1, 'Hospitalización: Sí', 'Hospitalización: No')

        output_df = input_df.copy()
        output_df['pred_binaria'] = pred_binary
        output_df['pred_interpretacion'] = pred_text

        st.markdown('#### Resultados')
        st.dataframe(output_df, use_container_width=True)

        csv_out = output_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label='Descargar resultados CSV',
            data=csv_out,
            file_name='predicciones_dengue.csv',
            mime='text/csv'
        )
else:
    st.info('Sube un archivo CSV para ejecutar predicciones.')

st.markdown('---')
st.write('Modelo usado: best_model_formal_7030.joblib')