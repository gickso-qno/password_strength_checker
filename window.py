import flet as ft

def main(page: ft.Page):

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    password = ft.TextField(label="Password", autofocus=True)

    text = ft.Text(value="Enter your password", color="blue")

    def btn_click(e):
        if password != "":
            page.add(ft.Checkbox(label=password.value))
            password.value = ""
            password.focus()
            password.update()

    page.add(text, ft.Row([password, ft.ElevatedButton("Check", on_click=btn_click)], alignment= ft.MainAxisAlignment.CENTER))

ft.app(port=8550, target=main, view=ft.AppView.WEB_BROWSER)