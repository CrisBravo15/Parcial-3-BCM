# Parcial-3-BCM
Script para automatización de formularios con pyautogui

# Explicación de uso
Ejecuta el exam_runner.exe y no hagas clic ni presiones ninguna entrada en el teclado para no alterar el proceso de rellenado del formulario

# Explicación de solución
Decidimos que los datos ingresados ya estuvieran dentro del archivo, y que se abriera google chrome mediante la búsqueda de windows porque era más sencillo que usar la propiedad de pyautogui LocateOnScreen, mediante tabs nos fuimos desplazando por todo el formulario y en la parte final de los radiobuttons para no utilizar un click o un enter decidimos utilizar la tecla down que al bajar en las opciones seleccionaría siempre la opción del medio

# Plataforma probada
Prueba ejecutada con Windows 10

# Resolución de pantalla
Resolución de pantalla usada: 1920 x 1080

# Coordenadas utilizadas
No se trabajó con coordenadas

# Equipo y Contribuciones
- Cristian Adan Bravo Guerra: Creación del repositorio junto con el README.md y la investigación de desplazamiento en el formulario
- Bruno Alberto Gonzalez Cuellar: Ayuda a estructurar el código y a organizar las carpetas para el repositorio
- Mikel Eduardo Jonguitud Hernandez: Ayuda a estructurar el código y encargado de escoger los comandos de PowerShell a ejecutar

# Comandos de PowerShell utilizados
Comando "Get-Date" para obtener la fecha.
Comando " Add-Type -AssemblyName System.Speech
    $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer
    $speak.Speak("Equipo BCM, profe pasenos porfa" ". Para poder reproducir un sonido en la computadora del usuario que ejecute el programas

