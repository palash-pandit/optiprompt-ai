import tiktoken

class TokenService:

    def __init__(self):
        self.encoding=tiktoken.encoding_for_model("gpt-4")

    def analyze(self,text:str):

        characters=len(text)
        words = len(text.split())
        sentences=len([s for s in text.replace("!",".").replace("?",".").split(".") if s.strip()])
        tokens=len(self.encoding.encode(text))


        return {
            "characters": characters,
            "words": words,
            "sentences": sentences,
            "tokens": tokens,
        }

    