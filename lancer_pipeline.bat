@echo off
:: 1. Aller dans le dossier de ton projet
cd /d "C:\Users\Mahmoud At-Tidianie\Desktop\GITHUB\Structuration projet 1"

:: 2. Activer ton environnement virtuel Python
call venv\Scripts\activate

:: 3. Lancer ton pipeline principal
python main.py

:: 4. Fermer automatiquement après exécution
exit