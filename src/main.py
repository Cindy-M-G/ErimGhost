from fastapi import FastAPI, Header, HTTPException, status
from pydantic import BaseModel
from typing import Dict, Set, Tuple
from src.graph import MantaGraph

app = FastAPI(title="Manta Zombie Escape API", version="1.0.0")

# API Key requerida por el contrato técnico del reto
API_KEY_SECRETA = "manta-zombie-secret-key"

# Instancia global del grafo de Manta (mantenido en memoria de la app)
manta_grafo = MantaGraph()

# Estado en memoria para obstáculos dinámicos y refugios de sobrevivientes
aristas_bloqueadas: Set[Tuple[str, str]] = set()
nodos_horda: Set[str] = set()
sobrevivientes_refugio: Dict[str, str] = {}  # sobrevivienteId -> nodo_refugio

def inicializar_mapa_base():
    """Carga inicial de nodos de prueba y refugios para Manta."""
    nodos_ejemplo = [
        ("N-0100", -0.9500, -80.7000),
        ("N-0117", -0.9550, -80.7050),
        ("N-0118", -0.9560, -80.7060),
        ("N-0200", -0.9600, -80.7100),  # Nodo Refugio
    ]
    for nid, lat, lng in nodos_ejemplo:
        manta_grafo.agregar_nodo(nid, lat, lng)
    
    # Agregar conexiones (aristas) con su respectiva distancia y tipo
    manta_grafo.agregar_arista("N-0100", "N-0117", 150.0, "calle")
    manta_grafo.agregar_arista("N-0117", "N-0118", 100.0, "avenida")
    manta_grafo.agregar_arista("N-0118", "N-0200", 200.0, "calle")
    
    # Registrar refugios oficiales
    manta_grafo.refugios = ["N-0200"]

# Inicializar al arrancar el servidor
inicializar_mapa_base()

class PasoRequest(BaseModel):
    sobrevivienteId: str
    nodoActual: str
    turno: int

class PasoResponse(BaseModel):
    siguienteNodo: str

@app.post("/paso", response_model=PasoResponse)
def calcular_paso(
    payload: PasoRequest, 
    x_api_key: str = Header(None)
):
    # Validación estricta de seguridad por cabecera
    if x_api_key != API_KEY_SECRETA:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key inválida o no proporcionada"
        )
    
    s_id = payload.sobrevivienteId
    nodo_actual = payload.nodoActual

    # Asignar automáticamente un refugio al sobreviviente si es su primera vez en el turno
    if s_id not in sobrevivientes_refugio:
        if manta_grafo.refugios:
            sobrevivientes_refugio[s_id] = manta_grafo.refugios[0]
        else:
            return PasoResponse(siguienteNodo=nodo_actual)

    destino = sobrevivientes_refugio[s_id]

    # Calcular el siguiente nodo seguro utilizando el motor de grafos
    siguiente_nodo = manta_grafo.calcular_siguiente_paso(
        nodo_actual=nodo_actual,
        nodo_destino=destino,
        aristas_bloqueadas=aristas_bloqueadas,
        nodos_horda=nodos_horda
    )

    return PasoResponse(siguienteNodo=siguiente_nodo)