import pygame, sys, time, random
import pygame.event as event

# 定義頻色變數
redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)

def gameOver(playSurface, score):
    txtFont = pygame.font.SysFont('arial.ttf', 54)
    
    txtSurf = txtFont.render('Game Over!', True, greyColour)
    txtRect = txtSurf.get_rect()
    txtRect.midbottom = (playSurface.get_rect().centerx , txtFont.get_height() )
    playSurface.blit(txtSurf, txtRect)

    txtSurf = txtFont.render('Score:' + str(score), True, greyColour)
    txtRect = txtSurf.get_rect()
    txtRect.midtop = (playSurface.get_rect().centerx, txtFont.get_height() )
    playSurface.blit(txtSurf, txtRect)
    
    pygame.display.update()
    
    time.sleep(2)
    pygame.quit()
    sys.exit()


def main():

    # 初始化pygame
    pygame.init()
    fpsClock = pygame.time.Clock()
    
    # 創建pygame顯示層
    playSurface = pygame.display.set_mode((600, 460))
    pygame.display.set_caption('Snake Game')
    
    # 初始化變數
    snakePosition = (100, 100)  # 貪吃蛇 蛇頭的位置
    snakeSegments = [snakePosition]  # 貪吃蛇 蛇的身體，初始為一個單位
    raspberryPosition = (300, 300)  # 樹莓的初始位置
    direction = '右'  # 初始方向為右
    score = 0  # 初始得分
    
    while True:
        
        # 檢測例如按鍵等pygame事件
        for e in event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            elif e.type == pygame.KEYDOWN:
                # 判斷鍵盤事件
                if e.key == pygame.K_RIGHT and direction in '上下':
                    direction = '右'
                if e.key == pygame.K_LEFT and direction in '上下':
                    direction = '左'
                if e.key == pygame.K_UP and direction in '左右':
                    direction = '上'
                if e.key == pygame.K_DOWN and direction in '左右':
                    direction = '下'
                if e.key == pygame.K_ESCAPE:
                    event.post(event.Event(pygame.QUIT))
                
        # 根據方向來設定(移動)新蛇頭的座標
        (x, y) = snakePosition
        if direction == '右':
            snakePosition = (x+20, y)
        elif direction == '左':
            snakePosition = (x-20, y)
        elif direction == '下':
            snakePosition = (x, y+20)
        else:  # direction == '上':
            snakePosition = (x, y-20)
        
        # 增加蛇的長度
        snakeSegments.insert(0, snakePosition)
        
        # 判斷是否吃掉了樹莓
        if snakePosition != raspberryPosition:  # 如果沒有吃到樹莓
            snakeSegments.pop() # 就把身體的最後一節(尾巴)刪掉

        else:   # 如果吃掉樹莓，則重新生成樹莓
            x = random.randrange(0, 30) * 20
            y = random.randrange(0, 23) * 20
            raspberryPosition = (x, y)
            score += 1
        
        # 清空、重繪pygame顯示層
        playSurface.fill(blackColour)

        # 重繪身體
        for seg in snakeSegments:
            pygame.draw.rect(playSurface, whiteColour, pygame.Rect(seg[0], seg[1], 20, 20))
        
        # 重繪樹莓
        pygame.draw.rect(playSurface, redColour, pygame.Rect(raspberryPosition[0], raspberryPosition[1], 20, 20))
        
        # 刷新pygame顯示層
        pygame.display.update()
        
        # 判斷是否死亡
        if snakePosition[0] > 600 or snakePosition[0] < 0:  # X軸有沒有超出視窗
            gameOver(playSurface, score)
        
        elif snakePosition[1] > 460 or snakePosition[1] < 0:    # Y軸有沒有超出視窗
            gameOver(playSurface, score)
        
        else:   # 是否吃到自己身體
            for seg in snakeSegments[1:]:
                if snakePosition == seg:    
                    gameOver(playSurface, score)
        
        # 控制遊戲速度
        fpsClock.tick(7)


if __name__ == "__main__":
    main()
