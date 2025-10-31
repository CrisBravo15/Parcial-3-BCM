import logging 
import datetime
import core

def main(): 
    logging.basicConfig(filename="run.log", level=logging.INFO, 
    format="%(asctime)s %(levelname)s %(message)s", encoding="utf-8") 
    logging.info("Inicio del examen") 

    data = { 
        "fecha": "30/10/2025", 
        "nombres": ["Cristian Adan Bravo Guerra",
                    "Bruno Alberto Gonzalez Cuellar",
                    "Mikel Eduardo Jonguitud Hernandez"],
        "suma": str(2115406 + 2116526 + 2116525),
        "equipo": "Ninguno"
    } 

    command = r'''
    Add-Type -AssemblyName System.Speech
    $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer
    $speak.Speak("Equipo BCM, profe pasenos porfa")
    '''

    code, out, err = core.run_powershell("Get-Date") 
    logging.info(f"PS code: {code}") 
    logging.info(f"PS output: {out}") 
    logging.info(f"PS error: {err}")
    code, out, err = core.run_powershell(command)
    logging.info(f"PS code: {code}") 
    logging.info(f"PS output: {out}") 
    logging.info(f"PS error: {err}")

    res = core.fill_form(data) 
    if res == "error":
        logging.error("Error al encontrar la imagen")

    logging.info("Fin del examen") 

if __name__ == "__main__": 
    main()