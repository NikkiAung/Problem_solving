import webbrowser
import time
import subprocess

def main():
    # 1. Open Zoom link
    zoom_link = "https://ccsf-edu.zoom.us/j/92121773277"
    webbrowser.open(zoom_link)
    
    # 2. Wait until 10 AM (or 1 hour)
    #    For a 9-10 session, wait for 3600 seconds
    time.sleep(20)
    
    # 3. Leave by killing Zoom
    #    Windows
    #    subprocess.call(["taskkill", "/f", "/im", "Zoom.exe"])
    #    macOS/Linux
    subprocess.call(["pkill", "zoom"])

if __name__ == "__main__":
    main()
