import sys
from datetime import datetime
from pathlib import Path
from typing import Union

import nbformat
from nbconvert import MarkdownExporter


def convert_notebook_to_post(notebook_path: Union[str, Path]) -> None:
    """Convert a Jupyter notebook to a Hugo blog post."""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb: nbformat.NotebookNode = nbformat.read(f, as_version=4)

    # Convert to markdown
    markdown_exporter = MarkdownExporter()
    markdown, _ = markdown_exporter.from_notebook_node(nb)

    # Extract title from first heading or filename
    title: str = Path(notebook_path).stem
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            if cell.source.startswith("# "):
                title = cell.source.splitlines()[0][2:].strip()
                break

    # Create front matter
    front_matter = f"""---
title: "{title}"
date: {datetime.now().strftime('%Y-%m-%d')}
lastmod: {datetime.now().strftime('%Y-%m-%d')}
draft: false
featured: false
tags: ["notebook", "python"]
categories: ["Data Science"]
image:
  caption: ''
  focal_point: ''
  preview_only: false
---

"""

    # Create post directory
    slug = title.lower().replace(' ', '-')
    post_dir = Path("content/post") / slug
    post_dir.mkdir(parents=True, exist_ok=True)

    # Write index.md
    with open(post_dir / "index.md", 'w', encoding='utf-8') as f:
        f.write(front_matter + markdown)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python notebook_to_post.py <notebook_path>")
        sys.exit(1)

    convert_notebook_to_post(sys.argv[1])