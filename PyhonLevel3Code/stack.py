class TextEditor:
    def __init__(self):
        self.text = ""  # Current text in the editor
        self.history = []  # Stack to store the history of changes

    # Function to add text to the editor
    def add_text(self, new_text):
        self.history.append(self.text)  # Push the current state to the history stack
        self.text += new_text
        print(f"Text after adding: '{self.text}'")

    # Function to undo the last operation
    def undo(self):
        if self.history:
            self.text = self.history.pop()  # Pop the last saved state
            print(f"Text after undo: '{self.text}'")
        else:
            print("Nothing to undo.")

    # Function to peek at the last saved state without undoing
    def peek_last(self):
        if self.history:
            last_state = self.history[-1]  # Peek at the top of the stack
            print(f"Last saved state (peek): '{last_state}'")
        else:
            print("No history to peek at.")

# Testing the TextEditor class
editor = TextEditor()

# Adding text and checking the state
editor.add_text("Hello")
editor.add_text(" World")

# Peek at the last state before undo
editor.peek_last()

# Undo the last addition
editor.undo()

# Undo again
editor.undo()

# Try undoing when there is nothing left to undo
editor.undo()
