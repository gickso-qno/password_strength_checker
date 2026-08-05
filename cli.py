import click
from checker import PasswordChecker

@click.command()
@click.argument('password', required=False)
@click.option('--file', '-f', type=click.Path(exists=True), help='File with passwords to check')
def main(password, file):
    checker = PasswordChecker()
    
    if file:
        with open(file, 'r') as f:
            for line in f:
                pwd = line.strip()
                if pwd:
                    result = checker.check_password(pwd)
                    click.echo(f"Password: {pwd}")
                    click.echo(f"Strength: {result.strength.upper()} (Score: {result.score}/100)")
                    if result.feedback:
                        click.echo(f"Issues: {', '.join(result.feedback)}")
                    if result.recommendation:
                        click.echo(f"Recommendations: {', '.join(result.recommendation)}")
                    click.echo("-" * 40)
    elif password:
        result = checker.check_password(password)
        click.echo(f"Strength: {result.strength.upper()} (Score: {result.score}/100)")
        if result.feedback:
            click.echo(f"Issues: {', '.join(result.feedback)}")
        if result.recommendation:
            click.echo(f"Recommendations: {', '.join(result.recommendation)}")
    else:
        password = click.prompt('Enter password')
        result = checker.check_password(password)
        click.echo(f"Strength: {result.strength.upper()} (Score: {result.score}/100)")
        if result.feedback:
            click.echo(f"Issues: {', '.join(result.feedback)}")
        if result.recommendation:
            click.echo(f"Recommendations: {', '.join(result.recommendation)}")

if __name__ == '__main__':
    main()