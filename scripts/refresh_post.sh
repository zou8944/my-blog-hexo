#!/usr/bin/env bash

echo "移除原有文章"
# 移除 demo 开头之外的所有文章
find ./source/_posts -type f ! -name "demo-*" -exec rm {} \;

cd ./scripts

rm -rf cache
mkdir cache && cd cache
wget https://github.com/zou8944/my-words/archive/refs/heads/main.zip

if [[ $(uname) == "Darwin" ]]; then
  unar -e utf-8 main.zip
else
  unzip -O utf-8 main.zip
fi

cp -r cache/my-words-main/posts/* ../source/_posts/
