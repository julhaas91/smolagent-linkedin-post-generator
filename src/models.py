import os
from smolagents import LiteLLMModel, OpenAIServerModel

def get_model(model: str) -> object:
    """
    Get the model based on the type specified.
    openai/gpt-4o-mini
    """

    type, model_id = model.split("/")

    if type == "ollama":
        return LiteLLMModel(
            model_id="gemma2",
            api_base="http://localhost:11434",
            num_ctx=8192,
        )
    elif type == "openai":
        return OpenAIServerModel(
            model_id="gpt-4o-mini",
            api_base="https://api.openai.com/v1",
            api_key=os.environ["OPENAI_API_KEY"],
        )
    else:
        raise ValueError(f"Model type '{type}' is not supported.")