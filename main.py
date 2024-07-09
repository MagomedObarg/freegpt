import flet as ft
import g4f
import asyncio

async def get_response(prompt):
    response = await g4f.ChatCompletion.create_async(
        model=g4f.models.default,
        messages=[{"role": "user", "content": prompt}],
        provider=g4f.Provider.You,
    )
    return response

def main(page: ft.Page):
    text_input = ft.TextField(label="Введите текст", width=300)

    text_output = ft.Text(value="", size=24)

    # Создаем кнопку
    def button_clicked(e):
        prompt = text_input.value
        response = asyncio.run(get_response(prompt))

        text_output.value = response
        page.update()

    button = ft.ElevatedButton("Отправить", on_click=button_clicked)

    page.add(
        ft.Column(
            controls=[
                text_input,
                button,
                text_output,
            ]
        )
    )

ft.app(main)