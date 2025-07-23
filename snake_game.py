import pygame
import random
import sys
import math

# 初始化pygame
pygame.init()

# 游戏配置
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
CELL_NUMBER_X = WINDOW_WIDTH // CELL_SIZE
CELL_NUMBER_Y = WINDOW_HEIGHT // CELL_SIZE

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_GREEN = (0, 100, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)

# 方向常量
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.vx = random.uniform(-5, 5)
        self.vy = random.uniform(-5, 5)
        self.color = color
        self.life = 60  # 粒子生命周期（帧数）
        self.max_life = 60
        self.size = random.uniform(2, 6)
        
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.1  # 重力效果
        self.life -= 1
        
        # 减小粒子大小
        self.size = max(0, self.size * 0.98)
        
        return self.life > 0
    
    def draw(self, screen):
        if self.life > 0:
            # 根据生命周期调整透明度
            alpha = int(255 * (self.life / self.max_life))
            color_with_alpha = (*self.color, alpha)
            
            # 创建一个带透明度的表面
            particle_surface = pygame.Surface((int(self.size * 2), int(self.size * 2)), pygame.SRCALPHA)
            pygame.draw.circle(particle_surface, color_with_alpha, 
                             (int(self.size), int(self.size)), int(self.size))
            screen.blit(particle_surface, (self.x - self.size, self.y - self.size))

class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.particles = []
        self.active = True
        self.explosion_sound_played = False
        
        # 创建爆炸粒子
        colors = [RED, ORANGE, YELLOW, WHITE]
        for _ in range(30):  # 创建30个粒子
            color = random.choice(colors)
            particle = Particle(x, y, color)
            self.particles.append(particle)
    
    def update(self):
        if not self.active:
            return
            
        # 更新所有粒子
        self.particles = [p for p in self.particles if p.update()]
        
        # 如果没有粒子了，爆炸结束
        if not self.particles:
            self.active = False
    
    def draw(self, screen):
        if self.active:
            for particle in self.particles:
                particle.draw(screen)

class Snake:
    def __init__(self):
        self.body = [(CELL_NUMBER_X // 2, CELL_NUMBER_Y // 2)]
        self.direction = RIGHT
        self.grow = False
        
    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # 检查边界碰撞
        if (new_head[0] < 0 or new_head[0] >= CELL_NUMBER_X or 
            new_head[1] < 0 or new_head[1] >= CELL_NUMBER_Y):
            return False, "wall"  # 返回碰撞类型
            
        # 检查自身碰撞
        if new_head in self.body:
            return False, "self"  # 返回碰撞类型
            
        self.body.insert(0, new_head)
        
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
            
        return True, None
    
    def change_direction(self, new_direction):
        # 防止反向移动
        if (self.direction[0] * -1, self.direction[1] * -1) != new_direction:
            self.direction = new_direction
    
    def grow_snake(self):
        self.grow = True
    
    def get_head_position_pixels(self):
        """获取蛇头在像素坐标系中的位置"""
        head_x, head_y = self.body[0]
        return (head_x * CELL_SIZE + CELL_SIZE // 2, head_y * CELL_SIZE + CELL_SIZE // 2)
    
    def draw(self, screen):
        for i, segment in enumerate(self.body):
            x = segment[0] * CELL_SIZE
            y = segment[1] * CELL_SIZE
            
            # 蛇头用不同颜色
            color = DARK_GREEN if i == 0 else GREEN
            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)

class Food:
    def __init__(self):
        self.position = self.generate_position()
    
    def generate_position(self):
        x = random.randint(0, CELL_NUMBER_X - 1)
        y = random.randint(0, CELL_NUMBER_Y - 1)
        return (x, y)
    
    def draw(self, screen):
        x = self.position[0] * CELL_SIZE
        y = self.position[1] * CELL_SIZE
        pygame.draw.rect(screen, RED, (x, y, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("贪吃蛇游戏")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.explosions = []  # 存储爆炸效果
        
        # 改进的中文字体加载
        self.font = self._load_chinese_font()
        self.game_over = False
    
    def _load_chinese_font(self):
        """加载支持中文的字体"""
        font_paths = [
            # macOS 系统字体（优先）
            "/System/Library/Fonts/PingFang.ttc",
            "/System/Library/Fonts/Helvetica.ttc",
            "/System/Library/Fonts/STHeiti Light.ttc",
            "/System/Library/Fonts/STHeiti Medium.ttc",
            "/System/Library/Fonts/Hiragino Sans GB.ttc",
            "/System/Library/Fonts/Arial Unicode MS.ttf",
            "/Library/Fonts/Arial Unicode MS.ttf",
            # Homebrew 安装的字体
            "/usr/local/share/fonts/wqy-zenhei.ttc",
            "/usr/local/share/fonts/wqy-microhei.ttc",
            # Linux 字体（保持兼容性）
            "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
            "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
            "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
            "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            # Windows 字体（保持兼容性）
            "C:/Windows/Fonts/msyh.ttc",
        ]
        
        # 尝试加载字体
        for font_path in font_paths:
            try:
                font = pygame.font.Font(font_path, 36)
                print(f"成功加载字体: {font_path}")
                return font
            except (FileNotFoundError, OSError) as e:
                print(f"字体加载失败: {font_path} - {e}")
                continue
        
        # 如果所有字体都失败，尝试系统字体
        try:
            print("尝试使用系统默认字体...")
            # macOS 系统字体名称
            mac_fonts = ['PingFang SC', 'Hiragino Sans GB', 'STHeiti', 'Arial Unicode MS']
            for font_name in mac_fonts:
                try:
                    font = pygame.font.SysFont(font_name, 36)
                    print(f"成功加载系统字体: {font_name}")
                    return font
                except:
                    continue
            # 通用字体
            return pygame.font.SysFont('simsun,arial,helvetica,sans-serif', 36)
        except:
            print("使用pygame默认字体（可能不支持中文）")
            return pygame.font.Font(None, 36)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_SPACE:
                        self.restart_game()
                    elif event.key == pygame.K_ESCAPE:
                        return False
                else:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction(UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction(RIGHT)
        return True
    
    def create_explosion(self, x, y):
        """在指定位置创建爆炸效果"""
        explosion = Explosion(x, y)
        self.explosions.append(explosion)
    
    def update(self):
        if not self.game_over:
            move_result, collision_type = self.snake.move()
            if not move_result:
                # 如果撞墙，在蛇头位置创建爆炸效果
                if collision_type == "wall":
                    head_x, head_y = self.snake.get_head_position_pixels()
                    self.create_explosion(head_x, head_y)
                # 如果撞到自己，也可以创建爆炸效果
                elif collision_type == "self":
                    head_x, head_y = self.snake.get_head_position_pixels()
                    self.create_explosion(head_x, head_y)
                
                self.game_over = True
                return
            
            # 检查是否吃到食物
            if self.snake.body[0] == self.food.position:
                self.snake.grow_snake()
                self.score += 10
                
                # 生成新食物，确保不在蛇身上
                while True:
                    self.food.position = self.food.generate_position()
                    if self.food.position not in self.snake.body:
                        break
        
        # 更新爆炸效果
        self.explosions = [explosion for explosion in self.explosions if explosion.active]
        for explosion in self.explosions:
            explosion.update()
    
    def draw(self):
        self.screen.fill(BLACK)
        
        if not self.game_over:
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
        
        # 绘制爆炸效果
        for explosion in self.explosions:
            explosion.draw(self.screen)
        
        # 显示分数
        score_text = self.font.render(f"分数: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # 游戏结束界面
        if self.game_over:
            game_over_text = self.font.render("游戏结束!", True, WHITE)
            restart_text = self.font.render("按空格键重新开始，ESC键退出", True, WHITE)
            
            game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            
            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
    
    def restart_game(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False
        self.explosions = []  # 清空爆炸效果
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)  # 控制游戏速度
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()