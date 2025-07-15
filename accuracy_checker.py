import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim
import os

def calculate_mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1] * imageA.shape[2])
    return err

def calculate_psnr(mse):
    if mse == 0:
        return float('inf')
    PIXEL_MAX = 255.0
    return 20 * np.log10(PIXEL_MAX / np.sqrt(mse))

def calculate_ssim(imageA, imageB):
    imageA_gray = np.mean(imageA, axis=2).astype(np.uint8)
    imageB_gray = np.mean(imageB, axis=2).astype(np.uint8)
    return ssim(imageA_gray, imageB_gray)

def process_images():
    raw_path = filedialog.askopenfilename(title="Select Original Image")
    if not raw_path:
        return

    enc_path = filedialog.askopenfilename(title="Select Encoded Image")
    if not enc_path:
        return

    raw_img = np.array(Image.open(raw_path).convert("RGB"))
    enc_img = np.array(Image.open(enc_path).convert("RGB"))

    if raw_img.shape != enc_img.shape:
        messagebox.showerror("Error", "Images must be of the same dimensions!")
        return

    mse_val = calculate_mse(raw_img, enc_img)
    psnr_val = calculate_psnr(mse_val)
    ssim_val = calculate_ssim(raw_img, enc_img)

    show_graph(mse_val, psnr_val, ssim_val)

def show_graph(mse, psnr, ssim_val):
    metrics = ["MSE", "PSNR", "SSIM"]
    values = [mse, psnr, ssim_val]

    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(metrics, values, color=["red", "green", "blue"])

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, f'{yval:.2f}', ha='center', va='bottom')

    plt.title("Image Comparison Metrics")
    plt.ylabel("Value")
    plt.ylim(0, max(values) * 1.2)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    legend_text = (
        "MSE: Lower is better. 0 means perfect match.\n"
        "PSNR: Higher is better. >40 dB is excellent.\n"
        "SSIM: Closer to 1 means structurally identical."
    )
    fig.text(1.05, 0.5, legend_text, fontsize=10, va='center')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image Accuracy Checker")
    root.geometry("400x200")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True)

    label = tk.Label(frame, text="Compare Raw and Encoded Image", font=("Arial", 12))
    label.pack(pady=10)

    btn = tk.Button(frame, text="Select Images & Compare", font=("Arial", 10), command=process_images)
    btn.pack(pady=10)

    root.mainloop()
