build:
	@sh ./cmd/refresh_post.sh

generate:
	@echo "生成静态页面 ..."
	hexo generate
	@echo "生成完成！"

clean:
	echo "移除文章 ..."
	rm -rf ./source/_posts/*
	echo "移除 thoughts 页面 ..."
	rm -rf ./source/thoughts/*
	echo "移除 newsletters 页面 ..."
	rm -rf ./source/newsletters/*
	echo "清除缓存 ..."
	rm -rf ./cmd/cache