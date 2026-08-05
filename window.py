import flet as ft
from checker import PasswordChecker

def main(page: ft.Page):
    page.title = "Password Strength Checker"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    checker = PasswordChecker()

    password_field = ft.TextField(label="Password", password=True, autofocus=True)
    
    strength_text = ft.Text(value="Enter your password", color="blue", size=20)
    score_text = ft.Text(value="", size=16)
    feedback_text = ft.Text(value="", color="red", size=14)
    recommendation_text = ft.Text(value="", color="green", size=14)
    
    def show_error(msg):
        snack_bar = ft.SnackBar(content=ft.Text(msg), bgcolor="red")
        page.snack_bar = snack_bar
        page.snack_bar.open = True
        page.update()
    
    def get_color_by_strength(strength: str) -> str:
        colors = {
            "weak": "red",
            "medium": "orange", 
            "strong": "lightgreen",
            "very strong": "green"
        }
        return colors.get(strength, "blue")
    
    def btn_click(e):
        password_value = password_field.value
        
        if not password_value:
            show_error("Password cannot be empty")
            return

        result = checker.check_password(password_value)
        
        strength_text.value = f"Strength: {result.strength.upper()}"
        strength_text.color = get_color_by_strength(result.strength)
        
        score_text.value = f"Score: {result.score}/100"
        
        if result.feedback:
            feedback_text.value = f"Issues: {', '.join(result.feedback)}"
        else:
            feedback_text.value = ""
        
        if result.recommendation:
            recommendation_text.value = f"Recommendations: {', '.join(result.recommendation)}"
        else:
            recommendation_text.value = "Great password!"
        
        password_field.value = ""
        password_field.focus()
        page.update()
    
    page.add(
        strength_text,
        score_text,
        password_field,
        ft.Row([ft.Button("Check", on_click=btn_click)], 
               alignment=ft.MainAxisAlignment.CENTER),
        feedback_text,
        recommendation_text
    )

ft.run(main, port=8550, view=ft.AppView.WEB_BROWSER)