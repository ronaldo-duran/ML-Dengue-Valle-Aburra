# Predicción de Hospitalización por Dengue (ML)

## Descripción
Este proyecto desarrolla un modelo de *Machine Learning* para predecir si una persona es candidata a hospitalización por dengue, a partir de síntomas clínicos, variables demográficas y variables geográficas.

Se realiza con fines académicos, utilizando datos abiertos.

## Objetivo
Construir y comparar múltiples modelos de clasificación para seleccionar el mejor desempeño en la predicción de la variable objetivo `pac_hos_`.

## Alcance técnico
- Limpieza y depuración de datos.
- Tratamiento de valores faltantes.
- Codificación de variables categóricas.
- Balanceo de clases con SMOTE.
- Hiperparametrización por modelo con `GridSearchCV` y validación cruzada estratificada.
- Comparación de modelos con métrica principal `F1-macro`.
- Exportación del mejor modelo entrenado.

## Modelos evaluados
1. Regresión logística
2. Árbol de decisión
3. KNN
4. SVM
5. XGBoost
6. Random Forest
7. Red neuronal (MLP)

## Resultado actual
De acuerdo con la ejecución registrada en el notebook, el mejor modelo global fue **XGBoost**, con desempeño superior en `F1-macro` frente al resto de modelos comparados.

## Estructura del proyecto
- `ML_Dengue_Notebook.ipynb`: notebook principal con todo el flujo de datos, entrenamiento y comparación.
- `dengue_mod.csv`: dataset base.
- `label_encoder_target.joblib`: codificador de la variable objetivo.
- `best_model_global.joblib`: mejor modelo exportado.

## Requisitos
- Python 3.9+
- Bibliotecas principales:
  - pandas
  - numpy
  - scikit-learn
  - imbalanced-learn
  - xgboost
  - matplotlib
  - seaborn

## Ejecución recomendada
1. Abrir `ML_Dengue_Notebook.ipynb`.
2. Ejecutar celdas en orden.
3. Verificar la tabla de ranking final de modelos.
4. Usar `best_model_global.joblib` para inferencia.

## Notas
- El proyecto está orientado a análisis y validación académica.
- El desempeño puede variar según versión de librerías, semilla y entorno de ejecución.