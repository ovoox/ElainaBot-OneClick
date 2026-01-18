FROM python:3.11-slim

WORKDIR /app

# 安装基础系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    libmagic1 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 复制项目文件
COPY . .

# 赋予启动脚本执行权限
RUN chmod +x entrypoint.sh

# 暴露 Web 面板端口
EXPOSE 5001

# 使用自动化脚本启动
ENTRYPOINT ["./entrypoint.sh"]
