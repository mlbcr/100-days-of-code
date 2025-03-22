class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def compare_question(self, guess):
        return self.answer == guess
