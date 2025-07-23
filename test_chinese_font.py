#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import sys
import os

def test_chinese_fonts():
    """测试Mac系统上的中文字体显示"""
    pygame.init()
    
    # 创建测试窗口
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("中文字体测试 - Chinese Font Test")
    
    # 测试文本
    test_texts = [
        "贪吃蛇游戏",
        "分数: 100",
        "游戏结束!",
        "按空格键重新开始",
        "中文显示测试 ABC 123"
    ]
    
    # Mac系统字体路径（STHeiti 优先）
    font_paths = [
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/STHeiti Medium.ttc", 
        "/System/Library/Fonts/STHeiti.ttc",
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/Arial Unicode MS.ttf",
        "/Library/Fonts/Arial Unicode MS.ttf"
    ]
    
    # Mac系统字体名称（STHeiti 优先）
    mac_fonts = ['STHeiti', 'STHeiti Light', 'STHeiti Medium', 'PingFang SC', 'Hiragino Sans GB', 'Arial Unicode MS']
    
    print("🔍 Mac中文字体测试")
    print("=" * 50)
    
    working_fonts = []
    
    # 测试文件路径字体
    print("\n📁 测试字体文件路径:")
    for font_path in font_paths:
        if os.path.exists(font_path):
            try:
                font = pygame.font.Font(font_path, 36)
                print(f"✅ {os.path.basename(font_path)} - 路径可用")
                
                # 测试渲染
                try:
                    text_surface = font.render("贪吃蛇游戏", True, (255, 255, 255))
                    working_fonts.append((font, os.path.basename(font_path)))
                    print(f"   ✅ 中文渲染成功")
                except Exception as e:
                    print(f"   ❌ 中文渲染失败: {e}")
                    
            except Exception as e:
                print(f"❌ {os.path.basename(font_path)} - 加载失败: {e}")
        else:
            print(f"❌ {os.path.basename(font_path)} - 文件不存在")
    
    # 测试系统字体名称
    print("\n🖥️  测试系统字体名称:")
    for font_name in mac_fonts:
        try:
            font = pygame.font.SysFont(font_name, 36)
            print(f"✅ {font_name} - 系统字体可用")
            
            # 测试渲染
            try:
                text_surface = font.render("贪吃蛇游戏", True, (255, 255, 255))
                working_fonts.append((font, font_name))
                print(f"   ✅ 中文渲染成功")
            except Exception as e:
                print(f"   ❌ 中文渲染失败: {e}")
                
        except Exception as e:
            print(f"❌ {font_name} - 加载失败: {e}")
    
    if not working_fonts:
        print("\n❌ 未找到可用的中文字体!")
        print("\n建议解决方案:")
        print("1. 确保您使用的是macOS系统")
        print("2. 运行 ./setup_mac.sh 安装额外字体")
        print("3. 检查系统语言设置是否包含中文")
        pygame.quit()
        return False
    
    print(f"\n✅ 找到 {len(working_fonts)} 个可用的中文字体")
    print("\n🎮 启动字体预览窗口...")
    print("按任意键切换字体，ESC键退出")
    
    # 字体预览
    clock = pygame.time.Clock()
    current_font_index = 0
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    current_font_index = (current_font_index + 1) % len(working_fonts)
        
        screen.fill((0, 0, 0))
        
        if working_fonts:
            font, font_name = working_fonts[current_font_index]
            
            # 显示字体名称
            title_font = pygame.font.Font(None, 24)
            title_text = title_font.render(f"Font: {font_name} ({current_font_index + 1}/{len(working_fonts)})", True, (255, 255, 0))
            screen.blit(title_text, (10, 10))
            
            # 显示测试文本
            y_offset = 80
            for i, text in enumerate(test_texts):
                try:
                    text_surface = font.render(text, True, (255, 255, 255))
                    screen.blit(text_surface, (50, y_offset + i * 60))
                except Exception as e:
                    error_text = title_font.render(f"渲染错误: {text}", True, (255, 0, 0))
                    screen.blit(error_text, (50, y_offset + i * 60))
            
            # 显示控制提示
            help_text = title_font.render("Press any key to switch font, ESC to exit", True, (128, 128, 128))
            screen.blit(help_text, (10, 550))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    print("\n✅ 字体测试完成!")
    return True

if __name__ == "__main__":
    print("🐍 Mac中文字体测试工具")
    print("用于验证贪吃蛇游戏的中文显示功能")
    print()
    
    try:
        test_chinese_fonts()
    except KeyboardInterrupt:
        print("\n\n⏹️  测试被用户中断")
    except Exception as e:
        print(f"\n❌ 测试过程中出错: {e}")
        sys.exit(1)