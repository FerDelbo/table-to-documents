from langchain_core.language_models.llms import LLM
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class agent_LLM(LLM):
    api_url: str = os.getenv("API_URL")
    api_key: str = os.getenv("API_KEY")
    model_name: str = os.getenv("MODEL_NAME", "gemini-2.5")
    provider: str = os.getenv("PROVIDER", "gemini")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.api_url = self.api_url.format(MODEL_NAME=self.model_name, API_KEY=self.api_key)

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(self, prompt: str, stop: list[str] | None = None) -> str:
        
        if self.provider == "gemini":
            headers = {"Content-Type": "application/json"}
            payload = {
                "contents": [{
                    "parts": [{"text": prompt}]
                }]
            }
            response = requests.post(self.api_url, json=payload, headers=headers)
            if response.status_code == 200:
                data = response.json()
                return data["candidates"][0]["content"]["parts"][0]["text"]
            else:
                raise ValueError(f"Gemini API request failed: {response.status_code} - {response.text}")
        else:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": self.model_name,
                "messages": [{"role": "user", "content": prompt}]
            }
            response = requests.post(self.api_url, json=payload, headers=headers)
            if response.status_code == 200:
                data = response.json()
                return data["choices"][0]["message"]["content"]
            else:
                raise ValueError(f"{self.model_name} API request failed: {response.status_code} - {response.text}")
        # else:
        #     raise ValueError(f"Unsupported provider: {self.provider}")
    def define_person(self, table, prompt):
        """Define a person based on the provided table and prompt."""
        prompt = prompt.format(table=table)
        person = self._call(f"Answer the following prompt:\n{prompt}")
        return person 