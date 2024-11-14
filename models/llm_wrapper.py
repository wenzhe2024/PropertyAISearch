import openai
from config.config import Config

class OpenAIWrapper:
    def __init__(self, model="GPT-4o", max_tokens=300, temperature=0.7):
        """
        初始化 OpenAI API Wrapper。

        参数:
        - model (str): 使用的模型名称，默认使用 "text-davinci-003"。
        - max_tokens (int): 返回的最大 token 数。
        - temperature (float): 控制生成文本的随机性，0.0 更确定，1.0 更随机。
        """
        openai.api_key = Config.OPENAI_API_KEY
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

    def query(self, prompt):
        """
        使用给定的 prompt 调用 OpenAI API，并返回响应。

        参数:
        - prompt (str): 用户提供的输入或查询。

        返回:
        - str: 模型生成的响应文本。
        """
        try:
            response = openai.Completion.create(
                engine=self.model,
                prompt=prompt,
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            # 返回模型的响应文本
            return response.choices[0].text.strip()
        except openai.error.OpenAIError as e:
            print("OpenAI API 请求出错:", e)
            return None
