import flet as ft
from connectionToDb import DatabaseConnection
from Dashboard import show_main_page


def login_panel(page, show_main_page):
    page.title = "Login Screen"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#1A1A1D"  # Set the background color for the entire application

    error_text = ft.Text("", color="#C3073F")  # Using one of the given colors for error text

    def on_login(e):
        print("Login button clicked")
        username_value = username.value
        password_value = password.value

        db = DatabaseConnection()
        db.connect()

        query = "SELECT * FROM users WHERE user_login = %s AND user_password = %s"
        result = db.fetchall(query, (username_value, password_value))

        if result:
            # Fade out effect before cleaning and showing the main page
            fade_container.opacity = 0
            page.update()
            page.clean()
            show_main_page(page, show_login_panel)
        else:
            error_text.value = "Неправильно ввели логин или пароль"
            page.update()

        db.close()

    username = ft.TextField(label="Username", width=300, bgcolor="#4E4E50", color=ft.colors.WHITE)
    password = ft.TextField(label="Password", password=True, can_reveal_password=True, width=300, bgcolor="#4E4E50",
                            color=ft.colors.WHITE)
    remember_me = ft.Checkbox(label="Remember me", fill_color=ft.colors.WHITE)  # White checkbox
    forgot_password = ft.TextButton("Forgot Password?", on_click=lambda e: print("Forgot Password clicked"),
                                    style=ft.ButtonStyle(color={"": "#6F2232"}))
    login_button = ft.ElevatedButton(
        "LOGIN",
        on_click=on_login,
        bgcolor="#C3073F",  # Initial red color
        color=ft.colors.WHITE,
        style=ft.ButtonStyle(
            bgcolor={
                "": "#C3073F",  # Initial red color
                "hovered": "#0000FF"  # Blue when hovered
            }
        )
    )

    login_panel = ft.Column(
        [
            ft.Row(
                [
                    ft.Image(
                        src="path/to/animated_emoji.gif",  # Path to your GIF file
                        width=40,
                        height=40
                    ),
                    ft.Container(
                        content=ft.Text(
                            "Hello!",
                            size=40,
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            italic=True,
                            style=ft.TextStyle(font_family="Helvetica Neue")
                        ),
                        alignment=ft.alignment.center,
                        padding=20,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            username,
            password,
            ft.Row([remember_me, forgot_password], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            login_button,
            error_text
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )

    fade_container = ft.Container(
        content=login_panel,
        width=400,
        height=400,
        bgcolor="#1A1A1D",  # Set the background to the black color provided
        border_radius=10,
        alignment=ft.alignment.center,
        opacity=1,
        animate_opacity=1000  # Increase duration to make transition more noticeable
    )

    page.add(fade_container)
    page.update()


def show_login_panel(page):
    page.clean()
    login_panel(page, show_main_page)
