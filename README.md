# 🐍 Multi-Functional Python App (Tkinter)

This project is a **GUI application built with Tkinter** that integrates multiple functionalities:
1. **Student Registration Form**
2. **Speech Recognition & Text-to-Speech**
3. **QR Code Generator**
4. **MCQ Quiz**

---

## 📦 Requirements

Install dependencies using `pip`:

```bash
pip install pyttsx3==2.90
pip install SpeechRecognition==3.10.0
pip install pydub==0.25.1
pip install "qrcode[pil]==7.4.2"
pip install Pillow==10.0.0
pip install tkcalendar==1.6.1
```

⚠️ Note: `pydub` requires [FFmpeg](https://ffmpeg.org/download.html) installed and added to PATH.

---

## 🚀 Features

### 1. Student Registration Form
- Collects **First Name, Last Name, Birth Date, Gender, Country, Address**.
- Saves form data to a `student_data.csv` file.
- Includes **Save Data** and **Clear Form** buttons.
- Uses **Text-to-Speech (TTS)** to confirm saved data.

---

### 2. Speech Recognition & Text-to-Speech
- **Text-to-Speech (TTS):** Convert typed text into speech using `pyttsx3`.
- **Speech-to-Text (STT):** Listen via microphone and convert spoken words into text using `speech_recognition`.

---

### 3. QR Code Generator
- Generate QR codes from user input text.
- Save QR codes as `.png` files.
- Display the generated QR code in the GUI.

---

### 4. MCQ Quiz
- A simple multiple-choice quiz on **Tkinter & Python basics**.
- Features:
  - Previous / Next navigation
  - Final Score calculation
  - **Text-to-Speech** announcement of results

---

## 🖼️ GUI Layout
The app uses **Tkinter’s Notebook (Tabs)** for multiple sections:
- **Tab 1:** Data Form
- **Tab 2:** Speech App
- **Tab 3:** QR Generator
- **Tab 4:** Quiz

---

## ▶️ Running the Application

Run the script:

```bash
python app.py
```

The GUI window will open with **four functional tabs**.

---

## 📂 Project Structure

```
multi_functional_app/
│── app.py                # Main Python application
│── student_data.csv       # Auto-generated file for form data
│── qrcode.png             # Example QR code output
│── README.md              # Documentation (this file)
```

---

## 🛠️ Technologies Used
- **Python 3.x**
- **Tkinter** (GUI framework)
- **tkcalendar** (Date Picker)
- **pyttsx3** (Text-to-Speech)
- **speech_recognition** (Speech-to-Text)
- **pydub + ffmpeg** (Audio handling)
- **qrcode** (QR code generation)
- **Pillow (PIL)** (Image handling)

---

## 👨‍💻 Author
Developed by **Abdelrhman Hamed** as a **Multi-Functional Educational App** combining Python GUI and external libraries.

