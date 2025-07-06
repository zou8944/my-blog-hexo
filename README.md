# 我的 Hexo 博客

这个仓库的作用是配置博客样式，然后将 My Words 仓库下的文章生成静态页面发布到 Cloudflare Pages。

数据来源：仓库 [My Words](https://github.com/zou8944/my-words)

发布到： Cloudflare Pages

评论存储：使用 gitalk 插件将评论写入到 My Words 仓库的 issues 中

## 开发

```shell
# 拉取博客文章
make build
# 生成静态页面
make generate
# 启动本地服务
make server
# 发布到 Cloudflare Pages
make deploy
```
