import os
import re
import sys


def generate_new_content(post_path):
    with open(post_path) as f:
        filename = post_path.split("/")[-1].split(".md")[0]
        lines = [line.strip("\n") for line in f.readlines()]

        # 拆分成 front-matter 和正文
        front_matter_started = False
        front_matter_ended = False
        front_matter_lines = []
        content_lines = []
        for line in lines:
            # 遇到第一个 --- 时开始读取 front-matter，遇到第二个 --- 时开始读取正文，后面的 --- 不管
            if line.strip() == "---":
                if front_matter_ended:
                    content_lines.append(line)
                elif front_matter_started:
                    front_matter_started = False
                    front_matter_ended = True
                else:
                    front_matter_started = True
                continue
            if front_matter_started and not front_matter_ended:
                front_matter_lines.append(line)
                continue
            if front_matter_ended:
                content_lines.append(line)
                continue

        # 读取 title
        title = ""
        date = ""
        created_at = ""
        for line in front_matter_lines:
            if line.strip().startswith("title:"):
                title = line.split("title:")[1].strip()
            elif line.strip().startswith("date:"):
                date = line.split("date:")[1].strip()
            elif line.strip().startswith("created_at:"):
                created_at = line.split("created_at:")[1].strip()
        if not title:
            front_matter_lines.append(f"title: {filename}")
        if not date:
            front_matter_lines.append(f"date: {created_at}")
        front_matter_lines.insert(0, "---")
        front_matter_lines.append("---")

        if len(content_lines) == 0:
            print(f"Warning: 文章 {post_path} 内容不合法。可能没有 front-matter")
            return None
        # 修复正文
        # 去掉 content_lines 开始的空行
        while content_lines[0].strip() == "":
            content_lines.pop(0)
        has_more = False
        for line in content_lines:
            if re.match(r"<!--\s*more\s*-->", line.strip()):
                has_more = True
                break
        if not has_more:
            insert_pos = None
            non_empty_count = 0
            insert_pos = None
            for idx, line in enumerate(content_lines):
                if line.strip() == "":
                    continue
                non_empty_count += 1
                if line.strip().startswith("```") and non_empty_count <= 5:
                    insert_pos = idx
                    break
                if non_empty_count == 5:
                    insert_pos = idx
                    break
            if insert_pos is not None:
                content_lines.insert(insert_pos, "<!-- more -->")

    final_lines = front_matter_lines + [""] + content_lines
    return "\n".join(final_lines)


def fix_post(post_path):
    new_content = generate_new_content(post_path)
    if new_content is None:
        return
    print(post_path)
    with open(post_path, "w") as f:
        f.write(new_content)


def fix_all_post(post_dir):
    for root, dirs, files in os.walk(post_dir):
        for file in files:
            if file.endswith(".md"):
                fix_post(os.path.join(root, file))


if __name__ == "__main__":
    # file_path = sys.argv[1]
    # fix_post("cache/my-words-main/posts/2018/Git 介绍.md")
    fix_all_post(sys.argv[1])
