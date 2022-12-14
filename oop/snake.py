from typing import List, Union
import random


class Point:
    def __init__(self, x: int, y: int):
        """
        給定 x 和 y 然後產生一個點
        """
        self.x = x
        self.y = y


class Region:
    def __init__(self, p1:Point, p2:Point):
        """
        給兩個點，定義一個矩形範圍
        """
        self.p1 = p1
        self.p2 = p2

    def rnd_point(self, except_points: List[Point] = []) -> Point:
        """
        產生範圍內的隨機一個「點」
        除了except_points(list of Point)之外
        """
        return Point( 
            random.randrange(self.p1.x, self.p2.x), 
            random.randrange(self.p1.y, self.p2.y) 
        )


class Snake:
    def __init__(self, region: Region):
        """
        傳入一個蛇活動的「範圍」及蛇頭的「點」\n
        建立一隻貪食蛇
        """
        self.region = region
        self.head = Point(
            (region.p1.x + region.p2.x) // 2,
            (region.p1.y + region.p2.y) // 2                
        )
        self.body = [self.head]
        self.food = self.new_food()
        self.score = 0

    def new_food(self) -> Point:
        """
        在原先給定的Region內，新增一個食物\n
        而且避免新增的食物出現在蛇的身體上
        """
        self.food = self.region.rnd_point(self.body)
        return self.food

    def is_eaten(self) -> bool:
        """
        判斷是否有吃到食物
        """
        return self.head == self.food

    def is_die(self) -> bool:
        """
        判斷是否死掉：\n
        1.碰到四周牆壁
        2.吃到自己身體
        """
        # 怎麼死的
        return False
        
    def go(self, dir_: str = 'R') -> None:
        """
        往目前方向(dir=L、R、U、D)走一步
        """
        # self.head.x +=1    # self.head.x -=1
        # self.head.y +=1    # self.head.y -=1
        # if is_eaten(): self.score+=1 加分
        pass
