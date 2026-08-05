from dataclasses import dataclass
from typing import List
import os

@dataclass
class PasswordResult:
    strength: str
    score: int
    feedback: list[str]
    recommendation: list[str]

class PasswordChecker:
    def __init__(self):
        self.common_passwords = self._load_common_passwords()

    def _load_common_passwords(self) -> set:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "common_password.txt")
        with open(file_path, "r") as file:
            return set(line.strip().lower() for line in file)

    def check_password(self, password: str) -> PasswordResult:
        strength = "weak"
        score = 0
        feedback = []
        recommendation = []
        
        # Check if password is in common passwords list
        if password.lower() in self.common_passwords:
            return PasswordResult(
                strength="weak",
                score=0,
                feedback=["Password is too common"],
                recommendation=["Use a more unique password"]
            )
        
        # Length check
        if len(password) < 8:
            feedback.append("Password is too short")
            recommendation.append("Use a longer password (minimum 8 characters)")
        elif len(password) < 12:
            score += 10
        elif len(password) < 16:
            score += 15
        else:
            score += 25

        # Uppercase check
        if any(char.isupper() for char in password):
            score += 15
        else:
            feedback.append("Password must have at least one uppercase letter")
            recommendation.append("Add an uppercase letter")

        # Lowercase check
        if any(char.islower() for char in password):
            score += 15
        else:
            feedback.append("Password must have at least one lowercase letter")
            recommendation.append("Add a lowercase letter")

        # Digit check
        if any(char.isdigit() for char in password):
            score += 15
        else:
            feedback.append("Password must have at least one number")
            recommendation.append("Add a number")

        # Special character check
        if any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?' for char in password):
            score += 20
        else:
            feedback.append("Password must have at least one special character")
            recommendation.append("Add a special character")

        # Determine strength category
        if score <= 40:
            strength = "weak"
        elif score <= 60:
            strength = "medium"
        elif score <= 80:
            strength = "strong"
        else:
            strength = "very strong"

        return PasswordResult(
            strength=strength,
            score=score,
            feedback=feedback,
            recommendation=recommendation
        )