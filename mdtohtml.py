import markdown
import argparse
import os

def markdown_to_html(input_file, output_file):
    # Read the Markdown file
    with open(input_file, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    html_content = markdown.markdown(md_content)

    # Define the HTML template below:
    html_template = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>This is just an example some HTML boilerplate</h1>
    <main class="container">
        {{ content }}
    </main>
</body>
</html>
    """

    # Insert the converted HTML content into the template
    full_html_content = html_template.replace('{{ content }}', html_content)

    # Create the HTML file and write the content to it
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(full_html_content)

    print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Convert a Markdown file to HTML.")
    parser.add_argument('input_file', help="The input Markdown file.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Derive the output file path
    input_file_path = args.input_file
    base_name = os.path.splitext(input_file_path)[0]
    output_file_path = f"{base_name}.html"

    # Convert the Markdown to HTML
    markdown_to_html(input_file_path, output_file_path)