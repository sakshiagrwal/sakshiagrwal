import requests
import re


def update_quote():
    # Get a new quote
    quote_data = requests.get("https://api.quotable.io/random").json()
    quote = quote_data["content"]
    author = quote_data["author"]
    print(f"quote: {quote}")
    print(f"author: {author}")

    # Open the README.md file
    with open("README.md", "r") as f:
        readme = f.read()

    # Replace the old quote with the new quote
    new_readme = re.sub(r"(#### _Quote:).*", f"\g<1> {quote}_", readme)

    # Replace the old author with the new author
    new_readme = re.sub(r"(######).*", f"\g<1> _by {author}_", new_readme)

    # Write the new quote to the README.md file
    with open("README.md", "w") as f:
        f.write(new_readme)


update_quote()
