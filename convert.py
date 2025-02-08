import markdown

try:
    # Read the Markdown file
    with open("research_stats.md", "r", encoding="utf-8") as md_file:
        md_content = md_file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)

    # Write the HTML content to a file
    with open("research_stats.html", "w", encoding="utf-8") as html_file:
        html_file.write(f"<!DOCTYPE html><html><body>{html_content}</body></html>")

    print("Successfully converted research_stats.md to research_stats.html!")
except FileNotFoundError:
    print("Error: research_stats.md file not found.")
except Exception as e:
    print(f"An error occurred: {e}")