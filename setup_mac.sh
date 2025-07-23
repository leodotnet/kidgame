#!/bin/bash

echo "🐍 贪吃蛇游戏 - Mac 系统安装脚本"
echo "=================================="

# 检查是否安装了Python3
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装"
    echo "请先安装Python3："
    echo "1. 访问 https://www.python.org/downloads/"
    echo "2. 或使用 Homebrew: brew install python"
    exit 1
fi

echo "✅ Python3 已安装: $(python3 --version)"

# 检查是否安装了pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 未安装"
    echo "请先安装pip3"
    exit 1
fi

echo "✅ pip3 已安装"

# 检查是否安装了Homebrew（可选）
if command -v brew &> /dev/null; then
    echo "✅ Homebrew 已安装"
    
    # 安装中文字体（可选）
    echo "📦 安装中文字体支持..."
    brew tap homebrew/cask-fonts 2>/dev/null || true
    brew install --cask font-wqy-zenhei 2>/dev/null || echo "字体已存在或安装失败（非必需）"
    brew install --cask font-wqy-microhei 2>/dev/null || echo "字体已存在或安装失败（非必需）"
else
    echo "⚠️  Homebrew 未安装（可选）"
    echo "如需安装更多中文字体，可安装Homebrew："
    echo '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
fi

# 安装pygame
echo "📦 安装pygame..."
pip3 install pygame==2.5.2

if [ $? -eq 0 ]; then
    echo "✅ pygame 安装成功"
else
    echo "❌ pygame 安装失败"
    echo "请尝试："
    echo "pip3 install --user pygame==2.5.2"
    exit 1
fi

# 检查macOS系统字体
echo "🔍 检查系统中文字体..."
fonts_found=0

font_paths=(
    "/System/Library/Fonts/PingFang.ttc"
    "/System/Library/Fonts/STHeiti Light.ttc"
    "/System/Library/Fonts/Hiragino Sans GB.ttc"
    "/System/Library/Fonts/Arial Unicode MS.ttf"
)

for font_path in "${font_paths[@]}"; do
    if [ -f "$font_path" ]; then
        echo "✅ 找到字体: $(basename "$font_path")"
        fonts_found=$((fonts_found + 1))
    fi
done

if [ $fonts_found -gt 0 ]; then
    echo "✅ 找到 $fonts_found 个中文字体，游戏应该能正常显示中文"
else
    echo "⚠️  未找到系统中文字体，可能需要手动安装"
fi

echo ""
echo "🎮 安装完成！"
echo "运行游戏: ./run_mac.sh 或 python3 snake_game.py"
echo ""
echo "游戏控制："
echo "• 方向键：控制蛇的移动"
echo "• 空格键：游戏结束后重新开始"
echo "• ESC键：退出游戏"