from PIL import Image

def decode_image(image_path):    
    img = Image.open(image_path)    
    binary_message = ""    
    for pixel in img.getdata():        # Extract the LSB of the blue channel
        binary_message += str(pixel[2] & 1)    # Split the binary message into 8-bit chunks and convert to characters
    message = ""    
    for i in range(0, len(binary_message), 8):        
        byte = binary_message[i:i+8]        
        if len(byte) == 8:
            char = chr(int(byte, 2))            
            message += char
            # Stop if we reach the end of the message
            if message.endswith('}'):                
                break

    return message

# Usage
extracted_flag = decode_image("shellmates.png") 
print("Extracted Flag:", extracted_flag)

# OR U CAN JUST USE ZSTEG TOOL or online tools 
