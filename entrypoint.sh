#!/bin/bash
set -e

echo ">>> 正在检查并安装依赖..."
pip install --no-cache-dir -r requirements.txt

echo ">>> 正在启动 ElainaBot..."
python main.py
