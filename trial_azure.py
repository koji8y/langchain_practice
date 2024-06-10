# %%
# from langchain.llms import OpenAI
# from langchain_community.chat_models import ChatOpenAI
from langchain_openai import AzureChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import os
from pathlib import Path
from dotenv import load_dotenv


# %%
try:
    load_dotenv(Path(Path(__file__).parent, '.env'))
except NameError:
    load_dotenv()

{'environemt variables': [var_name for var_name, value in os.environ.items() if "OPENAI" in var_name and value]}
# - 'OPENAI_API_KEY'
# - 'AZURE_OPENAI_API_KEY'
# - 'AZURE_OPENAI_ENDPOINT'
# %%
llm = AzureChatOpenAI(
    azure_deployment="my-gpt-4o",
)


# %%
prompt = "プログラミングを始めるのにおすすめの言語はなんですか?"
input = [HumanMessage(content=prompt)]
result = llm.invoke(input=prompt)
print(result.content)


# %%
