import time
import os

# Funktion zur Abfrage der CPU-Temperatur
def get_cpu_temperature():
    temp = os.popen("vcgencmd measure_temp").readline()
    return temp.replace("temp=", "").replace("'C\n", "")

# Pfad zur Logdatei
log_file_path = "/media/drives/nextcloud/admin/files/Logs/log.txt"

# Hauptschleife
while True:
    # Aktuelle Zeit und Temperatur abrufen
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    cpu_temp = get_cpu_temperature()

    # Log-Eintrag erstellen
    log_entry = f"{current_time} - CPU Temperature: {cpu_temp}°C\n"

    # Log-Eintrag in die Datei schreiben
    with open(log_file_path, "a") as log_file:
        log_file.write(log_entry)

    # 5 Minuten warten
    time.sleep(300)
