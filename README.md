# TP 1 Procesamiento de Imágenes

Primer proyecto de la materia Procesamiento de Imágenes de la Tecnicatura Universitaria en Inteligencia Artificial de la Universidad Nacional de Rosario.

El trabajo práctico busca implementar un ecualizado local del histograma en su primer ejercicio, y una corrección automática de exámenes en su segundo ejercicio.

---

## Estructura del proyecto

```text
ImagenesTP1/
  Ej1/
    tp1Ej1.py                           # Script python de implementación del ejercicio 1
    Imagen_con_detalles_escondidos.tif  # Imagen input del ejercicio
    notas.md                            # Notas al respecto del ejercicio
  Ej2/
    tp1Ej2.py                           # Script python de implementación del ejercicio 2
    examen_1.png
    ...
    examen_5.png                        # 5 exámenes de ejemplo para implementar el ejercicio 2
  TUIA_PDI_TP1_2026_C1.pdf              # Enunciado completo del trabajo práctico
  README.md
  requirements.txt                      # Librerías requeridas para instalar
  .gitignore                            # Ignora __pycache__/ y otros
```


## Instalación del proyecto y creación del entorno virtual

Antes de instalar las dependencias, es necesario crear y activar un entorno virtual.  
A continuación se detalla el procedimiento tanto para Linux como para Windows.

### Crear entorno virtual e instalar dependencias en Linux (Ubuntu / Debian)

Instalar `venv`:

```bash
sudo apt install python3-venv -y
python3 -m venv .venv
```

Desde la carpeta del proyecto:

```bash
python3 -m venv .venv
````

Activar el entorno virtual:

```bash
source .venv/bin/activate
```

Instalar las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

---

### Crear entorno virtual e instalar dependencias en Windows

Desde la carpeta del proyecto, crear el entorno virtual:

```bash
python -m venv .venv
```

o, según la instalación:

```bash
py -3 -m venv .venv
```

Activar el entorno virtual:

Usando PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

O usando CMD:

```cmd
.venv\Scripts\activate.bat
```

Instalar dependencias desde `requirements.txt`:

```bash
pip install -r requirements.txt
```