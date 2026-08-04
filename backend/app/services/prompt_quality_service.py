class PromptQualityService:

    def analyze(self, text: str):

        words = text.split()

        score = 0
        metrics = {}
        suggestions = []

        # -------- Clarity --------
        action_words = [
            "explain",
            "write",
            "summarize",
            "translate",
            "compare",
            "analyze",
            "generate",
            "create"
        ]

        clarity = 100 if any(word.lower() in action_words for word in words) else 40
        metrics["clarity"] = clarity
        score += clarity * 0.30

        # -------- Context --------
        word_count = len(words)

        if word_count >= 10:
            context = 100
        elif word_count >= 5:
            context = 70
        else:
            context = 30
            suggestions.append("Add more context.")

        metrics["context"] = context
        score += context * 0.20

        # -------- Constraints --------
        constraint_keywords = [
            "under",
            "within",
            "only",
            "maximum",
            "minimum",
            "exactly"
        ]

        has_constraint = any(k in text.lower() for k in constraint_keywords)

        constraints = 100 if has_constraint else 30

        if not has_constraint:
            suggestions.append("Specify constraints such as length or limits.")

        metrics["constraints"] = constraints
        score += constraints * 0.20

        # -------- Output Format --------
        formats = [
            "table",
            "json",
            "bullet",
            "markdown",
            "list",
            "code"
        ]

        has_format = any(f in text.lower() for f in formats)

        output_format = 100 if has_format else 30

        if not has_format:
            suggestions.append("Specify the desired output format.")

        metrics["output_format"] = output_format
        score += output_format * 0.15

        # -------- Conciseness --------
        conciseness = 100 if word_count <= 60 else 60

        if word_count > 100:
            suggestions.append("Prompt may be unnecessarily long.")

        metrics["conciseness"] = conciseness
        score += conciseness * 0.15

        score = round(score)

        if score >= 85:
            grade = "Excellent"
        elif score >= 70:
            grade = "Good"
        elif score >= 50:
            grade = "Average"
        else:
            grade = "Needs Improvement"

        return {
            "score": score,
            "grade": grade,
            "metrics": metrics,
            "suggestions": suggestions
        }