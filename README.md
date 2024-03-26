# Tmoh
Actualmente la descarga se hace en la misma carpeta donde se ubica el archivo ".py", por ello se exigen 3 alternativas: 
1. USANDO DOCKER - Copias las descargas del contenedor a tu PC (las descargas se encuentran en la carpeta /app del contenedor)
2. USANDO DOCKER - Haces referencia de la carpeta "/app" a una carpeta Local cuando ejecutes el contenedor para que las descargas se hagan directamente en tu PC (La carpeta Local debe tener el archivo .py para funcionar)
3. SIN DOCKER - Instalas python y las librerias que estan en 'requirements.txt' en tu computadora para ejecutarlo de manera Local.
