# Utiliser une image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY . .

# Installer les dépendances (si nécessaire)
# RUN pip install --no-cache-dir -r requirements.txt

# Rendre le script exécutable
RUN chmod +x challenge.py

# Commande par défaut pour exécuter le script
CMD ["python3", "challenge.py"]