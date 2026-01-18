#!/bin/bash

# 颜色定义
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

PROJECT_DIR="ElainaBot-OneClick"

echo -e "${GREEN}>>> 开始安装 ElainaBot...${NC}"

# 1. 克隆仓库 (如果当前不在项目目录中)
if [ ! -f "main.py" ]; then
    if [ -d "$PROJECT_DIR" ]; then
        echo -e "检测到已存在目录，正在进入..."
        cd "$PROJECT_DIR"
    else
        echo -e "正在克隆项目代码..."
        git clone -q https://github.com/ovoox/ElainaBot-OneClick.git
        if [ $? -ne 0 ]; then
            echo -e "${RED}错误：克隆仓库失败，请检查网络。${NC}"
            exit 1
        fi
        cd "$PROJECT_DIR"
    fi
fi

# 2. 安装系统依赖
if [ -f /etc/debian_version ]; then
    echo -e "正在安装系统依赖..."
    sudo apt-get update -qq && sudo apt-get install -y python3 python3-pip python3-venv mysql-server libmagic1 curl git -qq
fi

# 3. 安装 Python 依赖
echo -e "正在准备 Python 环境并安装依赖..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt -q

# 4. 交互式输入
echo -e "\n${GREEN}请填写以下信息：${NC}"
read -p "请输入机器人 APPID: " appid
read -p "请输入机器人 SECRET: " secret
read -p "请输入机器人 QQ号: " qq
read -p "请输入 Web 面板 Token (默认 admin): " token
token=${token:-admin}

# 写入配置
echo "ROBOT_APPID=$appid" > .env
echo "ROBOT_SECRET=$secret" >> .env
echo "ROBOT_QQ=$qq" >> .env
echo "WEB_ACCESS_TOKEN=$token" >> .env

# 5. 生成链接
IP=$(curl -s https://api.ipify.org || echo "localhost")
WEB_URL="http://$IP:5001/web/?token=$token"

echo -e "\n${GREEN}✅ 安装完成！${NC}"
echo -e "Web 管理面板地址: ${BLUE}$WEB_URL${NC}\n"

# 6. 启动
echo -e "${GREEN}>>> 正在启动机器人...${NC}"
python3 main.py
