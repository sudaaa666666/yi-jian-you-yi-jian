import pygame

# 初始化pygame
pygame.init()

# 窗口设置
CELL_SIZE = 80
GRID_ROW = 5
GRID_COL = 5
WIDTH = CELL_SIZE * GRID_COL
HEIGHT = CELL_SIZE * GRID_ROW
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("一箭又一箭")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
BLUE = (30, 120, 220)
GRAY = (160, 160, 160)

# 方向常量：上、右、下、左
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# 箭头数据：(行,列,方向,是否存在)
arrows = [
    (0, 0, RIGHT, True),
    (1, 1, DOWN, True),
    (2, 2, UP, True),
    (3, 0, RIGHT, True),
    (0, 3, DOWN, True),
    (4, 4, LEFT, True),
    (3, 3, UP, True),
]

# 方向对应的箭头符号
arrow_text = ["↑", "→", "↓", "←"]
font = pygame.font.SysFont("simhei", 48)


def is_blocked(r, c, dire, arr_list):
    """检测箭头飞出路径是否被其他箭头阻挡，完善四个方向边界判断"""
    dr, dc = 0, 0
    if dire == UP:
        dr, dc = -1, 0
    elif dire == DOWN:
        dr, dc = 1, 0
    elif dire == LEFT:
        dr, dc = 0, -1
    elif dire == RIGHT:
        dr, dc = 0, 1

    nr, nc = r + dr, c + dc
    # 逐格扫描直到棋盘边界
    while 0 <= nr < GRID_ROW and 0 <= nc < GRID_COL:
        for (ar, ac, ad, alive) in arr_list:
            if alive and ar == nr and ac == nc:
                return True  # 路径上存在箭头，被阻挡
        nr += dr
        nc += dc
    return False


def draw_board():
    screen.fill(WHITE)
    # 画网格
    for i in range(GRID_ROW + 1):
        pygame.draw.line(screen, GRAY, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 2)
    for j in range(GRID_COL + 1):
        pygame.draw.line(screen, GRAY, (j * CELL_SIZE, 0), (j * CELL_SIZE, HEIGHT), 2)

    # 绘制存活箭头
    for (r, c, d, alive) in arrows:
        if alive:
            tx = c * CELL_SIZE + CELL_SIZE // 2
            ty = r * CELL_SIZE + CELL_SIZE // 2
            text_surf = font.render(arrow_text[d], True, RED)
            rect = text_surf.get_rect(center=(tx, ty))
            screen.blit(text_surf, rect)


def get_click_arrow(mx, my):
    """根据鼠标点击位置，找到被点击的箭头索引"""
    col = mx // CELL_SIZE
    row = my // CELL_SIZE
    for idx, (r, c, d, alive) in enumerate(arrows):
        if alive and r == row and c == col:
            return idx
    return None


# 游戏主循环
running = True
while running:
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            idx = get_click_arrow(mouse_x, mouse_y)
            if idx is not None:
                r, c, dire, alive = arrows[idx]
                if not is_blocked(r, c, dire, arrows):
                    # 移除箭头，飞出
                    arrows[idx] = (r, c, dire, False)
                else:
                    print("被挡住，不能发射！")
    pygame.display.flip()

pygame.quit()
