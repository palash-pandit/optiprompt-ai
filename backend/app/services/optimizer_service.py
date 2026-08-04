import re


class OptimizerService:

    FILLER_PHRASES = [
        "please",
        "kindly",
        "could you",
        "would you",
        "can you",
        "i want you to",
        "if possible",
        "i would like you to",
        "may you",
        "would you mind"
    ]

    def remove_fillers(self, text: str) -> str:
        """
        Remove unnecessary polite phrases.
        """

        for phrase in self.FILLER_PHRASES:
            pattern = re.compile(r"\b" + re.escape(phrase) + r"\b", re.IGNORECASE)
            text = pattern.sub("", text)

        return text

    def remove_duplicate_words(self, text: str) -> str:
        """
        Remove consecutive duplicate words.
        Example:
        'Explain explain ML'
        -> 'Explain ML'
        """

        words = text.split()

        cleaned = []

        for word in words:

            if not cleaned:
                cleaned.append(word)

            elif cleaned[-1].lower() != word.lower():
                cleaned.append(word)

        return " ".join(cleaned)

    def normalize_spaces(self, text: str) -> str:
        """
        Remove extra spaces.
        """

        return " ".join(text.split())

    def normalize_punctuation(self, text: str) -> str:
        """
        Replace repeated punctuation with a single one.
        """

        text = re.sub(r"[!?]+", ".", text)
        text = re.sub(r"\.{2,}", ".", text)

        return text.strip()

    def capitalize_first_letter(self, text: str) -> str:
        """
        Capitalize first letter.
        """

        if not text:
            return text

        return text[0].upper() + text[1:]

    def optimize(self, text: str, strategy: str):
        """
        Main optimization pipeline.
        """

        original = text

        optimized = text

        if strategy == "Balanced":

            optimized = self.remove_fillers(optimized)
            optimized = self.remove_duplicate_words(optimized)
            optimized = self.normalize_spaces(optimized)
            optimized = self.normalize_punctuation(optimized)
            optimized = self.capitalize_first_letter(optimized)

        elif strategy == "Aggressive":

            optimized = self.remove_fillers(optimized)
            optimized = self.remove_duplicate_words(optimized)
            optimized = self.normalize_spaces(optimized)
            optimized = self.normalize_punctuation(optimized)
            optimized = self.capitalize_first_letter(optimized)

        # Conservative strategy keeps prompt unchanged

        optimization_applied = original.strip() != optimized.strip()

        return {

            "optimized_prompt": optimized,

            "optimization_applied": optimization_applied
        }