# Рисует узор, используя повтояющиеся круги
import turtle

NUM_CIRCLE = 36  # количество рисуемых кругов
RADIUS = 100  # радиус каждого круга
ANGLE = 10  # угол поворота
ANIMATION_SPEED = 0  # скорость анимации

turtle.speed(ANIMATION_SPEED)
# нарисовать NUM_CIRCLE кругов, наклоняя черепаху на ANGLE градусов,
# после того, как каждый круг был нарисован
for x in range(NUM_CIRCLE):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)
