import html
class Questions:
    """Creates an object that has question and answer as parameters"""
    def __init__(self,question,answer):
        self.question=html.unescape(question)
        self.answer=answer

        