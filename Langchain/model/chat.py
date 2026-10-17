from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

llm= ChatOpenAI(model="gpt-5-nano",temperature=0)

prompt="tell me a joke on programming"

response= llm.invoke(prompt)

print(response.content)