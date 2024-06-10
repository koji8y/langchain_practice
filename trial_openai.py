# %%
# from langchain.llms import OpenAI
# from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import os
from pathlib import Path
from dotenv import load_dotenv


# %%
try:
    load_dotenv(Path(Path(__file__).parent, '.env'))
except NameError:
    load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model_name="gpt-4o", openai_api_key=openai_api_key)


# %%
prompt = "プログラミングを始めるのにおすすめの言語はなんですか?"
input = [HumanMessage(content=prompt)]
result = llm.invoke(input=prompt)
print(result.content)


# %%
