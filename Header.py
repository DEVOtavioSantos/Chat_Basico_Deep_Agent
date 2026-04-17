from pyfiglet import Figlet
from rich.console import Console

def Banner():
    console = Console()
    f = Figlet(font="pagga")
    ascci_Banner = f.renderText("Chat Deep Agente básico")

    console.rule(style="#C15F3C")
    console.print(ascci_Banner, style="#C15F3C")
    console.print("Identidade: Base da Psicanálise (Freud e Lancan)\n\n")
    console.rule("Chat ligado", style="#C15F3C")