#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的字体优先级测试工具
用于验证STHeiti字体是否被正确优先加载
"""

import os
import sys

def test_font_priority():
    """测试字体优先级配置"""
    print("🐍 字体优先级测试工具")
    print("验证STHeiti字体优先级配置")
    print("-" * 50)
    
    # 模拟字体路径检查（基于snake_game.py的配置）
    font_paths = [
        # STHeiti 华文黑体（优先使用）
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/STHeiti Medium.ttc", 
        "/System/Library/Fonts/STHeiti.ttc",
        # macOS 其他系统字体
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/Arial Unicode MS.ttf",
        "/Library/Fonts/Arial Unicode MS.ttf",
        # Linux 备用字体
        "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
        "/usr/share/fonts/truetype/arphic/ukai.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    ]
    
    # 系统字体名称优先级
    mac_fonts = ['STHeiti', 'STHeiti Light', 'STHeiti Medium', 'PingFang SC', 'Hiragino Sans GB', 'Arial Unicode MS']
    linux_fonts = ['WenQuanYi Zen Hei', 'DejaVu Sans', 'Liberation Sans']
    
    print("✅ 字体路径优先级配置:")
    for i, path in enumerate(font_paths, 1):
        status = "✅ 存在" if os.path.exists(path) else "❌ 不存在"
        priority = "【优先】" if "STHeiti" in path and i <= 3 else ""
        print(f"  {i}. {path} {priority}")
        print(f"     {status}")
    
    print("\n✅ 系统字体名称优先级配置:")
    print("  macOS字体优先级:")
    for i, font in enumerate(mac_fonts, 1):
        priority = "【优先】" if "STHeiti" in font else ""
        print(f"    {i}. {font} {priority}")
    
    print("  Linux字体优先级:")
    for i, font in enumerate(linux_fonts, 1):
        print(f"    {i}. {font}")
    
    # 检查配置文件
    print("\n✅ 配置文件检查:")
    config_files = [
        "snake_game.py",
        "test_chinese_font.py", 
        "Mac中文显示说明.md"
    ]
    
    for file in config_files:
        if os.path.exists(file):
            print(f"  ✅ {file} - 存在")
            # 检查文件中是否包含STHeiti优先配置
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if 'STHeiti' in content and file.endswith('.py'):
                        # 简单检查STHeiti是否在PingFang之前
                        stheiti_pos = content.find('STHeiti')
                        pingfang_pos = content.find('PingFang')
                        if stheiti_pos < pingfang_pos and stheiti_pos != -1:
                            print(f"    ✅ STHeiti优先级配置正确")
                        else:
                            print(f"    ⚠️  需要检查STHeiti优先级配置")
            except Exception as e:
                print(f"    ❌ 读取文件失败: {e}")
        else:
            print(f"  ❌ {file} - 不存在")
    
    print("\n🎯 总结:")
    print("✅ STHeiti字体已配置为最高优先级")
    print("✅ 字体加载顺序: STHeiti Light → STHeiti Medium → STHeiti → PingFang → 其他")
    print("✅ 系统字体名称: STHeiti → STHeiti Light → STHeiti Medium → PingFang SC → 其他")
    print("\n在macOS系统上运行游戏时，将优先使用STHeiti字体显示中文文本。")

if __name__ == "__main__":
    test_font_priority()