#!/usr/bin/env bash

echo "移除文章 ..."
rm -rf ./source/_posts/*

echo "清除缓存 ..."
rm -rf ./cmd/cache

cd ./cmd

echo "下载文章 ..."
mkdir cache && cd cache
wget https://github.com/zou8944/my-words/archive/refs/heads/main.zip

echo "解压文章 ..."
if [[ $(uname) == "Darwin" ]]; then
  unar -e utf-8 main.zip
else
  unzip -O utf-8 main.zip
fi

cd ..

echo "调整文章数据 ..."
python check_and_fix_post.py cache/my-words-main/posts | grep ".md$" > cache/legal_post.txt

echo "移动文章到指定位置 ..."
# 将 cache/leagl_post.txt 中的文章移动到 source/_posts/ 目录下
mkdir -p ../source/_posts/
while IFS= read -r file; do
  # 复制文件到目标目录
  cp -rf "$file" ../source/_posts/
done < "cache/legal_post.txt"

echo "生成 thoughts 页面 ..."
python generate_thoughts.py cache/my-words-main/thoughts > cache/thoughts_index.md

echo "移动 thoughts 页面到指定位置 ..."
mkdir -p ../source/thoughts/
cp cache/thoughts_index.md ../source/thoughts/index.md

cd ..

echo "清除缓存 ..."
rm -rf ./cmd/cache

echo "完成！！！"
