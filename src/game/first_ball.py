from color import Color
from math import sqrt
from random import randint
import pygame


class Ball():
    """ボールクラス"""

    def __init__(self, x, y, radius, sx, sy, color=Color.RED.value):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        """ボール移動"""
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        """ボールを食べる"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            dist = sqrt(dx**2 + dy**2)
            if dist < self.radius + other.radius and self.radius > other.radius:
                other.alive = False
                self.radius += int(other.radius * 0.138)

    def draw(self, screen):
        """ボールを絵描き"""
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)


def main():
    # init
    pygame.init()
    # Window設定
    screen = pygame.display.set_mode((800, 600))
    # タイトル設定
    pygame.display.set_caption('ボールゲーム')
    # ボール生成
    balls = []

    running = True
    # 繰り返す事件を始める
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # マウス事件を取得
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 位置を取得
                x, y = event.pos
                radius = randint(10, 30)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.get_random_color()
                # ボールを生成
                ball = Ball(x, y, radius, sx, sy, color)
                balls.append(ball)

        # Windowバックグラウンド設定
        screen.fill(Color.WHITE.value)
        # ボール処理
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        # Windowリフレッシュ
        pygame.display.flip()
        # ボール移動
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            for other in balls:
                ball.eat(other)


if __name__ == "__main__":
    main()
