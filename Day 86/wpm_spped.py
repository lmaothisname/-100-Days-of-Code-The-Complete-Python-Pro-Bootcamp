import tkinter as tk
import random
import requests

FONT_UI = ("DejaVu Sans Mono",18,"bold")

class TypingSpeedTester:
  def __init__(self,root):
    self.root = root
    self.root.title("WPM Speed Test")
    self.root.geometry("2560x1600")
    
    # state variables
    self.time_limit = 60
    self.time_left = self.time_limit
    self.timer_running = False
    self.timer_job = None
    
    self.sample_text = ""
    self.typed_chars = 0
    self.correct_chars = 0
    
    self.setup_ui()
    self.load_new_sample()
    
  def setup_ui(self):
    # 1. Top Section: Header & Stats
    stats_frame = tk.Frame(self.root, bg="#f5f6fa") 
    stats_frame.pack(fill="x", pady=(0, 20))
    
    self.time_label = tk.Label(stats_frame, text="Time: 60s", font=FONT_UI, bg="#f5f6fa", fg="#2d3436")
    self.time_label.pack(side="left", padx=15)
    
    self.wpm_label = tk.Label(stats_frame, text="WPM: 0", font=FONT_UI, bg="#f5f6fa", fg="#0984e3")
    self.wpm_label.pack(side="left", padx=15)
    
    self.acc_label = tk.Label(stats_frame, text="Accuracy: 100%", font=FONT_UI, bg="#f5f6fa", fg="#00b894")
    self.acc_label.pack(side="left", padx=15)
    
    # 2. Middle Section: Target Text Display
    text_frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief="groove")
    text_frame.pack(fill="both", expand=True, pady=10)
    
    self.text_display = tk.Text(
      text_frame,
      wrap="word",
      font=("DejaVu Sans Mono", 16),
      padx=20,
      pady=20,
      bg="#ffffff",
      relief="flat"
    )
    
    self.text_display.pack(fill="both", expand=True)
    
    # Color tags for typed characters
    self.text_display.tag_config("correct", foreground="#00b894")
    self.text_display.tag_config("wrong", foreground="#d63031", underline=True)
    self.text_display.tag_config("active", background="#dfe6e9")
    
    # 3. Bottom Section: Input field and Controls
    control_frame = tk.Frame(self.root, bg="#f5f6fa")
    control_frame.pack(fill="x", pady=(15, 0))
    
    # User typing field
    self.entry = tk.Entry(control_frame, font=("DejaVu Sans Mono", 16), width=45)
    self.entry.pack(side="left", fill="x", expand=True , padx=(0,15), ipady=8)
    self.entry.bind("<KeyRelease>", self.check_input)
    
    # Reset / Restart button
    self.reset_btn = tk.Button(
      control_frame,
      text="Restart",
      font=("DejaVu Sans Mono", 14, "bold"), 
      bg="#0984e3",
      fg="white",
      padx=20,
      command=self.reset_test
    )
    self.reset_btn.pack(side="right")
  
  # Add Sample Texts & Loading Method
  def fetch_sample_text(self):
    try:
      url = "https://random-word-api.herokuapp.com/word?number=30"
      response = requests.get(url, timeout=3)
      if response.status_code == 200:
        words = response.json()
        return " ".join(words)
    except Exception:
      pass
    
    fallback_texts = [
      "The quick brown fox jumps over the lazy dog. Programming in Python is fun and versatile.",
      "Consistency is the key to mastering any new skill. Practice a little bit every single day.",
      "Technology connects the world, enabling communication across vast distances in milliseconds."
    ]
    return random.choice(fallback_texts)
  
  def load_new_sample(self):
    self.sample_text = self.fetch_sample_text()
  
    self.text_display.config(state="normal")
    self.text_display.delete("1.0", tk.END)
    self.text_display.insert("1.0", self.sample_text)
    self.text_display.config(state="disabled")
    
  # Handle Key Input & Character Highlighting
  def check_input(self, event=None):
    # Start timer on very first keystroke
    if not self.timer_running and self.time_left > 0:
      self.timer_running = True
      self.update_timer()
      
    typed = self.entry.get()
    self.text_display.config(state="normal")
    self.text_display.tag_remove("correct", "1.0", tk.END)
    self.text_display.tag_remove("wrong", "1.0", tk.END)
    
    correct_count = 0
    for i, char in enumerate(typed):
      if i >= len(self.sample_text):
        break
      
      pos = f"1.0 + {i} chars"
      next_pos = f"1.0 + {i+1} chars"
      
      if char == self.sample_text[i]:
        self.text_display.tag_add("correct", pos, next_pos)
        correct_count += 1
      else:
        self.text_display.tag_add("wrong", pos, next_pos)
    self.text_display.config(state="disabled")
    
    # Calculate live accuracy
    if len(typed) > 0:
      acc = int((correct_count / len(typed)) * 100)
      self.acc_label.config(text=f"Accuracy: {acc}%")
      
    # if completed full text
    if typed == self.sample_text:
      self.finish_test()
  
  # The Countdown & WPM Calculation 
  def update_timer(self):
    if self.time_left > 0:
      self.time_left -= 1
      self.time_label.config(text=f"Time: {self.time_left}s")
      
      # Live WPM: (characters typed / 5) / elapsed minutes
      time_eplased = self.time_limit - self.time_left
      if time_eplased > 0:
        words_typed = len(self.entry.get()) / 5
        minutes = time_eplased / 60
        live_wpm = int(words_typed / minutes)
        self.wpm_label.config(text=f"WPM: {live_wpm}")
      self.timer_job = self.root.after(1000, self.update_timer)
    else:
      self.finish_test()
      
  def finish_test(self):
    self.timer_running = False
    if self.timer_job:
      self.root.after_cancel(self.timer_job)
    self.entry.config(state="disabled")
    
  # Reset Logic & Application Runner
  def reset_test(self):
    if self.timer_job:
      self.root.after_cancel(self.timer_job)
    
    self.time_left = self.time_limit
    self.timer_running = False
    self.time_label.config(text=f"Time: {self.time_limit}s")
    self.wpm_label.config(text="WPM: 0")
    self.acc_label.config(text="Accuracy: 100%")
    
    self.entry.config(state="normal") 
    self.entry.delete(0,tk.END)
    self.load_new_sample()
    
if __name__ == "__main__":
  root = tk.Tk()
  app = TypingSpeedTester(root)
  root.mainloop()