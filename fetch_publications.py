from scholarly import scholarly
import datetime

# Replace with your actual Google Scholar ID
SCHOLAR_ID = "tQNSWaAAAAAJ&hl"  # Replace with your Google Scholar ID
OUTPUT_FILE = "research_stats.md"

def fetch_research_stats(scholar_id):
    """Fetches research stats (citations, h-index, i10-index) from Google Scholar."""
    try:
        print("Fetching author details...")
        author = scholarly.search_author_id(scholar_id)  # Fetch author by ID
        author = scholarly.fill(author)  # Fetch full details about the author
        print("Author details fetched. Fetching research stats...")

        # Extract research stats
        stats = {
            "citations": author.get("citedby", "N/A"),
            "h_index": author.get("hindex", "N/A"),
            "i10_index": author.get("i10index", "N/A"),
        }

        return stats
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def update_markdown(stats):
    """Updates the research stats markdown file."""
    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write("# 📊 Research Stats\n\n")
            f.write("Here are my research stats from Google Scholar:\n\n")
            f.write(f"- **Total Citations**: {stats['citations']}\n")
            f.write(f"- **h-index**: {stats['h_index']}\n")
            f.write(f"- **i10-index**: {stats['i10_index']}\n")
            f.write(f"\n\n_Last updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_")
    except Exception as e:
        print(f"An error occurred while updating the markdown file: {e}")

if __name__ == "__main__":
    stats = fetch_research_stats(SCHOLAR_ID)
    if stats:
        update_markdown(stats)
        print(f"Updated {OUTPUT_FILE} with research stats.")
    else:
        print("No stats found or an error occurred.")