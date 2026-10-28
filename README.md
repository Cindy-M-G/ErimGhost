# ErimGhost
# 🧟 ErimGhost (Track A: Escape de Manta Zombie)

Motor de rutas inteligente en tiempo real para evacuación y supervivencia en Manta durante la SpookyThon 2026 (ULEAM).

## 🚀 Qué hace el proyecto
ErimGhost funciona como la radio de emergencia de los sobrevivientes. A través de un grafo optimizado de la ciudad de Manta (intersecciones y calles), calcula paso a paso la ruta más segura hacia los refugios, recalculando dinámicamente el camino ante bloqueos viales y el avance imprevisto de hordas zombis.

## ⚙️ Stack Tecnológico
* **Lenguaje:** Python 3.x
* **Framework:** FastAPI
* **Lógica de Grafos:** NetworkX (Algoritmo A*)
* **Validación de Datos:** Pydantic
* **Despliegue AWS:** (Indica aquí si usaste API Gateway + Lambda o App Runner/ECS Fargate)

## 📡 Contrato Técnico (API)
El sistema expone el endpoint obligatorio protegido por cabecera:
* **POST /paso**
* **Header:** `x-api-key: manta-zombie-secret-key`
* **Payload de Ejemplo:**
  ```json
  {
    "sobrevivienteId": "S-0089",
    "nodoActual": "N-0117",
    "turno": 142
  }









  # 🧟 ErimGhost — Motor de Rutas de Evacuación Zombie (Track A)
**SpookyThon 2026 · ULEAM Manta**

ErimGhost es un motor de evacuación inteligente en tiempo real diseñado para guiar a los sobrevivientes hacia los refugios más cercanos en la ciudad de Manta durante un apocalipsis zombie.

---

## 🎯 Características Principales
* **Algoritmo A* Dinámico:** Recalcula el camino más corto considerando distancia y velocidad por tipo de calle (avenida, calle, callejón, puente).
* **Evitación de Hordas:** Detecta nodos infestados por hordas y bloquea automáticamente el nodo y sus intersecciones vecinas.
* **Respuesta en Tiempo Real:** Latencia promedio `< 50ms` para cumplir holgadamente con el requisito de `< 500ms`.
* **Autenticación:** Seguridad mediante cabecera personalizada `x-api-key`.

---

## 🛠️ Requisitos e Instalación Local

### Clonar el repositorio
```bash
git clone [https://github.com/tu-usuario/erimghost-manta-zombie.git](https://github.com/tu-usuario/erimghost-manta-zombie.git)
cd erimghost-manta-zombie




# 🧟 ErimGhost — Motor de Rutas de Evacuación Zombie (Track A)
**SpookyThon 2026 · ULEAM Manta**

ErimGhost es un motor de rutas en tiempo real diseñado para la evacuación en Manta. Utiliza FastAPI y el algoritmo A* de NetworkX para calcular el paso a paso hacia el refugio más cercano, evitando hordas y bloqueos.

## 🚀 Ejecución Local
```bash
pip install -r requirements.txt
python main.py


```mermaid
graph TD
    User[Sobreviviente / Cliente Web] -->|HTTP POST /paso| ALB[AWS App Runner / ALB]
    ALB -->|Ruta en tiempo real| API[FastAPI Engine - Python 3.10]
    API -->|Algoritmo A* + Grafos| NX[NetworkX Graph Engine]
    API -->|Consola de Monitoreo| CW[AWS CloudWatch & Budgets]



---

### 2. Pegar la Declaración de Costos en tu `README.md`
Pega esta sección exacta al final de tu `README.md`:

```markdown
## Declaración de Costos (AWS)

* **Costo Estimado Mensual en Producción:** ~$8.00 USD / mes (AWS App Runner 0.25 vCPU / 0.5 GB RAM + CloudWatch).
* **Costo Real Gastado durante el Evento:** $0.00 USD (Cubierto bajo AWS Free Tier / Créditos).
