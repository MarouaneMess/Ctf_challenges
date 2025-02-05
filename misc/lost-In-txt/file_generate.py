import random
import base64

# Générer 10 000 lignes de texte aléatoire
lines = ["HELLOOOOO-ThisIsARandomLine:" + str(i) for i in range(10000)]

# Cacher le flag encodé en base64
flag = "shellmates{L0st_1n_T3xt}"
encoded_flag = base64.b64encode(flag.encode()).decode().strip()  # Encoder en base64
position = random.randint(0, 9999)
lines[position] = encoded_flag

# Écrire dans un fichier
with open("lost_flag.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")