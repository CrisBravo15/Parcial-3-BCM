import subprocess 
import pyautogui
from datetime import datetime 
from pathlib import Path

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

def fill_form(data): 

    # Abrir chrome y entrar al formulario
    pyautogui.press('win')
    pyautogui.typewrite("google chrome")
    pyautogui.PAUSE = 2

    pyautogui.press('enter')
  
    # Link del formulario
    pyautogui.typewrite("https://forms.office.com/pages/responsepage.aspx?id=EZDKymp73kSGHwlaLKiDt4wXC_YfIWlGrUcWrbkA4-NURjFZQjdBMkJNSlkwQkVCM0c2V0cyWTVHNSQlQCNjPTEu&classId=31f16070-5361-4de8-9624-98f60a6f24ae&assignmentId=c865c317-1511-4faa-8a46-565ecf1dd392&submissionId=bba50a75-6a1b-7a54-a1d6-b7b07cf7a9fc&route=shorturl")
    pyautogui.press("enter")

    take_screenshot("before")
    pyautogui.PAUSE = 1.2

    pyautogui.press("tab") 
    pyautogui.typewrite(data["fecha"]) 
    pyautogui.PAUSE = 1.2
    pyautogui.press("tab") 

    for i in range(3):
        pyautogui.typewrite(data["nombres"][i])
        pyautogui.press("enter") 
        pyautogui.PAUSE = 1.2
        
    pyautogui.press("tab") 
    pyautogui.typewrite(data["suma"]) 
    pyautogui.PAUSE = 1.2
    pyautogui.press("tab")
    take_screenshot("during")
    pyautogui.press("down") 
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.PAUSE = 2
    take_screenshot("after") 

pyautogui.FAILSAFE = True 
