def solution(points, routes):
    answer = 0
    collision = 0
    routes = [ [ p - 1 for p in point ] for point in routes ]
    robots = [ points[r[0]] for r in routes ]
    routes = [ route[1:] for route in routes ]
    
    while routes:
        unique = set([(y, x) for y, x in robots])
        for y, x in unique:
            if robots.count([y, x]) > 1:
                collision += 1
        for i, (y, x) in enumerate(robots):
            ty, tx = points[routes[i][0]]
            dy, dx = 0, 0
            if ty == y and tx == x:
                routes[i] = routes[i][1:]
                if not routes[i]:
                    robots[i] = [0, 0]
                    continue
                ty, tx = points[routes[i][0]]
            if y < ty:
                dy = 1
            elif y > ty:
                dy = -1
            elif x < tx:
                dx = 1
            elif x > tx:
                dx = -1
                
            robots[i] = [y + dy, x + dx]
        robots = [ robot for robot in robots if robot != [0, 0] ]
        routes = [ route for route in routes if route ]
        
        
    return collision