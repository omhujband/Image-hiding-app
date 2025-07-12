# 🖼️ Image Hiding App

A simple steganography-based desktop application that allows you to **hide (encode)** and **retrieve (decode)** secret messages inside image files using the **Least Significant Bit (LSB)** method. Built with `Tkinter` for GUI and `Pillow`/`NumPy` for image processing.

---

## 📑 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

---

## ✨ Features

- Encode secret messages into `.png`, `.jpg`, or `.jpeg` images.
- Decode and reveal hidden messages.
- Bit position selection for steganography depth (1st, 2nd, or 3rd LSB).
- User-friendly GUI built with `Tkinter`.
- Supports saving the encoded image file.

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/omhujband/Image-hiding-app.git
   cd Image-hiding-app
   ```

2. **Install dependencies (Python 3 required):**
   ```bash
   pip install tinker numpy
   ```

---

## 🚀 Usage

1. Run the app:
   ```bash
   python image_hiding_app.py
   ```

2. In the GUI:
   - Choose the bit position (1st, 2nd, or 3rd).
   - Click **"Encode Image"** to select an image and input your secret message.
   - Click **"Decode Image"** to extract a hidden message from an image.

---

## 🧠 How It Works

- The app encodes text messages into the image's pixel data by modifying the **Least Significant Bit (LSB)** of RGB channels.
- Each character is converted to 8-bit binary and embedded across the image.
- A null character (`\0`) marks the end of the hidden message.
- Bit selection allows balancing between **message robustness** and **image distortion visibility**.

---

## 📦 Dependencies

- [`NumPy`](https://numpy.org) – pixel array manipulation
- [`Tkinter`](https://wiki.python.org/moin/TkInter) – GUI (built-in with Python)

Install all via:

```bash
pip install pillow numpy
```

---

## 🔧 Configuration

- **Bit Position (1–3):** Selects which bit in the RGB byte to modify.
  - 1st bit (least visible change)
  - 2nd/3rd bits (more storage, more visible)

---

## 🧪 Examples

### ✅ Encoding:
- Select an image.
- Choose bit depth (e.g., 1st bit).
- Enter secret message.
- Save encoded image.

### 🔍 Decoding:
- Select the encoded image.
- Choose the same bit depth used for encoding.
- View the hidden message in a popup window.

---

## 🛠️ Troubleshooting

- **Image not saving?**
  - Ensure the save dialog is completed with a `.png` extension.
- **Message not decoded properly?**
  - Make sure you're using the same bit position that was used for encoding.

---

## 🔮 Future Enhancements

- **Image Compression Optimization**  
  - Implement smarter encoding that minimizes the increase in file size by applying advanced compression techniques after embedding messages.
  - Or add an inbuilt compressor to minimise the size of output image.

- **Message Accuracy Checking**  
  Adding different accuracy detection mechanism (e.g., using PSNR, SSIM, MSE, and BER) to ensure that the output image matches the original image. 

---

## 🤝 Acknowledgements
Developed with ❤️ in Python 

Inspired by basic steganography principles & academic research.