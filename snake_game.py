import pygame
import random
import sys

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

# 方向常量
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

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
            return False
            
        # 检查自身碰撞
        if new_head in self.body:
            return False
            
        self.body.insert(0, new_head)
        
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
            
        return True
    
    def change_direction(self, new_direction):
        # 防止反向移动
        if (self.direction[0] * -1, self.direction[1] * -1) != new_direction:
            self.direction = new_direction
    
    def grow_snake(self):
        self.grow = True
    
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
        self.font = pygame.font.Font(None, 36)
        self.game_over = False
        
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
    
    def update(self):
        if not self.game_over:
            if not self.snake.move():
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
    
    def draw(self):
        self.screen.fill(BLACK)
        
        if not self.game_over:
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
        
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