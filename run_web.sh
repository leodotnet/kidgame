#!/bin/bash

echo "🐍 启动贪吃蛇游戏 Web版..."
echo "=================================="

# 检查是否有python3
if command -v python3 &> /dev/null; then
    echo "使用 Python3 启动本地服务器..."
    echo "游戏地址: http://localhost:8000"
    echo "按 Ctrl+C 停止服务器"
    echo ""
    python3 -m http.server 8000
elif command -v python &> /dev/null; then
    echo "使用 Python 启动本地服务器..."
    echo "游戏地址: http://localhost:8000"
    echo "按 Ctrl+C 停止服务器"
    echo ""
    python -m http.server 8000
else
    echo "未找到 Python，请直接用浏览器打开 index.html 文件"
    echo "或者安装 Python 后再运行此脚本"
    
    # 尝试直接打开浏览器
    if command -v xdg-open &> /dev/null; then
        xdg-open index.html
    elif command -v open &> /dev/null; then
        open index.html
    else
        echo "请手动用浏览器打开 index.html 文件"
    fi
fi