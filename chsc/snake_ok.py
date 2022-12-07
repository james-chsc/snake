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
    snakePosition = [100, 100]  # 貪吃蛇 蛇頭的位置
    snakeSegments = [snakePosition]  # 貪吃蛇 蛇的身體，初始為一個單位
    raspberryPosition = [300, 300]  # 樹莓的初始位置
    direction = '右'  # 初始方向為右
    changeDirection = ''    # 下一個方向
    score = 0  # 初始得分
    
    while True:
        
        # 檢測例如按鍵等pygame事件
        for e in event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
            elif e.type == pygame.KEYDOWN:
                # 判斷鍵盤事件
                if e.key == pygame.K_RIGHT:
                    changeDirection = '右'
                if e.key == pygame.K_LEFT:
                    changeDirection = '左'
                if e.key == pygame.K_UP:
                    changeDirection = '上'
                if e.key == pygame.K_DOWN:
                    changeDirection = '下'
                if e.key == pygame.K_ESCAPE:
                    event.post(event.Event(pygame.QUIT))
        
        # 判斷是否輸入了反方向
        if changeDirection == '右' and not direction == '左':
            direction = changeDirection
        if changeDirection == '左' and not direction == '右':
            direction = changeDirection
        if changeDirection == '上' and not direction == '下':
            direction = changeDirection
        if changeDirection == '下' and not direction == '上':
            direction = changeDirection
        
        # 根據方向移動蛇頭的座標
        if direction == '右':
            snakePosition[0] += 20
        elif direction == '左':
            snakePosition[0] -= 20
        elif direction == '下':
            snakePosition[1] += 20
        else:  # direction == '上':
            snakePosition[1] -= 20
        
        # 增加蛇的長度
        snakeSegments.insert(0, list(snakePosition))
        
        # 判斷是否吃掉了樹莓
        if snakePosition != raspberryPosition:
            snakeSegments.pop() # 刪掉尾巴

        else:   # 如果吃掉樹莓，則重新生成樹莓
            x = random.randrange(1, 30)
            y = random.randrange(1, 23)
            raspberryPosition = [int(x * 20), int(y * 20)]
            score += 1
        
        # 繪製pygame顯示層
        playSurface.fill(blackColour)
        for position in snakeSegments:
            pygame.draw.rect(playSurface, whiteColour, 
                pygame.Rect(position[0], position[1], 20, 20))
            pygame.draw.rect(playSurface, redColour, 
                pygame.Rect(raspberryPosition[0], raspberryPosition[1], 20, 20))
        
        # 刷新pygame顯示層
        pygame.display.update()
        
        # 判斷是否死亡
        if snakePosition[0] > 600 or snakePosition[0] < 0:
            gameOver(playSurface, score)
        if snakePosition[1] > 460 or snakePosition[1] < 0:
            gameOver(playSurface, score)
        for seg in snakeSegments[1:]:
            if snakePosition == seg:    # 吃到自己身體
                gameOver(playSurface, score)
        
        # 控制遊戲速度
        fpsClock.tick(5)


if __name__ == "__main__":
    main()
