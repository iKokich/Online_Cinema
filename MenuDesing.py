import flet as ft

def main(page: ft.Page):
    page.title = "Login Screen"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = ft.colors.DEEP_PURPLE  # Изменяем цвет заднего фона

    page.add(
        ft.Column(
            [
                ft.Container(
                    content=ft.Image(
                        src="robot.png",  # Укажи путь к изображению на твоем компьютере
                        width=100,
                        height=100
                    ),
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=ft.Text(
                        "Hi!",
                        size=24,
                        color=ft.colors.WHITE
                    ),
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=ft.TextField(
                        label="Username",
                        width=300,
                    ),
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=ft.TextField(
                        label="Password",
                        password=True,
                        width=300,
                    ),
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Checkbox(label="Remember me"),
                            ft.TextButton(text="Forgot Password?", on_click=lambda e: print("Forgot Password clicked")),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=ft.ElevatedButton(
                        text="LOGIN",
                        bgcolor=ft.colors.PINK,
                        color=ft.colors.WHITE,
                        on_click=lambda e: print("Login clicked")
                    ),
                    alignment=ft.alignment.center
                )
            ],
            alignment=ft.alignment.center
        )
    )

ft.app(target=main)



