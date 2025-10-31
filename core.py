import subprocess 
import pyautogui
import os
import sys
from datetime import datetime 
from pathlib import Path

# Funcion agregada al código para guardar la imagen al .exe
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def run_powershell(cmd): 
    try: 
        result = subprocess.run(["powershell", "-Command", cmd], 
        capture_output=True, text=True, timeout=10) 
        return result.returncode, result.stdout.strip(), result.stderr.strip() 
    except Exception as e: 
        return 1, "", str(e) 
    
def take_screenshot(name): 
    out = Path("out") 
    out.mkdir(exist_ok=True) 
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ") 
    path = out / f"{name}_{ts}.png" 
    img = pyautogui.screenshot() 
    img.save(path) 
    return path 

# Función para escoger el equipo favorito
def find_img(img = "imgs/campo.png"):
    campo = resource_path(img)
    try:
        box = pyautogui.locateOnScreen(campo, confidence=0.7, grayscale=True)

        if box:
            center = pyautogui.center(box)
            pyautogui.click(center)
            if img == "imgs/campo.png":
                pyautogui.press("enter")

    except pyautogui.ImageNotFoundException:
        return "error"

def fill_form(data): 
    # Abrir chrome y entrar al link
    pyautogui.press('win')
    pyautogui.typewrite("google chrome")
    pyautogui.PAUSE = 2

    pyautogui.press('enter')
    pyautogui.typewrite("https://forms.office.com/pages/responsepage.aspx?id=EZDKymp73kSGHwlaLKiDt4wXC_YfIWlGrUcWrbkA4-NURjFZQjdBMkJNSlkwQkVCM0c2V0cyWTVHNSQlQCNjPTEu&classId=31f16070-5361-4de8-9624-98f60a6f24ae&assignmentId=c865c317-1511-4faa-8a46-565ecf1dd392&submissionId=bba50a75-6a1b-7a54-a1d6-b7b07cf7a9fc&route=shorturl")
    pyautogui.press("enter")

    take_screenshot("before")
    pyautogui.PAUSE = 1.5

    # Encontrar posición inicial
    find_img()

    pyautogui.PAUSE = 1.5
    pyautogui.press("tab") 

    for i in range(3):
        pyautogui.typewrite(data["nombres"][i])
        pyautogui.press("enter") 
        pyautogui.PAUSE = 1.2
        
    pyautogui.press("tab") 
    pyautogui.typewrite(data["suma"]) 
    pyautogui.PAUSE = 1.7
    take_screenshot("during")
    pyautogui.press("tab") 

    # Parte de RadioButtons
    if data["equipo"].lower() == "marvel":
        find_img("imgs/marvel.png")
    elif data["equipo"].lower() == "dc":
        find_img("imgs/dc.png")
    else:
        find_img("imgs/ninguno.png")

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.PAUSE = 2
    take_screenshot("after") 


pyautogui.FAILSAFE = True 