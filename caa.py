import tkinter as tk
import random
import time

# List of words for the typing test
words = ['Rural','Sixith','Sesquipedalian','Phenomenon','Onomatopoeia','Supercalifragilisticexpialidocious','Worcestershire','Suburban','Foramens','Obstinance']

class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")

        self.word_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Helvetica", 18))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_word)

        self.start_button = tk.Button(root, text="Start", command=self.start_typing_test)
        self.start_button.pack(pady=10)

        self.timer_label = tk.Label(root, text="", font=("Helvetica", 18))
        self.timer_label.pack(pady=10)

        self.test_in_progress = False
        self.words_typed = 0
        self.correct_words = 0
        self.start_time = 0
        self.duration = 60  # Set the duration of the typing test (in seconds)

    def get_random_word(self):
        return random.choice(words)

    def start_typing_test(self):
        self.test_in_progress = True
        self.words_typed = 0
        self.correct_words = 0
        self.start_time = time.time()
        self.update_word()

    def update_word(self):
        if self.test_in_progress:
            word = self.get_random_word()
            self.word_label.config(text=word)
            self.entry.delete(0, 'end')
            self.words_typed += 1
            if self.words_typed == 1:
                self.start_timer()
    
    def check_word(self, event):
        if self.test_in_progress:
            entered_word = self.entry.get().strip()
            target_word = self.word_label.cget("text")
            if entered_word == target_word:
                self.correct_words += 1
            self.update_word()
    
    def start_timer(self):
        def update_timer():
            if self.test_in_progress:
                elapsed_time = time.time() - self.start_time
                remaining_time = max(self.duration - elapsed_time, 0)
                self.timer_label.config(text=f"Time remaining: {int(remaining_time)} seconds")
                if remaining_time == 0:
                    self.end_typing_test()
                else:
                    self.root.after(1000, update_timer)

        update_timer()
    
    def end_typing_test(self):
        self.test_in_progress = False
        self.word_label.config(text="Typing test completed!")
        self.entry.delete(0, 'end')
        wpm = (self.correct_words / (self.duration / 60)) if self.duration > 0 else 0
        self.timer_label.config(text=f"Your Words Per Minute (WPM): {wpm:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()
