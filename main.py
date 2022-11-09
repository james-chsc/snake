import pygame

pygame.init()

window_surface  = pygame.display.set_mode( (800, 600) )

pygame.display.set_caption('Hello World:)')
window_surface.fill( (255, 125, 125) )

# 設定字型和大小
font微軟正黑體60pt = pygame.font.Font('./fonts/msjh.ttc', 60)
# 用設定好的字型大小渲染「Hello World!」
text_surface = font微軟正黑體60pt.render('Hello World! 大家好', True, (0, 0, 255), (0,255,0))

window_surface.blit(text_surface, (50, 100))

pygame.display.update()

while True:
    # 迭代整個事件迴圈，若有符合事件則對應處理
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if event.type == pygame.QUIT:
            pygame.quit()