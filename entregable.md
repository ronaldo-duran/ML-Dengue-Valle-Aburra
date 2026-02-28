# METODOLOGÍA CRISP-DM

## 1. ENTENDIMIENTO DEL NEGOCIO (0.5 unidad)

### 1.1 Descripción del negocio  
### 1.2 Descripción del problema  
### 1.3 Objetivos de la minería  
### 1.4 Diseño de solución  

| Tipo de análisis | Tipo de aprendizaje | Posibles métodos | Evaluación |
|------------------|--------------------|------------------|------------|
| Predictivo       | Supervisado        | KNN, MLP         | MAE, MAPE  |

---

## 2. ENTENDIMIENTO DE LOS DATOS (0.5 unidad)

### 2.1 Diccionario de datos

| Variable | Descripción | Tipo de variable (numérica / categórica) | Variable de entrada o salida |
|----------|------------|-------------------------------------------|-------------------------------|

### 2.2 Reglas de calidad

#### Variables numéricas

| Variable | Valor mínimo | Valor máximo |
|----------|--------------|--------------|

#### Variables categóricas

| Variable | Valores posibles |
|----------|------------------|

---

## 3. PREPARACIÓN DE DATOS (1 unidad)

### 3.1 Selección de variables  
### 3.2 Descripción estadística  
### 3.3 Limpieza de atípicos  
(Imputación o borrado de variables con errores)

### 3.4 Limpieza de nulos  
(Imputación o borrado de campos nulos)

### 3.5 Creación de nuevas variables (si es necesario)  

### 3.6 Análisis de relaciones  
- Análisis lineal  
- Análisis no lineal  

### 3.7 Reducción de dimensiones  
(Según el análisis anterior y/o con PCA)

### 3.8 Balanceo  
(Para ejercicios de clasificación)

---

## 4. MODELAMIENTO Y EVALUACIÓN (1 unidad)

### 4.1 Configuración y selección de métodos de Machine Learning  

#### 4.1.1 Selección de 5 modelos de Machine Learning clásico  
#### 4.1.2 Selección de 3 modelos de ensambles  
- Uno de votación  
- Uno de bagging  
- Uno de boosting  

### 4.2 Ajuste de hiperparámetros con el 70% de los datos haciendo Cross Validation  

#### 4.2.1 Justificación de selección de la métrica de desempeño  
#### 4.2.2 Ajuste de hiperparámetros de los modelos de Machine Learning clásico  
#### 4.2.3 Ajuste de hiperparámetros de los dos modelos de ensamble  

### 4.3 Medida de calidad del modelo  

#### 4.3.1 Evaluación de los modelos con el set de pruebas  
#### 4.3.2 Selección del modelo con mejor desempeño  

---

## 5. DESPLIEGUE (2 unidades)

### 5.1 Predicción de datos futuros  
(Utilice su modelo para hacer una predicción con datos que no haya utilizado)

### 5.2 Construya un conjunto de datos de entrada para hacer predicciones con el modelo  

### 5.3 Prepare el conjunto de datos nuevo  

### 5.4 Realice la predicción con los datos de entrada nuevos y presente la predicción, interpretando el resultado  

### 5.5 Usando Streamlit y Streamlit.io construya una aplicación web y despliéguela  
- Imprima un pantallazo de la aplicación funcionando  
- Adjunte la URL a este trabajo  