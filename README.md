# Parcial-3-BCM
Script para automatización de formularios con pyautogui

# Explicación de uso
Ejecuta el exam_runner.exe y no hagas clic ni presiones ninguna entrada en el teclado para no alterar el proceso de rellenado del formulario

# Explicación de solución
Primero encontramos la imagen usando la libreria **pyautogui** y su función *locateOnScreen* y le damos una imagen de cómo se ve el input inicial y ahi seguimos introduciendo los datos mediante la data que está declarada en el archivo runner y nos fuimos desplazando a traves del 'tab' hasta llegar a la parte de los RadioButtons donde volvimos a utilizar lo mismo que al principio y si la data decía que equipo era ninguno buscaba la imagen y le daba clic sobre la opción

# Plataforma probada
Prueba ejecutada con Windows 10

# Resolución de pantalla
Resolución de pantalla usada: 1920 x 1080

# Coordenadas utilizadas
No se trabajó con coordenadas

# Equipo y Contribuciones
- Cristian Adan Bravo Guerra: Creación del repositorio junto con el README.md, la investigación de desplazamiento en el formulario, creación de nuevas funciones para saber en qué área introducir datos
- Bruno Alberto Gonzalez Cuellar: Ayuda a estructurar el código y a organizar las carpetas para el repositorio
- Mikel Eduardo Jonguitud Hernandez: Ayuda a estructurar el código y encargado de escoger los comandos de PowerShell a ejecutar

# Comandos de PowerShell utilizados
Comando "Get-Date" para obtener la fecha.
Comando " Add-Type -AssemblyName System.Speech
    $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer
    $speak.Speak("Equipo BCM, profe pasenos porfa" ". Para poder reproducir un sonido en la computadora del usuario que ejecute el programas

