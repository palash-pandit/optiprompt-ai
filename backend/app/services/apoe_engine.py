from app.services.token_service import TokenService
from app.services.prompt_quality_service import PromptQualityService
from app.services.prompt_classifier_service import PromptClassifierService
from app.services.strategy_selector_service import StrategySelectorService
from app.services.optimizer_service import OptimizerService


class APOEEngine:

    def __init__(self):
        self.token_service = TokenService()
        self.quality_service = PromptQualityService()
        self.classifier_service = PromptClassifierService()
        self.strategy_service = StrategySelectorService()
        self.optimizer_service = OptimizerService()

    def optimize(self, text: str, user_mode: str):

        # Analyze original prompt
        token_before = self.token_service.analyze(text)

        quality = self.quality_service.analyze(text)

        classification = self.classifier_service.classify(text)

        strategy = self.strategy_service.select_strategy(
            classification["prompt_type"],
            quality["score"],
            user_mode
        )

        # Optimize prompt
        optimization = self.optimizer_service.optimize(
            text,
            strategy["strategy"]
        )

        # Analyze optimized prompt
        token_after = self.token_service.analyze(
            optimization["optimized_prompt"]
        )

        # Token statistics
        tokens_before = token_before["tokens"]
        tokens_after = token_after["tokens"]

        tokens_saved = max(0, tokens_before - tokens_after)

        reduction_percentage = 0

        if tokens_before > 0:
            reduction_percentage = round(
                (tokens_saved / tokens_before) * 100,
                2
            )

        # Temporary cost estimation
        COST_PER_1K_TOKENS = 0.01

        cost_before = round(
            (tokens_before / 1000) * COST_PER_1K_TOKENS,
            6
        )

        cost_after = round(
            (tokens_after / 1000) * COST_PER_1K_TOKENS,
            6
        )

        savings = round(
            cost_before - cost_after,
            6
        )

        return {
            "original_prompt": text,
            "optimized_prompt": optimization["optimized_prompt"],
            "optimization_applied": optimization["optimization_applied"],

            "quality_score": quality["score"],
            "prompt_type": classification["prompt_type"],
            "strategy": strategy["strategy"],
            "reasons": strategy["reason"],

            "tokens_before": tokens_before,
            "tokens_after": tokens_after,
            "tokens_saved": tokens_saved,
            "reduction_percentage": reduction_percentage,

            "estimated_cost_before": cost_before,
            "estimated_cost_after": cost_after,
            "estimated_savings": savings
        }