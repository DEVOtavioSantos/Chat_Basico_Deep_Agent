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

Banner();
console = Console()
load_dotenv()
llm = ChatOpenRouter(
    model="openrouter/free",
    temperature=0.3
    )

Prompt = ChatPromptTemplate.from_messages([
    ("system", especialidade),
    ("user", "{input}")
])

chain = Prompt | llm | StrOutputParser()
while True:
    resposta = input("\n\nVocê:")

    entrada = {
        "input": resposta,
        "assunto": assunto
    }


    for chunk in chain.stream(entrada):
        print(chunk, end="", flush=True)

