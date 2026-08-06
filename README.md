# Password Strength Checker

A comprehensive password strength checker that evaluates password complexity and provides actionable recommendations for improvement. Supports both CLI and web interfaces.

## Features

- **Multi-factor strength analysis**: Evaluates passwords based on length, character variety, and common password detection
- **Detailed feedback**: Provides specific issues and recommendations for each password
- **Dual interface**: Works as both CLI tool and web application
- **Common password detection**: Checks against a database of 100+ weak passwords
- **Color-coded results**: Visual indication of password strength (weak/medium/strong/very strong)

## Installation

### Requirements
- Python 3.8+
- Flet (for web interface)

### Setup
```bash
# Install dependencies
pip install flet click

# Or use the provided requirements file
pip install -r requirements.txt
```

## Usage

### CLI Interface

#### Interactive mode
```bash
python cli.py
```

#### Direct password check
```bash
python cli.py "YourPassword123!"
```

#### Check passwords from file
```bash
python cli.py -f passwords.txt
```

#### Example output
```
Strength: STRONG (Score: 75/100)
Issues: None
Recommendations: None
```

### Web Interface

```bash
python window.py
```

The web interface will open in your default browser at `http://localhost:8550`

#### Features
- Real-time password checking
- Visual strength indicator with progress bar
- Color-coded results (red/orange/green)
- Detailed feedback and recommendations
- Clean, responsive UI

## Password Scoring System

Passwords are evaluated on a 0-100 scale based on:

| Criteria | Points |
|----------|--------|
| Length < 8 | 0 |
| Length 8-11 | 10 |
| Length 12-15 | 15 |
| Length 16+ | 25 |
| Uppercase letters | 15 |
| Lowercase letters | 15 |
| Digits | 15 |
| Special characters | 20 |

### Strength Categories
- **Weak**: 0-40 points (or common password)
- **Medium**: 41-60 points
- **Strong**: 61-80 points
- **Very Strong**: 81-100 points

## Project Structure

```
password_strength_checker/
├── checker.py           # Core password checking logic
├── cli.py              # Command-line interface
├── window.py           # Web interface (Flet)
├── common_password.txt # Database of weak passwords
├── README.md           # This file
└── .gitignore          # Git ignore rules
```

## Module Usage

You can also use the checker as a module in your own projects:

```python
from checker import PasswordChecker

checker = PasswordChecker()
result = checker.check_password("MyPassword123!")

print(f"Strength: {result.strength}")
print(f"Score: {result.score}")
print(f"Issues: {result.feedback}")
print(f"Recommendations: {result.recommendation}")
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available for educational purposes.