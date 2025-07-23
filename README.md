# 🐍 贪吃蛇游戏 (Snake Game)

一个用Python和Pygame开发的经典贪吃蛇游戏，支持中文界面显示，兼容Mac、Linux和Windows系统。

## 🌟 特性

- 🎮 经典贪吃蛇游戏玩法
- 🇨🇳 完整中文界面支持
- 🖥️ 跨平台兼容 (Mac/Linux/Windows)
- 🎯 智能字体加载系统
- 🔄 游戏结束后可重新开始
- ⌨️ 响应式键盘控制

## 🚀 Mac系统快速开始

### 方法一：一键安装运行
```bash
# 1. 运行安装脚本
./setup_mac.sh

# 2. 启动游戏
./run_mac.sh
```

### 方法二：手动安装
```bash
# 1. 确保已安装Python3
python3 --version

# 2. 安装pygame
pip3 install pygame==2.5.2

# 3. 直接运行游戏
python3 snake_game.py
```

### 测试中文字体
```bash
# 运行字体测试工具
python3 test_chinese_font.py
```

## 🐧 Linux系统

```bash
# 安装依赖
sudo apt update
sudo apt install -y python3-pygame fonts-wqy-zenhei fonts-wqy-microhei

# 运行游戏
./run_game.sh
# 或
python3 snake_game.py
```

## 🪟 Windows系统

```bash
# 安装pygame
pip install pygame==2.5.2

# 运行游戏  
python snake_game.py
```

## 🎮 游戏控制

| 按键 | 功能 |
|------|------|
| ↑↓←→ | 控制蛇的移动方向 |
| 空格键 | 游戏结束后重新开始 |
| ESC | 退出游戏 |

## 🔧 中文显示支持

游戏内置智能字体加载系统，支持以下字体：

### Mac系统字体
- PingFang SC (苹方)
- Hiragino Sans GB (冬青黑体简体中文)  
- STHeiti (华文黑体)
- Arial Unicode MS

### Linux系统字体
- WenQuanYi Zen Hei (文泉驿正黑)
- WenQuanYi Micro Hei (文泉驿微米黑)
- Noto Sans CJK

### Windows系统字体
- Microsoft YaHei (微软雅黑)

## 📁 项目结构

```
snake-game/
├── snake_game.py           # 主游戏文件
├── setup_mac.sh           # Mac系统安装脚本
├── run_mac.sh             # Mac系统运行脚本  
├── run_game.sh            # Linux系统运行脚本
├── test_chinese_font.py   # 中文字体测试工具
├── requirements.txt       # Python依赖
├── README.md             # 项目说明
└── GAME_INFO.md          # 游戏详细信息
```

## 🔍 故障排除

### 中文显示为方块
1. 运行字体测试：`python3 test_chinese_font.py`
2. Mac用户：运行 `./setup_mac.sh` 安装字体
3. Linux用户：安装中文字体包
4. 检查系统语言设置

### pygame导入错误
```bash
# Mac
pip3 install pygame==2.5.2

# Linux
sudo apt install python3-pygame

# Windows  
pip install pygame==2.5.2
```

### 权限错误 (Mac/Linux)
```bash
chmod +x setup_mac.sh run_mac.sh run_game.sh
```

## 🎯 游戏截图

游戏界面包含：
- 中文游戏标题："贪吃蛇游戏"
- 实时分数显示："分数: XXX"
- 游戏结束提示："游戏结束!"
- 操作说明："按空格键重新开始，ESC键退出"

## 🤝 贡献

欢迎提交Issue和Pull Request来改进游戏！

## 📄 许可证

MIT License - 详见LICENSE文件

---

🎮 **享受游戏吧！** 如有问题请提交Issue。
