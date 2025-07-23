# 🍎 Mac系统中文显示支持说明

## 📋 概述

本贪吃蛇游戏已针对Mac系统优化，确保中文界面能够正确显示。游戏包含完整的中文界面，包括游戏标题、分数显示、游戏结束提示等。

## 🎯 支持的中文内容

- **游戏标题**: "贪吃蛇游戏"
- **分数显示**: "分数: XXX"  
- **游戏结束**: "游戏结束!"
- **操作提示**: "按空格键重新开始，ESC键退出"

## 🔧 字体支持系统

### Mac系统内置字体（优先使用）
1. **STHeiti Light/Medium** (华文黑体) - 优先使用的传统Mac中文字体
2. **PingFang SC** (苹方) - macOS Sierra及以后版本
3. **Hiragino Sans GB** (冬青黑体简体中文) - 经典Mac中文字体
4. **Arial Unicode MS** - 通用Unicode字体

### 字体加载优先级
```
1. 文件路径字体 (直接加载字体文件) - STHeiti 优先
   └── /System/Library/Fonts/STHeiti Light.ttc
   └── /System/Library/Fonts/STHeiti Medium.ttc
   └── /System/Library/Fonts/STHeiti.ttc
   └── /System/Library/Fonts/PingFang.ttc
   └── /System/Library/Fonts/Hiragino Sans GB.ttc
   └── /Library/Fonts/Arial Unicode MS.ttf

2. 系统字体名称 (通过系统字体API) - STHeiti 优先
   └── STHeiti
   └── STHeiti Light
   └── STHeiti Medium
   └── PingFang SC
   └── Hiragino Sans GB  
   └── Arial Unicode MS

3. 降级方案
   └── 通用字体
   └── pygame默认字体
```

## 🚀 快速安装

### 方法一：自动安装（推荐）
```bash
# 运行Mac专用安装脚本
./setup_mac.sh

# 启动游戏
./run_mac.sh
```

### 方法二：手动安装
```bash
# 1. 检查Python3
python3 --version

# 2. 安装pygame
pip3 install pygame==2.5.2

# 3. 运行游戏
python3 snake_game.py
```

## 🔍 字体测试

运行字体测试工具验证中文显示：

```bash
python3 test_chinese_font.py
```

测试工具功能：
- ✅ 检测可用的Mac中文字体
- ✅ 测试中文文本渲染
- ✅ 提供字体预览界面
- ✅ 显示字体加载状态

## 🛠️ 故障排除

### 问题1：中文显示为方块 □□□
**原因**: 字体加载失败或字体不支持中文

**解决方案**:
1. 运行字体测试：`python3 test_chinese_font.py`
2. 检查macOS版本（建议10.11+）
3. 确认系统语言包含中文
4. 重启应用程序

### 问题2：pygame导入失败
**错误信息**: `ModuleNotFoundError: No module named 'pygame'`

**解决方案**:
```bash
# 使用pip3安装
pip3 install pygame==2.5.2

# 如果权限问题，使用用户安装
pip3 install --user pygame==2.5.2

# 使用conda（如果已安装）
conda install pygame
```

### 问题3：脚本无执行权限
**错误信息**: `Permission denied`

**解决方案**:
```bash
chmod +x setup_mac.sh run_mac.sh
```

### 问题4：字体路径不存在
**现象**: 控制台显示多个"字体加载失败"

**说明**: 这是正常现象，系统会自动尝试多个字体路径，最终会找到可用的字体。

## 📱 系统兼容性

| macOS版本 | 支持状态 | 推荐字体 |
|-----------|----------|----------|
| macOS 12+ (Monterey) | ✅ 完全支持 | STHeiti |
| macOS 11 (Big Sur) | ✅ 完全支持 | STHeiti |
| macOS 10.15 (Catalina) | ✅ 完全支持 | STHeiti |
| macOS 10.14 (Mojave) | ✅ 完全支持 | STHeiti |
| macOS 10.13 (High Sierra) | ✅ 完全支持 | STHeiti |
| macOS 10.12 (Sierra) | ✅ 完全支持 | STHeiti |
| macOS 10.11 (El Capitan) | ⚠️ 基本支持 | STHeiti |

## 🎮 使用体验

### 正常显示效果
- 所有中文文字清晰可读
- 字体大小适中（36px）
- 文字颜色为白色，背景对比度良好
- 支持中英文混合显示

### 游戏界面预览
```
🎮 游戏窗口标题: "贪吃蛇游戏"
📊 左上角显示: "分数: 100"
💀 游戏结束时: "游戏结束!"
🔄 重启提示: "按空格键重新开始，ESC键退出"
```

## 📞 技术支持

如遇到中文显示问题：

1. **运行诊断**: `python3 test_chinese_font.py`
2. **查看日志**: 游戏启动时的字体加载信息
3. **检查系统**: 确认macOS版本和语言设置
4. **重新安装**: 运行 `./setup_mac.sh`

---

**✅ 经过测试，游戏在Mac系统上能够完美显示中文界面！**

*最后更新: 2025年1月23日*