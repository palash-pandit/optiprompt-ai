import json
from pathlib import Path


class PricingManager:

    def __init__(self):

        config_path = (
            Path(__file__)
            .parent.parent
            / "config"
            / "models.json"
        )

        with open(config_path, "r") as file:
            self.models = json.load(file)["models"]

    def get_all_models(self):

        return self.models

    def get_model(self, model_id: str):

        for model in self.models:

            if model["id"] == model_id:
                return model

        return None


    