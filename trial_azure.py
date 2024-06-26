# %%
1
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
    path = Path(Path(__file__).parent, '.env')
    load_dotenv(path)
    print(f'load {path}')
except NameError:
    load_dotenv()
    print(f'load .env')

{'environemt variables': 
    [var_name for var_name, value in os.environ.items()
     if any(map(lambda kwd: kwd in var_name, ["OPENAI", "CHAT"])) and value]}
# - 'OPENAI_API_KEY'
# - 'AZURE_OPENAI_API_KEY'
# - 'AZURE_OPENAI_ENDPOINT'
# %%
llm = AzureChatOpenAI(
    #azure_deployment="my-gpt-4o",
    model_name="gpt-4o",
    openai_api_version="2024-05-13",
)


# %%
prompt = "プログラミングを始めるのにおすすめの言語はなんですか?"
input = [HumanMessage(content=prompt)]
result = llm.invoke(input=prompt)
print(result.content)


# %%
