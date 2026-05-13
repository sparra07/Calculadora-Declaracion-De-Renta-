# Calculadora Declaracion De Renta 

 ###  Creadores

- Carolina Flórez Salazar 
- Samuel Parra Marín
   
---
>La entrevista y la tabla de excel se encuentran en la carpeta llamada "Entrega 1"
---
  ### Persona entrevistada
- **Nombre:** Magnolia Salazar Agudelo 
- **Especialización :** Administracion y Contabilidad 
- **Fecha de la entrevista:** 07/02/2026
---
 ### Interfáz desarrollada por:
 
- Juan David Idarraga Porras 
- Alejandro Tello Giraldo
- Kesman Posso Parra

### Descripción del Proyecto
La función de esta aplicación es transformar la compleja legislación en un proceso de cálculo preciso y fácil de entender para cualquier trabajador. Su objetivo es procesar el ingreso bruto de un empleado y aplicarle en orden jerárquico todos los beneficios y límites legales que permite la DIAN.

---
### Funciones 
-  Depuración Automática (salud y pension)
-  Gestión de beneficios (Hijos o padres)
- Control de topes legales (40% del ingreso neto)
- Validación de datos (Como un asalariado no aprta a la salud)
---

Esta aplicación nos ayuda a tener una herramienta de "empoderamiento financiero y planeación tributaria". Esto quiere decir que convierte a un usuario en el propio dueño de su información tributaria, brindándole la seguridad de sus propios datos y confidencialidad.

---

### Entradas 
- **Ingreso Bruto**: Es el dinero total que el usuario gana antes de cualquier descuento. Es la cifra que aparece en el contrato de trabajo o el total de honorarios recibidos.
- **Aportes ley**: Son los descuentos obligatorios que el estado exige para seguridad social. Sin estos aportes, no se puede calcular la "Renta Líquida".
- **Deducciones**: Son gastos específicos que el usuario ya tiene o inversiones que hace para bajar legalmente la base de sus impuestos. Estas son opcionales pero clave para la optimización.
---
### Definición de Salidas y Cálculo
**Renta Líquida**: Es el dinero real que queda tras los descuentos obligatorios (salud, pensión, etc.).
- Renta Liquida = Ingreso Bruto - Aportes de ley

**Beneficio Real**: Suma las deducciones específicas (salud prepagada, dependientes, intereses de vivienda) y le añade la exención de ley (el 25% de renta exenta sobre el saldo).
- Beneficio Real = Deducciones + ((Renta LIquida - Deducciones) * 0,25)
  
**Límite Legal**: El techo máximo que la ley permite deducir (usualmente el 40%).
- Limite Legal = Renta LIquida * 0.40

Estas tres fórmulas constituyen el algoritmo de optimización de la aplicación. Son los pilares de cálculo que garantizan que el resultado final sea matemáticamente exacto y legalmente viable
- Resultado Total = Renta Liquida - Limite Legal
---
### Caso Especial 
Si el Beneficio real es mayor que el Limite legal eentonces:
- Resultado total = Renta Liquida - Limite legal

Si el Beneficio Real es menor o igual que el limite legal entonces:
- Resultado Total = Renta Liquida - Beneficio Real
---
###  Arquitectura del Sistema
El software está construido bajo un diseño modular en Python, separando las responsabilidades para facilitar el mantenimiento y la escalabilidad:

---


### 1. Capa de Modelo (`Logica_calculadora.py`)
Es el núcleo del sistema e implementa las reglas de negocio:
* **Clase `Impuestos`**: Estructura de datos para el manejo de ingresos, aportes y deducciones.
* **Clase `CalculadoraImpuestos`**: Contiene el algoritmo que calcula la Renta Líquida, Beneficio Real y Límite Legal.
* **Gestión de Excepciones**: Implementa validaciones críticas como `IngresoInvalido`, `AportesObligatorios` y `DeduccionFueraRango`.

---

### 2. Capa de Interfaz (`Consola.py`)
Gestiona la interacción directa con el usuario:
* **Entrada**: Captura datos financieros mediante teclado.
* **Procesamiento**: Ejecuta la lógica dentro de un bloque `try-except` para manejar errores de validación sin cerrar el programa.
* **Salida**: Presenta un desglose detallado de los valores resultantes.
---


### 3. Capa de Pruebas (`test_calculadora.py`)
Garantiza la fiabilidad mediante **Pruebas Unitarias**:
* Verifica escenarios normales, casos de ingresos en cero y validaciones de aportes obligatorios para asalariados.



---
Funcionamiento y Ejecución
---
### Prerrequisitos

Antes de comenzar, asegúrese de tener lo siguiente:

- **Python 3.14.3** instalado en su computador. Si no lo tiene, descárguelo desde python.org.
  > En Windows, durante la instalación marque la casilla **"Add Python to PATH"**
- La carpeta del proyecto descargada (`ej. Calculadora-Declaracion-De-Renta-`)

---
### Opción 1 — Desde la Terminal (CMD / Bash)

**Paso 1 — Abrir la terminal**
- **Windows:** Presione `Win + R`, escriba `cmd` y presione Enter.
- **Mac / Linux:** Busque "Terminal" en su menú de aplicaciones.

**Paso 2 — Ir a la carpeta del proyecto**
Escriba `cd` seguido de la ruta donde guardó el proyecto. 
> Consejo: Escriba `cd ` y arrastre la carpeta hacia la ventana de la terminal.*

**Paso 3 — Ejecutar el programa**
* **Windows:** `python src/Consola.py`
* **Mac / Linux:** `python3 src/Consola.py`

**Paso 4 — Ejecutar las pruebas unitarias**
Para verificar la integridad del código:
* `python -m unittest src/test_calculadora.py`

---

###  Opción 2 — Desde un IDE (VS Code, PyCharm)

1.  **Abrir el proyecto:** Use la opción "Abrir carpeta" y seleccione la raíz del proyecto.
2.  **Seleccionar el intérprete:** Asegúrese de que el entorno reconozca Python 3.14.3
3.  **Ejecutar:** Abra el archivo `src/Consola.py` y presione el botón (Run).
4.  **Pruebas:** Abra `src/test_calculadora.py` y ejecútelo para ver los resultados de los tests.

---

## Cómo ejecutar la aplicación en Visual Studio Code

Siga las siguientes instrucciones para poner en marcha el programa:

### 1. Abrir el proyecto en Visual Studio Code
- Inicie Visual Studio Code.
- Diríjase a **File > Open Folder**.
- Seleccione la carpeta principal del proyecto (donde se encuentran archivos como `app.py`, la carpeta `src`, `build`, entre otros).

### 2. Identificar el archivo de ejecución
El archivo encargado de iniciar la interfaz es:
src/view/payment_gui.py

### 3. Abrir la terminal integrada
- En el menú superior seleccione **Terminal > New Terminal**.
- Confirme que la terminal esté ubicada en la carpeta raíz del proyecto.

### 4. Ejecutar la aplicación
Ingrese el siguiente comando en la terminal:

```bash
python src/view/payment_gui.py
En sistemas donde se utilice python3, ejecute:
python3 src/view/payment_gui.py
