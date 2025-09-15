n = int(input())
ball = input()
def gather(direction, color):
    strip = eval(f"ball.{direction}strip('{color}')")
    return strip.count(color)
gathers = [gather('l', 'B'), gather('r', 'B'), gather('l', 'R'), gather('r', 'R')]
print(min(gathers))