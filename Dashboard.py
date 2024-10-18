import flet as ft
import time
import threading


def show_main_page(page, show_login_panel):
    animated_text = ft.Text(
        "Welcome to the Main Page!",
        size=30,
        color=ft.colors.WHITE,
        weight=ft.FontWeight.BOLD,
        style=ft.TextStyle(font_family="Helvetica Neue"),
        animate_opacity=1000  # Add opacity animation with duration of 1000ms
    )

    def glow_effect():
        while True:
            # Increase opacity to create glow effect
            animated_text.opacity = 1.0
            page.update()
            time.sleep(1)  # Glow for 1 second

            # Reduce opacity to remove glow effect
            animated_text.opacity = 0.5
            page.update()
            time.sleep(1)  # Wait for 1 second

    # Start glow effect in a separate thread
    threading.Thread(target=glow_effect, daemon=True).start()

    sidebar = ft.Container(
        content=ft.Column(
            [
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.icons.HOME, color=ft.colors.WHITE),
                        ft.Text("Главная")
                    ], alignment=ft.MainAxisAlignment.START),
                    on_click=lambda e: print("Navigating to Главная..."),
                    style=ft.ButtonStyle(
                        color={"": ft.colors.WHITE, "hovered": "#ECD06F"},
                        bgcolor={"hovered": "transparent"},
                        text_style={"hovered": ft.TextStyle(size=24)}
                    ),
                ),
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.icons.MOVIE, color=ft.colors.WHITE),
                        ft.Text("Фильмы")
                    ], alignment=ft.MainAxisAlignment.START),
                    on_click=lambda e: print("Navigating to Фильмы..."),
                    style=ft.ButtonStyle(
                        color={"": ft.colors.WHITE, "hovered": "#ECD06F"},
                        bgcolor={"hovered": "transparent"},
                        text_style={"hovered": ft.TextStyle(size=24)}
                    ),
                ),
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.icons.TV, color=ft.colors.WHITE),
                        ft.Text("Сериалы")
                    ], alignment=ft.MainAxisAlignment.START),
                    on_click=lambda e: print("Navigating to Сериалы..."),
                    style=ft.ButtonStyle(
                        color={"": ft.colors.WHITE, "hovered": "#ECD06F"},
                        bgcolor={"hovered": "transparent"},
                        text_style={"hovered": ft.TextStyle(size=24)}
                    ),
                ),
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.icons.ANIMATION, color=ft.colors.WHITE),
                        ft.Text("Аниме")
                    ], alignment=ft.MainAxisAlignment.START),
                    on_click=lambda e: print("Navigating to Аниме..."),
                    style=ft.ButtonStyle(
                        color={"": ft.colors.WHITE, "hovered": "#ECD06F"},
                        bgcolor={"hovered": "transparent"},
                        text_style={"hovered": ft.TextStyle(size=24)}
                    ),
                ),
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.icons.PERSON, color=ft.colors.WHITE),
                        ft.Text("Профиль")
                    ], alignment=ft.MainAxisAlignment.START),
                    on_click=lambda e: print("Navigating to Профиль..."),
                    style=ft.ButtonStyle(
                        color={"": ft.colors.WHITE, "hovered": "#ECD06F"},
                        bgcolor={"hovered": "transparent"},
                        text_style={"hovered": ft.TextStyle(size=24)}
                    ),
                ),
                ft.TextButton(
                    content=ft.Row([
                        ft.Icon(ft.icons.EXIT_TO_APP, color=ft.colors.WHITE),
                        ft.Text("Выход")
                    ], alignment=ft.MainAxisAlignment.START),
                    on_click=lambda e: show_login_panel(page),
                    style=ft.ButtonStyle(
                        color={"": ft.colors.WHITE, "hovered": "#ECD06F"},
                        bgcolor={"hovered": "transparent"},
                        text_style={"hovered": ft.TextStyle(size=24)}
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=20,
        ),
        width=200,
        bgcolor="#4E4E50",  # Set the background color for the sidebar tile
        padding=20,
        border_radius=10
    )

    main_content = ft.Container(
        content=ft.Column(
            [
                animated_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        expand=True,
        padding=20,
        bgcolor="#1A1A1D",  # Set the background color for the main content tile
        border_radius=10
    )

    fade_container = ft.Container(
        content=ft.Row(
            [
                sidebar,
                main_content
            ],
            spacing=20,  # Add spacing between tiles
        ),
        padding=20,
        opacity=0,
        animate_opacity=1000  # Increase duration to make transition more noticeable
    )

    page.add(fade_container)
    page.update()

    # Trigger fade in with a delay
    fade_container.opacity = 1
    page.update()
