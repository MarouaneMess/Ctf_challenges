from PIL import Image

def encode_image(image_path, message, output_path):
    try:
        img = Image.open(image_path)
        binary_message = ''.join(format(ord(i), '08b') for i in message)
        binary_message += '00000000'  # Ajouter un terminateur pour indiquer la fin du message
        data_index = 0

        # Créer une copie modifiable de l'image
        img = img.convert("RGB")
        pixels = img.load()
        for y in range(img.height):
            for x in range(img.width):
                if data_index < len(binary_message):
                    # Obtenir la valeur du pixel
                    r, g, b = pixels[x, y]
                    # Modifier le bit le moins significatif du canal bleu
                    new_b = (b & ~1) | int(binary_message[data_index])
                    data_index += 1

                    # Mettre à jour le pixel avec le nouveau canal bleu
                    pixels[x, y] = (r, g, new_b)
                else:
                    break
            if data_index >= len(binary_message):
                break

        # Sauvegarder l'image encodée
        img.save(output_path)
        print(f"Message encodé et sauvegardé dans {output_path}")
    except Exception as e:
        print(f"Erreur lors de l'encodage de l'image : {e}")

# Utilisation
flag = "shellmates{h1dd3n_1n_th3_p1x3ls}"
encode_image("image.png", flag, "shellmates.png")

# the flag was in shellmates.png