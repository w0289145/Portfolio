import sys

import pygame

SCREEN_SIZE = 900, 700

# object dimensions
BRICK_WIDTH = 60
BRICK_HEIGHT = 15
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 12
BALL_DIAMETER = 16
BALL_RADIUS = BALL_DIAMETER / 2


MAX_PADDLE_X = SCREEN_SIZE[0] - PADDLE_WIDTH
MAX_BALL_X = SCREEN_SIZE[0] - BALL_DIAMETER
MAX_BALL_Y = SCREEN_SIZE[1] - BALL_DIAMETER

# paddle position  Y
PADDLE_Y = SCREEN_SIZE[1] - PADDLE_HEIGHT - 10

# color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRICK_COLOR = (0, 75, 133)

# state constants
STATE_BALL_IN_PADDLE = 0
STATE_PLAYING = 1
STATE_WON = 2
STATE_GAME_OVER = 3
STATE_CHANGING_LEVEL = 4


class BrickBreak:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("BrickBreaker by Tristin Mckellar")

        self.clock = pygame.time.Clock()

        if pygame.font:
            self.font = pygame.font.Font(None, 30)
        else:
            self.font = None

        # change the variable to load a specific level first
        # variable (level, score, lives)
        self.init_game(6, 0, 3)

    def init_game(self, thelevel, thescore, thelives):
        self.level = thelevel
        self.lives = thelives
        self.score = thescore
        self.state = STATE_BALL_IN_PADDLE

        self.paddle = pygame.Rect(300, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.ball = pygame.Rect(300, PADDLE_Y - BALL_DIAMETER, BALL_DIAMETER, BALL_DIAMETER)

        self.ball_vel = [5, -5]


        if self.level == 1:
            self.create_bricks1()
        elif self.level == 2:
            self.create_bricks2()
        elif self.level == 3:
            self.create_bricks3()
        elif self.level == 4:
            self.create_bricks4()
        elif self.level == 5:
            self.create_bricks5()
        elif self.level == 6:
            self.create_bricks6()
        elif self.level == 7:
            self.create_bricks7()
        elif self.level == 8:
            self.create_bricks8()
        elif self.level == 9:
            self.create_bricks9()


    # here is all the code to create the bricks for different levels

    # level 1
    def create_bricks1(self):
        # position of bricks
        y_ofs = 35
        self.bricks = []
        for i in range(1):
            x_ofs = 35
            for j in range(12):
                self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                # distance apart(bricks)
                x_ofs += BRICK_WIDTH + 10
            y_ofs += BRICK_HEIGHT + 5

    # level 2
    def create_bricks2(self):
        y_ofs = 35
        self.bricks = []
        for i in range(3):
            x_ofs = 35
            for j in range(12):
                self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                x_ofs += BRICK_WIDTH + 10
            y_ofs += BRICK_HEIGHT + 5

    # level 3
    def create_bricks3(self):
        y_ofs = 35
        self.bricks = []
        for i in range(5):
            x_ofs = 35
            for j in range(12):
                self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                x_ofs += BRICK_WIDTH + 10
            y_ofs += BRICK_HEIGHT + 5

    # level 4
    def create_bricks4(self):
        y_ofs = 35
        self.bricks = []
        for i in range(7):
            x_ofs = 35
            for j in range(12):
                self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                x_ofs += BRICK_WIDTH + 10
            y_ofs += BRICK_HEIGHT + 5

    # level 5
    def create_bricks5(self):
        y_ofs = 35
        self.bricks = []
        for i in range(9):
            x_ofs = 35
            for j in range(12):
                self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                x_ofs += BRICK_WIDTH + 10
            y_ofs += BRICK_HEIGHT + 5

    # level 6
    def create_bricks6(self):
        y_ofs = 35
        self.bricks = []
        for i in range(11):
            x_ofs = 35
            for j in range(12):
                self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                x_ofs += BRICK_WIDTH + 10
            y_ofs += BRICK_HEIGHT + 5

    # level 7
    def create_bricks7(self):
        y_ofs = 35
        self.bricks = []
        for i in range(13):
            x_ofs = 35
            for j in range(12):
                self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                x_ofs += BRICK_WIDTH + 10
            y_ofs += BRICK_HEIGHT + 5


        # level 8
    def create_bricks8(self):
        y_ofs = 35
        self.bricks = []
        for i in range(15):
            x_ofs = 35
            for j in range(12):
                self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                x_ofs += BRICK_WIDTH + 10
            y_ofs += BRICK_HEIGHT + 5



    # level 9
    def create_bricks9(self):
        y_ofs = 35
        self.bricks = []
        for i in range(17):
            x_ofs = 35
            for j in range(12):
                self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
                x_ofs += BRICK_WIDTH + 10
            y_ofs += BRICK_HEIGHT + 5



    def draw_bricks(self):
        for brick in self.bricks:
            pygame.draw.rect(self.screen, BRICK_COLOR, brick)

    def check_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.paddle.left -= 10
            if self.paddle.left < 0:
                self.paddle.left = 0

        if keys[pygame.K_RIGHT]:
            self.paddle.left += 10
            if self.paddle.left > MAX_PADDLE_X:
                self.paddle.left = MAX_PADDLE_X

        if keys[pygame.K_SPACE] and self.state == STATE_BALL_IN_PADDLE:
            self.ball_vel = [7, -7]
            self.state = STATE_PLAYING

        elif keys[pygame.K_RETURN] and self.state == STATE_WON:
            self.level += 1
            self.lives += 1
            self.init_game(self.level, self.score, self.lives)

        elif keys[pygame.K_RETURN] and self.state == STATE_GAME_OVER:
            self.init_game(0, 0, 3)

    def move_ball(self):
        self.ball.left += self.ball_vel[0]
        self.ball.top += self.ball_vel[1]

        if self.ball.left <= 0:
            self.ball.left = 0
            self.ball_vel[0] = -self.ball_vel[0]
        elif self.ball.left >= MAX_BALL_X:
            self.ball.left = MAX_BALL_X
            self.ball_vel[0] = -self.ball_vel[0]

        if self.ball.top < 0:
            self.ball.top = 0
            self.ball_vel[1] = -self.ball_vel[1]

    def handle_collisions(self):
        for brick in self.bricks:
            if self.ball.colliderect(brick):
                self.score += 1
                self.ball_vel[1] = -self.ball_vel[1]
                self.bricks.remove(brick)
                break

        if len(self.bricks) == 0:
            self.state = STATE_WON

        if self.ball.colliderect(self.paddle):
            self.ball.top = PADDLE_Y - BALL_DIAMETER
            self.ball_vel[1] = -self.ball_vel[1]

        # if the ball hits the ground
        elif self.ball.top > self.paddle.top:
            self.lives -= 1
            if self.lives > 0:
                self.state = STATE_BALL_IN_PADDLE
            else:
                self.state = STATE_GAME_OVER



    def show_stats(self):
        if self.font:
            font_surface = self.font.render(
                "LEVEL: " + str(self.level + 0) + " SCORE: " + str(self.score) + " LIVES: " + str(self.lives), False,
                BLACK)
            self.screen.blit(font_surface, (205, 5))

    def show_message(self, message):
        if self.font:
            size = self.font.size(message)
            font_surface = self.font.render(message, False, (0, 75, 133))
            x = (SCREEN_SIZE[0] - size[0])
            y = (SCREEN_SIZE[1] - size[1]) / 1
            self.screen.blit(font_surface, (x, y))

    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.clock.tick(50)
            self.screen.fill(WHITE)
            self.check_input()

            if self.state == STATE_PLAYING:
                self.move_ball()
                self.handle_collisions()
            elif self.state == STATE_BALL_IN_PADDLE:
                self.ball.left = self.paddle.left + self.paddle.width / 2
                self.ball.top = self.paddle.top - self.ball.height
                self.show_message("PRESS SPACE TO START")
            elif self.state == STATE_GAME_OVER:
                self.show_message("GAME OVER. PRESS ENTER TO RESTART")
            elif self.state == STATE_WON:
                self.show_message("YOU WON! PRESS ENTER TO PLAY THE NEXT LEVEL")
            elif self.state == STATE_WON and self.level == 9:
                self.show_message("CONGRATULATIONS, YOU'VE COMPLETED THE GAME!!")

            # draw paddle
            pygame.draw.rect(self.screen, (233, 118, 9), self.paddle)                                                    # PADDLE COLOR

            # draw ball
            pygame.draw.circle(self.screen, BLACK, (self.ball.left + BALL_RADIUS, self.ball.top + BALL_RADIUS),          # BALL COLOR
                               BALL_RADIUS)

            self.draw_bricks()

            self.show_stats()

            pygame.display.flip()


if __name__ == "__main__":
    BrickBreak().run()
