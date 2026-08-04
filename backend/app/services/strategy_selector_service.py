class StrategySelectorService:

    def select_strategy(
        self,
        prompt_type: str,
        quality_score: int,
        user_mode: str,
    ):

        reasons = []

        # Rule 1
        if prompt_type in ["Coding", "Medical", "Legal"]:

            reasons.append(
                "Sensitive prompt type requires minimal modification."
            )

            return {
                "strategy": "Conservative",
                "reason": reasons,
            }

        # Rule 2
        if user_mode.lower() == "quality":

            reasons.append(
                "User selected Quality First mode."
            )

            return {
                "strategy": "Conservative",
                "reason": reasons,
            }

        # Rule 3
        if quality_score >= 80:

            reasons.append(
                "Prompt quality is already high."
            )

            return {
                "strategy": "Balanced",
                "reason": reasons,
            }

        # Rule 4
        if quality_score < 50:

            reasons.append(
                "Prompt quality is low."
            )

            reasons.append(
                "Aggressive optimization recommended."
            )

            return {
                "strategy": "Aggressive",
                "reason": reasons,
            }

        reasons.append(
            "Balanced optimization selected."
        )

        return {
            "strategy": "Balanced",
            "reason": reasons,
        }