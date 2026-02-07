# 🎧 PDF to Audiobook Converter

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Windows-lightgrey?style=for-the-badge)

A smart Python tool that converts PDF study notes and books into offline audiobooks (`.wav`). Built to help students study while traveling without needing an internet connection.

---

## 🌟 Key Features
- **📖 Smart PDF Parsing:** Extracts text automatically from standard PDF documents using `PyPDF2`.
- **🗣️ 100% Offline Mode:** Uses `pyttsx3` to convert text to speech without any API keys or internet.
- **🍏 macOS Optimized:** Solves common audio driver freezing issues on Mac by exporting to `.wav` format.
- **⏯️ Interactive Menu:** User-friendly CLI menu to Listen, Save, or both.

---

## 🛠️ Tech Stack
| Component | Technology |
|---|---|
| **Language** | Python 3 |
| **PDF Processing** | `PyPDF2` |
| **Audio Engine** | `pyttsx3` (Offline) |
| **System** | `OS` module (File handling) |

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/isham461/PDF-to-Audiobook-Converter.git](https://github.com/isham461/PDF-to-Audiobook-Converter.git)
cd PDF-to-Audiobook-Converter
'''
2. Install Dependencies
   Install the necessary Python libraries using pip:
   ```bash
   pip install PyPDF2 pyttsx3

3.Run the Application Run the main Python script to start the converter:
python3 audiobook.py
