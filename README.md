# 🌍 Aplicación End-to-End de Calidad del Aire con Machine Learning y FastAPI

Proyecto integrador para el monitoreo, análisis espacial y predicción de la calidad del aire en la provincia de Manabí, Ecuador.

---

## 🛠️ Tecnologías Utilizadas
* **Backend:** FastAPI, Uvicorn, Pydantic
* **Base de Datos:** Supabase (PostgreSQL) para datos espaciales
* **Machine Learning:** Scikit-Learn, Joblib, NumPy, Pandas
* **Frontend / Dashboard:** HTML5, TailwindCSS, Leaflet.js (Mapas) y Plotly.js (Gráficos)

---

## 📊 Conceptos de Machine Learning Evaluados

### 1. Algoritmos Entrenados
* **Supervisado:** *Random Forest Regressor* para predecir concentraciones de Monóxido de Carbono (CO).
* **No Supervisado:** *K-Means Clustering* para agrupar estaciones según su nivel de riesgo de contaminación.

### 2. Métodos de Evaluación y Validación
* **Método de Retención (Hold-out):** División de los datos en 80% entrenamiento y 20% prueba para medir el rendimiento general del modelo.
* **Validación Cruzada (K-Folds CV):** Implementación de 5 particiones (*5-Folds*) para garantizar estabilidad en las métricas (RMSE, R²).

### 3. Control de Calidad del Modelo
* Ajuste de hiperparámetros (profundidad máxima, número de estimadores) para evitar **Overfitting** (sobreajuste) y **Underfitting** (subajuste).

---

## 📂 Estructura del Repositorio
* `main.py` - Servidor Backend y endpoints con FastAPI.
* `index.html` - Dashboard interactivo (Mapa espacial, gráficos y predicción).
* `modelo_supervisado.pkl` - Modelo Random Forest exportado.
* `modelo_nosupervisado.pkl` - Modelo K-Means exportado.
* `requirements.txt` - Librerías requeridas.
* `README.md` - Documentación oficial del proyecto.

---

## 🚀 Instrucciones de Ejecución Local
1. Instalar las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt