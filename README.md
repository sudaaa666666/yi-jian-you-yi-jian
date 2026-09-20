# 一箭又一箭
## 游戏简介
“一箭又一箭”是一款基于Pygame实现的点击式箭头解谜小游戏。玩家需要观察棋盘上箭头的方向以及相互阻挡关系，按照合理顺序点击箭头，让所有箭头依次飞出棋盘。游戏规则简单，但需要判断二维坐标、方向、阻挡碰撞，是一次小型软件开发实践项目。

## 开发环境
- Python 3.10+
- pygame-ce（Pygame社区增强版）

## 安装和运行方法
1. 安装依赖库
```bash
pip install pygame-ce

2. 克隆项目到本地

git clone https://github.com/sudaaa66666/yi-jian-you-yi-jian.git
cd yi-jian-you-yi-jian

3. 运行游戏

python main.py

## 游戏操作说明

- 鼠标左键点击箭头，被点击的箭头会沿着自身方向飞出
- 如果箭头前进路径上存在其他箭头阻挡，则无法发射
- 游戏目标：按照正确顺序，发射棋盘上全部箭头，清空棋盘通关

## 游戏截图
> 
> 游戏运行截图
<img width="450" height="401" alt="微信图片_20260919205337" src="https://github.com/user-attachments/assets/3ff6eafd-26f5-4fad-a20b-07ce64bfe408" />

## 项目文件结构
.
├── main.py          # 游戏主程序源代码
├── README.md        # 项目说明文档
└── screenshot.png   # 游戏截图资源
