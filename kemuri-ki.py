import psutil
import time
import smtplib
import imaplib
import email
import socket
import requests
import speech_recognition as sr
import pyttsx3
from email.mime.text import MIMEText

class KIManager:
    def __init__(self):
        self.features = [
            {"name": "Basis KI-Funktionalität", "cpu": 10, "ram": 200},
            {"name": "Erweiterte Kommunikation", "cpu": 15, "ram": 300},
            {"name": "Sicherheitssysteme", "cpu": 20, "ram": 400},
            {"name": "Autonome Entscheidungsfindung", "cpu": 25, "ram": 500},
            {"name": "Cyberabwehr & Täuschungssysteme", "cpu": 30, "ram": 600},
            {"name": "Selbstheilende Netzwerke", "cpu": 35, "ram": 700},
            {"name": "Neuronale Anpassung & Deep Learning", "cpu": 40, "ram": 800},
            {"name": "Quantenverschlüsselung & Blockchain-Sicherheit", "cpu": 45, "ram": 900},
            {"name": "Globale Bedrohungsanalyse & Satellitenüberwachung", "cpu": 50, "ram": 1000},
            {"name": "Adaptive Drohnensteuerung & Physiksimulation", "cpu": 55, "ram": 1100},
            {"name": "Dezentrale KI-Netzwerke", "cpu": 20, "ram": 300},
            {"name": "Dynamische Abo-Modelle für Nutzer", "cpu": 25, "ram": 350},
            {"name": "KI-gesteuerte Intrusion Detection", "cpu": 30, "ram": 400},
            {"name": "Dynamische Cloud-Integration", "cpu": 35, "ram": 500},
            {"name": "Adaptive Task-Priorisierung", "cpu": 40, "ram": 600},
            {"name": "Unterstützung für IoT & Smart Home", "cpu": 30, "ram": 350},
            {"name": "Sprachkommunikation & Echtzeit-Übersetzung", "cpu": 20, "ram": 300}
        ]
        self.active_features = []
        self.email_account = "rauch91steven@gmail.com"
        self.email_password = "DEIN_PASSWORT"  # Sicher speichern, nicht im Klartext!
        self.smtp_server = "smtp.gmail.com"
        self.imap_server = "imap.gmail.com"
        self.server_nodes = ["server1.example.com", "server2.example.com"]  # Liste der vernetzten Server
        self.pay_accounts = {"basic": 1, "premium": 5, "enterprise": 10}  # Berechtigungsstufen
        self.admin_accounts = ["rauch91steven@gmail.com", "cybercore.ki@kemuri-ki-net.com"]  # Master-Admin mit voller Kontrolle
        
        # Initialisierung der Sprachsteuerung
        self.speech_recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()
    
    def check_resources(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        available_memory = psutil.virtual_memory().available / (1024 * 1024)  # MB
        return cpu_usage, available_memory
    
    def activate_features_dynamically(self, account_type="admin"):
        print("Dynamische Aktivierung basierend auf Bedarf und Ressourcen...")
        max_features = self.pay_accounts.get(account_type, 0) if account_type != "admin" else len(self.features)
        while True:
            cpu_usage, available_memory = self.check_resources()
            activated_count = 0
            for feature in self.features:
                if activated_count >= max_features:
                    break
                if feature["name"] not in self.active_features and cpu_usage < 80 and available_memory > feature["ram"]:
                    self.active_features.append(feature["name"])
                    print(f"Aktiviere: {feature['name']}")
                    activated_count += 1
                    time.sleep(2)  # Simulierte Ladezeit
            
            for feature in self.active_features[:]:
                if cpu_usage > 85 or available_memory < 100:
                    self.active_features.remove(feature)
                    print(f"Deaktiviere: {feature}")
            
            time.sleep(5)  # Zyklische Überprüfung der Systemressourcen
    
    def text_to_speech(self, text):
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()
    
    def speech_to_text(self):
        with sr.Microphone() as source:
            print("Sprich jetzt...")
            audio = self.speech_recognizer.listen(source)
            try:
                return self.speech_recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                return "Ich konnte das nicht verstehen."
            except sr.RequestError:
                return "Fehler bei der Verbindung zur Spracherkennung."
    
    def run(self, account_type="admin"):
        print("Starte KI-System...")
        self.activate_features_dynamically(account_type)
        self.text_to_speech("Das KI-System wurde erfolgreich gestartet und läuft jetzt.")

if __name__ == "__main__":
    ki_manager = KIManager()
    ki_manager.run(account_type="admin")
