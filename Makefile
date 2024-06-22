fetch_post:
	@sh ./cmd/refresh_post.sh

clean:
	echo "移除文章 ..."
	rm -rf ./source/_posts/*
	echo "清除缓存 ..."
	rm -rf ./scripts/cache