# ElainaBot 终极一键部署版

本仓库支持**一条命令**完成环境安装、依赖配置及程序启动。

## 🚀 终极一键启动

在终端执行以下命令即可（支持 Ubuntu/Debian）：

```bash
curl -sSL https://raw.githubusercontent.com/ovoox/ElainaBot-OneClick/master/install.sh | bash
```

## 🛠 脚本功能
1. **自动安装环境**：自动安装 Python3, Pip, MySQL, Git 等系统依赖。
2. **自动配置虚拟环境**：创建隔离的 Python 运行环境，防止污染系统。
3. **自动安装依赖**：一键安装 `requirements.txt` 中的所有库。
4. **交互式配置**：脚本运行中会提示您输入机器人 APPID 等关键信息。
5. **直接启动**：配置完成后自动运行主程序。

## 🐳 Docker 方式 (备选)
如果您更喜欢 Docker，请确保已安装 Docker 和 Docker Compose：
```bash
docker-compose up -d
```

## 🔗 原始项目
基于 [lengxi-root/ElainaBot](https://github.com/lengxi-root/ElainaBot) 优化。
