import re
import sys
from datetime import datetime
import os

def format_citations_in_file(file_path):
    """
    Reads a markdown file, finds a single-line citation block, and reformats it
    into a multi-line markdown list.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}", file=sys.stderr)
        sys.exit(1)

    citation_header = "#### **引用文献**"
    header_index = content.find(citation_header)
    if header_index == -1:
        return

    # Try to extract date from YAML front matter
    date_str = None
    front_matter_match = re.search(r'---(.*?)---', content, re.DOTALL)
    if front_matter_match:
        front_matter = front_matter_match.group(1)
        date_match = re.search(r'date:\s*(\d{4}-\d{2}-\d{2})', front_matter)
        if date_match:
            date_str = date_match.group(1)

    if date_str:
        try:
            # Parse YYYY-MM-DD and format to M月 D, YYYY
            dt_object = datetime.strptime(date_str, '%Y-%m-%d')
            date_accessed = f"{dt_object.month}月 {dt_object.day}, {dt_object.year}にアクセス、"
        except ValueError:
            # Fallback if date parsing fails
            now = datetime.now()
            date_accessed = f"{now.month}月 {now.day}, {now.year}にアクセス、"
    else:
        # Fallback if date field is not found
        now = datetime.now()
        date_accessed = f"{now.month}月 {now.day}, {now.year}にアクセス、"

    search_area_start = header_index + len(citation_header)
    search_area = content[search_area_start:]

    first_line = search_area.lstrip().split('\n')[0].strip()

    if not first_line or first_line.startswith("1. "):
        return

    # Corrected Regex Pattern:
    # (\d+)     - Captures the number
    # \\.      - Matches the literal "."
    # \s       - Matches the space
    # (.*?)     - Non-greedily captures the title and URL
    # (?=...)   - Positive lookahead for the next citation or end of string
    pattern = re.compile(r'(\d+)\\. (.*?)(?=\s+\d+\\. |$)' ) # Corrected: escaped backslashes in regex pattern
    matches = pattern.findall(first_line)

    if not matches:
        return

    new_citation_lines = []
    for number, text in matches:
        try:
            title, url = text.rsplit(', ', 1)
            if not url.startswith('http'):
                continue
            new_line = f"{number}. {title.strip()}, {date_accessed} [{url.strip()}]({url.strip()})  "
            new_citation_lines.append(new_line)
        except ValueError:
            continue

    if not new_citation_lines:
        return

    new_citations_block = "\n\n" + "\n".join(new_citation_lines)
    
    original_block_to_replace = search_area.lstrip().split('\n')[0]
    new_content = content.replace(original_block_to_replace, new_citations_block.strip() + '\n')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Successfully formatted citations in {os.path.basename(file_path)}.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python format_citations.py <file_path1> [<file_path2> ...]", file=sys.stderr)
        sys.exit(1)

    for file_path in sys.argv[1:]:
        if '*' in file_path or '?' in file_path:
            import glob
            files = glob.glob(file_path, recursive=True)
            for f in files:
                format_citations_in_file(f)
        else:
            format_citations_in_file(file_path)

if __name__ == "__main__":
    main()