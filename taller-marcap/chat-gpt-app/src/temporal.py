import openai  # pip install openai
import config # local
import typer  # pip install "typer[all]"
from rich import print  # pip install rich
from rich.table import Table

def main():

    openai.api_key = config.api_key

    print(" [bold green]ChatGPT API en Python[/bold green]")

    # opciones para el usuario
    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")

    print(table)

    # Dando Contexto del asistente
    context = {"role": "system",
               "content": "Eres un asistente que sabe todo sobre k-pop"}
    messages = [context]

    while True:

        content = __prompt()

	# reiniciando, nueva conversacion
        if content == "new":
            print(" Nueva conversación creada")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

        # una respuesta
        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold red]> [/bold red] [red]{response_content}[/red]")


####################funciones####################

def __prompt() -> str:
    prompt = typer.prompt("\n¿Sobre qué quieres hablar? ")

    if prompt == "exit":
        exit = typer.confirm(" ¿Estás seguro?")
        if exit:
            print(" ¡Hasta luego!")
            raise typer.Abort()

        return __prompt()

    return prompt


if __name__ == "__main__":
    typer.run(main)

