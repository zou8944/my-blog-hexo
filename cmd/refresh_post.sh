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

pwd
echo "移动文章到指定位置 ..."
## 将 cache/leagl_post.txt 中的文章移动到 source/_posts/ 目录下
while IFS= read -r file; do
  # 复制文件到目标目录
  cp -rf "$file" ../source/_posts/
done < "cache/legal_post.txt"

cd ..

echo "清除缓存 ..."
rm -rf ./cmd/cache

echo "完成！！！"