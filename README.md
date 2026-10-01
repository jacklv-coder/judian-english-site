# 奇想语法官网

独立静态站点：主页、隐私政策、使用帮助、使用条款。无统计、广告脚本和表单。

本仓库只存放公开网站，不含 App 源码、题库、签名或用户学习数据。

本地校验：`python3 check_site.py`。GitHub Pages 使用 `main` 分支根目录和 `.nojekyll`；正式地址为 `https://jacklv-coder.github.io/judian-english-site/`。

Git fetch / push 使用 SSH。CI 的 `REPO_SSH_KEY` 为本仓库专用只读 deploy key，不能写入仓库。网站变更通过功能分支与 PR，检查通过后合并；已有产品的网站不受影响。

支持联系信息沿用开发者已发布产品的公开资料。App 未正式可下载前，主页显示“即将上线”；确认实际商店公开链接生效后再替换为下载入口。
