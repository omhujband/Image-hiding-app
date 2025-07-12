# Import necessary libraries
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image
import numpy as np

# Function to encode message into image
def encode_image(image_path, message, bit_position):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = np.array(img)
    message += '\0'  # Null character to indicate end of message
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    index = 0
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(3):  # Iterate over RGB channels
                if index < len(binary_message):
                    pixel_bin = list(format(pixels[i, j, k], '08b'))
                    pixel_bin[-bit_position] = binary_message[index]  # Modify the bit
                    pixels[i, j, k] = int(''.join(pixel_bin), 2)
                    index += 1
                else:
                    break

    encoded_img = Image.fromarray(pixels.astype(np.uint8))
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        encoded_img.save(save_path, optimize=True)  # Use optimize to reduce size increase
        messagebox.showinfo("Success", "Image saved successfully!")

# Function to decode message from image
def decode_image(image_path, bit_position):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = np.array(img)

    binary_message = ""
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(3):  # Iterate over RGB channels
                pixel_bin = format(pixels[i, j, k], '08b')
                binary_message += pixel_bin[-bit_position]  # Extract the bit

    message = ""
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        if char == '\0':  # Stop at null character
            break
        message += char

    # Create a new window to display message with copy option
    result_window = tk.Toplevel()
    result_window.title("Decoded Message")
    result_window.geometry("400x200")

    text_box = tk.Text(result_window, wrap='word', font=("Arial", 10))
    text_box.pack(expand=True, fill='both', padx=10, pady=10)
    text_box.insert('1.0', message)
    text_box.config(state='normal')  # Enable copy

# GUI Setup
def main():
    root = tk.Tk()
    root.title("Steganography App")
    root.geometry("400x300")  # Set a larger window size

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True)

    tk.Label(frame, text="Select Bit Position for Encoding/Decoding:", font=("Arial", 12)).pack(pady=(0, 10))
    bit_var = tk.IntVar(value=1)
    tk.Radiobutton(frame, text="1st Bit", variable=bit_var, value=1, font=("Arial", 10)).pack(anchor='w')
    tk.Radiobutton(frame, text="2nd Bit", variable=bit_var, value=2, font=("Arial", 10)).pack(anchor='w')
    tk.Radiobutton(frame, text="3rd Bit", variable=bit_var, value=3, font=("Arial", 10)).pack(anchor='w')

    def open_encode():
        image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if image_path:
            message = simpledialog.askstring("Input", "Enter message to encode:")
            if message:
                encode_image(image_path, message, bit_var.get())

    def open_decode():
        image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if image_path:
            decode_image(image_path, bit_var.get())

    tk.Button(frame, text="Encode Image", command=open_encode, width=20, font=("Arial", 10)).pack(pady=10)
    tk.Button(frame, text="Decode Image", command=open_decode, width=20, font=("Arial", 10)).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
