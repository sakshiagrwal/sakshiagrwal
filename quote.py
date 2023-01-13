import requests
import re

def update_quote():
    # Get a new quote
    quote = requests.get('https://api.quotable.io/random').json()['content']
    print(f'quote: {quote}')

    # Open the README.md file
    with open("README.md", "r") as f:
        readme = f.read()

    # Replace the old quote with the new quote
    new_readme = re.sub(r"(#### Random Quote:).*", f"\g<1> {quote}", readme)

    # Write the new quote to the README.md file
    with open("README.md", "w") as f:
        f.write(new_readme)

update_quote()
