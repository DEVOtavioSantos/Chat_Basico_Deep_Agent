import os
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
from langgraph.prebuilt import create_react_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from Prompts.SystemPrompt import especialidade
from Prompts.BaseDeConhecimento.psicanalise import assunto
from rich.console import Console
from rich.markdown import Markdown
from Header import Banner
from api import api
Banner()
console = Console()
load_dotenv()
llm = ChatOpenRouter(
    model="openrouter/free",
    temperature=0.3,
    api_key=api 
)

Prompt = ChatPromptTemplate.from_messages([
    ("system", especialidade + "\n\n{assunto}"),
    ("user", "{input}")
])

chain = Prompt | llm | StrOutputParser()
while True:
    try:
        resposta = input("\n\nVocê: ")
        if resposta.lower() in ("sair", "exit", "quit"):
            break
        entrada = {"input": resposta}
        for chunk in chain.stream({
            "input":entrada,
            "assunto":assunto
        }):
            print(chunk, end="", flush=True)
    except KeyboardInterrupt:
        print("\nEncerrando...")
        break
    except Exception as e:
        print(f"\nErro: {e}")
