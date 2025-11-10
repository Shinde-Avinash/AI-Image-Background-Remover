# 🧠 AI Image Background Remover

A **fast and modern web tool** for removing image backgrounds using the powerful **[rembg](https://github.com/danielgatis/rembg)** library — backed by a lightweight **Flask** server and a sleek **Tailwind CSS** interface.
<img width="1842" height="826" alt="image" src="https://github.com/user-attachments/assets/abc06532-f288-4303-9cb2-70589f842812" />
<img width="1756" height="831" alt="image" src="https://github.com/user-attachments/assets/16062f49-b7f1-4f09-b315-3abe87fdfb0e" />

---

## ✨ Features

- ⚡ **Instant Removal:** Uses the state-of-the-art `rembg` AI model for high-quality background segmentation.  
- 🖤 **Modern UI:** Clean, responsive, dark-themed interface built with **Tailwind CSS**.  
- 🪄 **Simple Workflow:** Upload → Process → Download — all in three easy steps.  
- 🖼️ **Supported Formats:** Accepts `.png`, `.jpg`, `.jpeg`, and `.webp` files.  

---
| Component     | Technology                  |
| ------------- | --------------------------- |
| **Backend**   | Flask (Python)              |
| **AI Engine** | rembg (ONNX model)          |
| **Frontend**  | Tailwind CSS + Jinja2       |
| **Storage**   | Local static/uploads folder |
| **Language**  | Python 3.8+                 |


## 🚀 Setup & Installation

Follow these steps to set up and run the application locally.

### 🧩 Prerequisites
You’ll need **Python 3.8 or higher** installed on your system.

---

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YourUsername/AI-Image-Background-Remover.git
cd AI-Image-Background-Remover

AI-Image-Background-Remover/
├── app.py                      # Flask application backend and routes
├── static/                     # Static files and processed images
│   └── uploads/                # Uploaded + processed output files
└── templates/
    └── home.html               # Frontend HTML (Tailwind CSS + Jinja2)
🌟 Author

Developed by: Avinash Shinde
Passionate about Python, AI integration, and building modern user-centric web tools.

⭐ If you find this project helpful, don’t forget to star the repo!
