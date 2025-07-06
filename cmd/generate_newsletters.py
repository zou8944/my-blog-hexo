"""
生成 newsletter
- 为所有文件添加 front-matter
- 将 homepage.md 换成 index.md
"""

import os
import re
import sys


def handle_newsletter_file(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        title = os.path.basename(file_path).replace(".md", "")
        front_matter = f"""---
title: {title}
date: 2025-07-06 17:54:50
---
"""
        content = front_matter + content
        print(f"已为 {file_path} 添加 front-matter")

    # 匹配 Markdown 链接中的 .md 后缀，例如：[text](./path/file.md) -> [text](./path/file)
    content = re.sub(r"\]\(([^)]*?)\.md\)", r"](\1)", content)
    print(f"已处理 {file_path}")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


def handle_newsletter_dir(dir: str):
    for root, _, files in os.walk(dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                handle_newsletter_file(file_path)

    homepage_path = os.path.join(dir, "homepage.md")
    index_path = os.path.join(dir, "index.md")
    if os.path.exists(homepage_path):
        os.rename(homepage_path, index_path)
        print(f"已将 {homepage_path} 重命名为 {index_path}")


def main():
    # newsletters_dir = "/Users/zouguodong/Code/Personal/my-blog-hexo/source/newsletters"
    newsletter_dir = sys.argv[1]
    handle_newsletter_dir(newsletter_dir)


if __name__ == "__main__":
    main()
