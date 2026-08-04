class PromptClassifierService:

    def classify(self, text: str):

        text = text.lower()

        categories = {
            "Coding": [
                "python",
                "java",
                "code",
                "program",
                "function",
                "algorithm",
                "bug"
            ],

            "Translation": [
                "translate",
                "translation",
                "convert to"
            ],

            "Summarization": [
                "summarize",
                "summary",
                "shorten"
            ],

            "Creative Writing": [
                "story",
                "poem",
                "novel",
                "creative"
            ],

            "Data Analysis": [
                "dataset",
                "analysis",
                "csv",
                "statistics",
                "graph"
            ],

            "Educational": [
                "explain",
                "what is",
                "how does",
                "difference between",
                "teach"
            ]
        }

        for category, keywords in categories.items():

            for keyword in keywords:

                if keyword in text:
                    return {
                        "prompt_type": category,
                        "confidence": 0.95
                    }

        return {
            "prompt_type": "General Question",
            "confidence": 0.60
        }