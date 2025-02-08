import markdown

# Read the Markdown file
with open("publications.md", "r", encoding="utf-8") as md_file:
    md_content = md_file.read()

# Convert Markdown to HTML
html_content = markdown.markdown(md_content)

# Write the HTML content to a file
with open("publications.html", "w", encoding="utf-8") as html_file:
    html_file.write(f"<!DOCTYPE html><html><body>{html_content}</body></html>")