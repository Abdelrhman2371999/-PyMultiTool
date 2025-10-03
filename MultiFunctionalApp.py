from tkinter import *
from tkinter import ttk, messagebox, filedialog
from tkcalendar import DateEntry
import pyttsx3
import speech_recognition as sr
import qrcode
import time
from PIL import Image, ImageTk
import os


class MultiFunctionalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Functional Python App")
        self.root.geometry("800x700")
        self.root.config(bg="lightblue")
        
        # Initialize TTS engine
        self.engine = pyttsx3.init()
        
        self.create_notebook()
        self.welcome_user()
    
    def create_notebook(self):
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        
        # Create frames for each functionality
        self.form_frame = Frame(self.notebook, bg="lightblue")
        self.speech_frame = Frame(self.notebook, bg="lightblue")
        self.qr_frame = Frame(self.notebook, bg="lightblue")
        self.quiz_frame = Frame(self.notebook, bg="lightblue")
        
        # Add frames to notebook
        self.notebook.add(self.form_frame, text="Data Form")
        self.notebook.add(self.speech_frame, text="Speech App")
        self.notebook.add(self.qr_frame, text="QR Generator")
        self.notebook.add(self.quiz_frame, text="MCQ Quiz")
        
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Setup each tab
        self.setup_form_tab()
        self.setup_speech_tab()
        self.setup_qr_tab()
        self.setup_quiz_tab()
    
    def welcome_user(self):
        self.engine.say("Welcome to the Multi Functional Python Application!")
        self.engine.runAndWait()
    
    def setup_form_tab(self):
        # Title
        title_label = Label(self.form_frame, text="Student Registration Form", 
                          font=("Courier", 20, "bold"), bg="lightblue", 
                          bd=5, relief=RIDGE)
        title_label.grid(row=0, column=0, pady=10, columnspan=4, sticky="we")
        
        # First Name
        Label(self.form_frame, text="First Name:", bg="lightblue", 
              font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.first_name_entry = Entry(self.form_frame, width=25, font=("Arial", 12))
        self.first_name_entry.grid(row=1, column=1, pady=5)
        
        # Last Name
        Label(self.form_frame, text="Last Name:", bg="lightblue", 
              font=("Arial", 12)).grid(row=1, column=2, padx=10, pady=5, sticky="w")
        self.last_name_entry = Entry(self.form_frame, width=25, font=("Arial", 12))
        self.last_name_entry.grid(row=1, column=3, pady=5)
        
        # Birth Date
        Label(self.form_frame, text="Birth Date:", bg="lightblue", 
              font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.birth_date = DateEntry(self.form_frame, width=20, background="darkblue", 
                                   foreground="white", borderwidth=2, font=("Arial", 12))
        self.birth_date.grid(row=2, column=1, pady=5, sticky="w")
        
        # Gender
        Label(self.form_frame, text="Gender:", bg="lightblue", 
              font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.gender_var = StringVar(value="None")
        Radiobutton(self.form_frame, text="Male", variable=self.gender_var, 
                   value="Male", bg="lightblue", font=("Arial", 12)).grid(row=3, column=1, sticky="w")
        Radiobutton(self.form_frame, text="Female", variable=self.gender_var, 
                   value="Female", bg="lightblue", font=("Arial", 12)).grid(row=3, column=2, sticky="w")
        
        # Country
        Label(self.form_frame, text="Country:", bg="lightblue", 
              font=("Arial", 12)).grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.country_combo = ttk.Combobox(self.form_frame, values=[
            "Egypt", "Saudi Arabia", "United Arab Emirates", "Jordan", 
            "Lebanon", "Qatar", "Kuwait", "Oman", "Bahrain"
        ], font=("Arial", 12), width=23)
        self.country_combo.grid(row=4, column=1, pady=5, sticky="w")
        
        # Address
        Label(self.form_frame, text="Address:", bg="lightblue", 
              font=("Arial", 12)).grid(row=5, column=0, padx=10, pady=5, sticky="nw")
        self.address_text = Text(self.form_frame, height=4, width=50, font=("Arial", 12))
        self.address_text.grid(row=5, column=1, columnspan=3, pady=5, padx=10, sticky="we")
        
        # Buttons
        Button(self.form_frame, text="Save Data", command=self.save_form_data,
               bg="green", fg="white", font=("Arial", 12, "bold"), 
               width=12).grid(row=6, column=1, pady=20)
        Button(self.form_frame, text="Clear Form", command=self.clear_form,
               bg="red", fg="white", font=("Arial", 12, "bold"), 
               width=12).grid(row=6, column=2, pady=20)
    
    def save_form_data(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        birth_date = self.birth_date.get()
        gender = self.gender_var.get()
        country = self.country_combo.get()
        address = self.address_text.get("1.0", END).strip()
        
        if not all([first_name, last_name, country]):
            messagebox.showerror("Error", "Please fill all required fields!")
            return
        
        data = f"{first_name},{last_name},{birth_date},{gender},{country},{address}\n"
        
        try:
            with open("student_data.csv", "a", encoding="utf-8") as file:
                file.write(data)
            messagebox.showinfo("Success", "Data saved successfully!")
            self.engine.say(f"Data saved for {first_name} {last_name}")
            self.engine.runAndWait()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {str(e)}")
    
    def clear_form(self):
        self.first_name_entry.delete(0, END)
        self.last_name_entry.delete(0, END)
        self.gender_var.set("None")
        self.country_combo.set('')
        self.address_text.delete("1.0", END)
        self.first_name_entry.focus()
    
    def setup_speech_tab(self):
        # Title
        Label(self.speech_frame, text="Speech Recognition & Text-to-Speech", 
              font=("Courier", 16, "bold"), bg="lightblue").pack(pady=10)
        
        # Text-to-Speech Section
        tts_frame = LabelFrame(self.speech_frame, text="Text-to-Speech", 
                              bg="lightblue", font=("Arial", 12, "bold"))
        tts_frame.pack(fill="x", padx=20, pady=10)
        
        Label(tts_frame, text="Enter text to speak:", bg="lightblue", 
              font=("Arial", 11)).pack(anchor="w", padx=10, pady=5)
        self.tts_entry = Text(tts_frame, height=3, width=60, font=("Arial", 11))
        self.tts_entry.pack(padx=10, pady=5)
        
        Button(tts_frame, text="🔊 Speak Text", command=self.speak_text,
               bg="blue", fg="white", font=("Arial", 11, "bold")).pack(pady=10)
        
        # Speech-to-Text Section
        stt_frame = LabelFrame(self.speech_frame, text="Speech-to-Text", 
                              bg="lightblue", font=("Arial", 12, "bold"))
        stt_frame.pack(fill="x", padx=20, pady=10)
        
        Button(stt_frame, text="🎤 Start Listening", command=self.start_listening,
               bg="green", fg="white", font=("Arial", 12, "bold"), 
               height=2).pack(pady=10)
        
        self.stt_result = Text(stt_frame, height=4, width=60, font=("Arial", 11))
        self.stt_result.pack(padx=10, pady=5)
    
    def speak_text(self):
        text = self.tts_entry.get("1.0", END).strip()
        if text:
            self.engine.say(text)
            self.engine.runAndWait()
        else:
            messagebox.showwarning("Warning", "Please enter some text to speak!")
    
    def start_listening(self):
        self.stt_result.delete("1.0", END)
        self.stt_result.insert(END, "Listening... Please speak now.\n")
        self.root.update()
        
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout=10)
            
            text = r.recognize_google(audio)
            self.stt_result.delete("1.0", END)
            self.stt_result.insert(END, f"Recognized text: {text}")
            
        except sr.UnknownValueError:
            self.stt_result.delete("1.0", END)
            self.stt_result.insert(END, "Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            self.stt_result.delete("1.0", END)
            self.stt_result.insert(END, f"Error with speech recognition: {e}")
        except Exception as e:
            self.stt_result.delete("1.0", END)
            self.stt_result.insert(END, f"Error: {str(e)}")
    
    def setup_qr_tab(self):
        # Title
        Label(self.qr_frame, text="QR Code Generator", 
              font=("Courier", 16, "bold"), bg="lightblue").pack(pady=10)
        
        # Input Section
        input_frame = Frame(self.qr_frame, bg="lightblue")
        input_frame.pack(pady=10)
        
        Label(input_frame, text="Enter text/data for QR code:", 
              bg="lightblue", font=("Arial", 11)).grid(row=0, column=0, sticky="w")
        
        self.qr_data = Text(input_frame, height=4, width=50, font=("Arial", 11))
        self.qr_data.grid(row=1, column=0, padx=5, pady=5)
        
        Label(input_frame, text="File name (without extension):", 
              bg="lightblue", font=("Arial", 11)).grid(row=2, column=0, sticky="w")
        
        self.qr_filename = Entry(input_frame, width=30, font=("Arial", 11))
        self.qr_filename.grid(row=3, column=0, padx=5, pady=5)
        
        Button(input_frame, text="Generate QR Code", command=self.generate_qr,
               bg="purple", fg="white", font=("Arial", 11, "bold")).grid(row=4, column=0, pady=10)
        
        # QR Display Section
        self.qr_label = Label(self.qr_frame, text="QR Code will appear here", 
                             bg="white", relief="solid", bd=2, width=40, height=15)
        self.qr_label.pack(pady=10)
    
    def generate_qr(self):
        data = self.qr_data.get("1.0", END).strip()
        filename = self.qr_filename.get().strip()
        
        if not data:
            messagebox.showerror("Error", "Please enter data for QR code!")
            return
        
        if not filename:
            filename = "qrcode"
        
        try:
            qr = qrcode.make(data)
            qr.save(f"{filename}.png")
            
            # Display the QR code
            img = Image.open(f"{filename}.png")
            img = img.resize((200, 200), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            
            self.qr_label.config(image=photo, text="")
            self.qr_label.image = photo
            
            messagebox.showinfo("Success", f"QR code saved as {filename}.png")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate QR code: {str(e)}")
    
    def setup_quiz_tab(self):
        # Title
        Label(self.quiz_frame, text="Python GUI Programming Quiz", 
              font=("Courier", 16, "bold"), bg="lightblue").pack(pady=10)
        
        # Quiz Questions
        self.questions = [
            {
                "question": "What is the main purpose of using 'columnspan' in Tkinter's grid layout?",
                "options": [
                    "To set the background color of multiple columns",
                    "To make a widget span across multiple columns",
                    "To create space between columns",
                    "To align widgets vertically"
                ],
                "answer": 1
            },
            {
                "question": "Which library is used for generating QR codes?",
                "options": ["qrcode", "QRGenerator", "pyqrcode", "qrgen"],
                "answer": 0
            },
            {
                "question": "What does 'sticky=we' do in grid layout?",
                "options": [
                    "Makes the widget sticky like glue",
                    "Aligns widget to both west and east (left and right)",
                    "Makes the widget invisible",
                    "Sets widget color to white"
                ],
                "answer": 1
            }
        ]
        
        self.current_question = 0
        self.score = 0
        self.user_answers = []
        
        # Question Display
        self.question_label = Label(self.quiz_frame, text="", wraplength=600,
                                   bg="lightblue", font=("Arial", 12, "bold"), justify="left")
        self.question_label.pack(pady=10)
        
        # Options Frame
        self.option_frame = Frame(self.quiz_frame, bg="lightblue")
        self.option_frame.pack(pady=10)
        
        self.option_vars = []
        self.option_buttons = []
        
        for i in range(4):
            var = IntVar(value=-1)
            self.option_vars.append(var)
            btn = Radiobutton(self.option_frame, text="", variable=var, 
                             value=i, bg="lightblue", font=("Arial", 11),
                             command=lambda i=i: self.select_answer(i))
            btn.grid(row=i, column=0, sticky="w", pady=5)
            self.option_buttons.append(btn)
        
        # Navigation Buttons
        nav_frame = Frame(self.quiz_frame, bg="lightblue")
        nav_frame.pack(pady=20)
        
        Button(nav_frame, text="Previous", command=self.previous_question,
               bg="orange", fg="white", font=("Arial", 11)).grid(row=0, column=0, padx=10)
        
        Button(nav_frame, text="Next", command=self.next_question,
               bg="green", fg="white", font=("Arial", 11)).grid(row=0, column=1, padx=10)
        
        Button(nav_frame, text="Submit Quiz", command=self.submit_quiz,
               bg="red", fg="white", font=("Arial", 11, "bold")).grid(row=0, column=2, padx=10)
        
        # Score Display
        self.score_label = Label(self.quiz_frame, text="Score: 0/0", 
                                bg="lightblue", font=("Arial", 12, "bold"))
        self.score_label.pack(pady=10)
        
        self.display_question()
    
    def display_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=f"Q{self.current_question + 1}: {question_data['question']}")
            
            for i, option in enumerate(question_data['options']):
                self.option_buttons[i].config(text=option)
            
            # Show current answer if exists
            if self.current_question < len(self.user_answers):
                selected = self.user_answers[self.current_question]
                self.option_vars[selected].set(selected)
            else:
                for var in self.option_vars:
                    var.set(-1)
            
            self.score_label.config(text=f"Score: {self.score}/{len(self.questions)}")
    
    def select_answer(self, option_index):
        if self.current_question >= len(self.user_answers):
            self.user_answers.append(option_index)
        else:
            self.user_answers[self.current_question] = option_index
        
        # Check if answer is correct
        correct_answer = self.questions[self.current_question]['answer']
        if option_index == correct_answer:
            if self.current_question >= len(self.user_answers) - 1:
                self.score += 1
    
    def previous_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.display_question()
    
    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.display_question()
    
    def submit_quiz(self):
        # Calculate final score
        self.score = 0
        for i, answer in enumerate(self.user_answers):
            if answer == self.questions[i]['answer']:
                self.score += 1
        
        messagebox.showinfo("Quiz Completed", 
                           f"Your final score: {self.score}/{len(self.questions)}\n"
                           f"Percentage: {(self.score/len(self.questions))*100:.1f}%")
        
        # Speak the result
        self.engine.say(f"Quiz completed! Your score is {self.score} out of {len(self.questions)}")
        self.engine.runAndWait()

# Main application
if __name__ == "__main__":
    root = Tk()
    app = MultiFunctionalApp(root)
    root.mainloop()
