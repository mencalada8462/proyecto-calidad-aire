from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
from supabase import create_client, Client

# Inicializar FastAPI
app = FastAPI(title="API Espacial - Calidad del Aire")

# Permitir que el Frontend (Dashboard) se comunique con esta API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------
# 1. CONEXIÓN A SUPABASE
# ---------------------------------------------------------
# Reemplaza esto con tu URL exacta
SUPABASE_URL = "https://oeamxrzljgcynsBphybq.supabase.co" 
# Reemplaza esto con tu Clave Publicable (sb_publicable_...)
SUPABASE_KEY = sb_publishable_6JMxoT3BjxZL5owvcpV9Lg_qjIh_4Am 

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---------------------------------------------------------
# 2. CARGAR EL MODELO DE MACHINE LEARNING
# ---------------------------------------------------------
modelo_rf = joblib.load("modelo_supervisado.pkl")

# Definir la estructura de datos que el usuario enviará
class DatosMeteorologicos(BaseModel):
    Dioxido_Nitrogeno: float
    Temperatura: float
    Humedad: float
    Latitud: float
    Longitud: float

# ---------------------------------------------------------
# 3. RUTAS DE LA API (ENDPOINTS)
# ---------------------------------------------------------
@app.get("/")
def inicio():
    return {"mensaje": "¡Hola, profesor! La API está funcionando correctamente."}

@app.get("/datos-espaciales")
def obtener_datos():
    """Consulta la base de datos en Supabase y devuelve las coordenadas"""
    respuesta = supabase.table("calidad_aire").select("*").limit(100).execute()
    return respuesta.data

@app.post("/predecir")
def predecir_contaminacion(datos: DatosMeteorologicos):
    """Recibe datos del dashboard y devuelve la predicción del modelo"""
    entrada = np.array([[
        datos.Dioxido_Nitrogeno, 
        datos.Temperatura, 
        datos.Humedad, 
        datos.Latitud, 
        datos.Longitud
    ]])
    prediccion = modelo_rf.predict(entrada)
    
    return {
        "prediccion_Monoxido_Carbono": round(float(prediccion[0]), 2),
        "mensaje": "Predicción realizada con éxito"
    }