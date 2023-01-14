import requests


def update_quote():
    # Get a new quote
    quote_data = requests.get("https://api.quotable.io/random").json()
    quote = quote_data["content"]
    author = quote_data["author"]
    print(f"quote: {quote}")
    print(f"author: {author}")

    # Open the README.md file
    with open("README.md", "r") as f:
        readme_lines = f.readlines()

    # Find the line number of the quote and author
    quote_line = 13
    author_line = 15

    # Replace the quote and author lines
    readme_lines[quote_line-1] = f"#### _{quote}_\n"
    readme_lines[author_line-1] = f"###### _by {author}_\n"

    # Write the new quote and author to the README.md file
    with open("README.md", "w") as f:
        f.writelines(readme_lines)


update_quote()
