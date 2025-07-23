#!/bin/bash

echo "🐍 启动贪吃蛇游戏 (Mac版)"
echo "========================"
echo ""
echo "游戏控制说明："
echo "• 使用方向键 ↑↓←→ 控制蛇的移动"
echo "• 按 ESC 键或关闭窗口退出游戏"
echo "• 游戏结束后按空格键重新开始"
echo ""

# 检查Python3是否可用
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: Python3 未安装"
    echo "请先运行 ./setup_mac.sh 进行安装"
    exit 1
fi

# 检查pygame是否已安装
python3 -c "import pygame" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ 错误: pygame 未安装"
    echo "请先运行 ./setup_mac.sh 进行安装"
    exit 1
fi

echo "🎮 正在启动游戏..."
echo ""

# 设置环境变量以确保在Mac上正常运行
export PYGAME_HIDE_SUPPORT_PROMPT=1

# 启动游戏
python3 snake_game.py