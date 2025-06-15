# FabLab-Machine-Learning-

# Detección de Rostros con Robot NAO

## Objetivo

Implementar y demostrar la integración de un modelo de IA en el robot NAO para que sea capaz de detectar el número de rostros presentes frente a su cámara y realizar una acción basada en este resultado: anunciar el número de rostros detectados mediante síntesis de voz. Este proyecto ejemplifica cómo un agente inteligente (el robot NAO) puede ejecutar acciones en respuesta a resultados obtenidos por modelos de IA.

## Arquitectura de Componentes

El sistema se compone de los siguientes elementos:

### 1. Usuario
- **Descripción:** Una o más personas se posicionan frente al robot NAO, quien será el objetivo de la detección de rostros.

### 2. Robot NAO
- **ALVideoDevice:** Encargado de capturar imágenes utilizando la cámara del robot.
- **ALTextToSpeech:** Permite al robot anunciar por voz el número de rostros detectados.
- **vision_definitions:** Módulo de la API de NAOqi para definir parámetros de captura de imagen y configuración de la cámara.

### 3. Computadora Cliente
- **Script Python:**  
  - **Comunicación con NAO:** Usa `ALProxy` para establecer conexión remota con el robot y acceder a sus módulos (`ALVideoDevice`, `ALTextToSpeech`).
  - **Captura y Procesamiento de Imagen:** Solicita una imagen a NAO, la recibe en formato RAW, la transforma y procesa.
  - **Librerías utilizadas:**
    - `cv2` (OpenCV): Para el procesamiento y la detección de rostros mediante clasificadores Haar Cascade.
    - `numpy`: Para manipulación de arrays y procesamiento de la imagen.
    - `PIL` (Pillow): Para convertir los datos de imagen recibidos en formatos compatibles.
    - `vision_definitions`: Proporciona constantes para especificar el formato de imagen y otros parámetros relacionados a la cámara de NAO.
    - `time`: Para manejar temporizadores y demoras entre capturas.
  - **Clasificación de rostros:** Detecta cuántos rostros hay en la imagen usando OpenCV.
  - **Acción:** Informa el número de rostros al robot, que lo comunica en voz alta mediante `ALTextToSpeech`.   

La comunicación entre la computadora cliente y el robot NAO se realiza a través de la red TCP/IP.

## Instrucciones de Instalación y Ejecución

### Requisitos previos

- Robot NAO físico o simulador NAOqi
- Acceso a la red local entre la computadora y el robot
- Python 2.7 (por compatibilidad con NAOqi SDK)
- Paquetes de python requeridos: 
    - `naoqi`, `opencv-python`, `numpy`, `pillow`
    - *(`vision_definitions` viene incluido en el SDK de NAOqi, no se instala por pip)*
    

### 1. Clonar el repositorio

```bash
git clone https://github.com/KarimS21/FabLab-Machine-Learning-.git
cd FabLab-Machine-Learning-
```

### 2. Instalar dependencias en la computadora cliente

- Recomendado : usar un entorno virtual
```bash
pip install opencv-python numpy Pillow
# Instala NAOqi SDK manualmente según tu sistema operativo:
# http://doc.aldebaran.com/2-5/dev/python/install_guide.html
```

### 3. Configurar la IP del robot
En el script CLASIFICADOR.py, reemplaza la variable de IP (robot_ip) por la dirección IP de tu robot NAO.

### 4. Ejecutar el Script
```bash
python CLASIFICADOR.py
```

### 5. Interactuar con el Robot 
- Posiciónate (o coloca varias personas) frente al robot.
- El robot capturará una imagen, detectará el número de rostros y lo anunciará por voz.

## Video demostrativo
https://youtu.be/kzNfD35hg5U

## Autores

- **Daniel Ivan Carbajal Robles** — *u20221b751*
- **Mildred Micaela Marchan Quispe** — *u202213292*
- **Nicolás Francisco Miranda Rafael** — *u202216895*
- **Rosa Maria Rodríguez Valencia** — *u202212675*
- **Karim Wagner Samanamud Mosquera** — *u201816862*
- **Ian Joaquin Sanchez Alva** — *u202124676*
- **Joge Sebastian Valdivia Peceros** — *u202212452*
- **Joaquín Eduardo Velarde Leyva** — *u202212510*

---

**Curso:** Machine Learning – CC57  
**Universidad Peruana de Ciencias Aplicadas – FabLab Monterrico**  
**Junio 2025**

