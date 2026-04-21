import pygame
import numpy as np
import os
import random
import cv2

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

x, y = 400, 500
speed = 6

data = []
obstacles = []

os.makedirs("data", exist_ok=True)

running = True
clock = pygame.time.Clock()

frame_count = 0   # 🔥 for optimization

while running:
    clock.tick(25)

    screen.fill((50,50,50))
    #road ban rha h
    pygame.draw.rect(screen, (30,30,30), (250, 0, 300, HEIGHT))

    #road ki ehite lines
    for i in range(0, HEIGHT, 40):
        pygame.draw.line(screen, (255,255,255), (400, i), (400, i+20), 5)

    # spawn obstacles (limit added)
    if len(obstacles) < 5 and random.randint(1, 35) == 1:
        obstacles.append(pygame.Rect(random.randint(260,480), 0, 40, 40))

    # move + draw obstacles
    for obs in obstacles[:]:
        obs.y += 5
    #overflow na ho data toh objects remove 
        if obs.y > HEIGHT:
            obstacles.remove(obs)
        #draw obstacles
        pygame.draw.rect(screen, (255,0,0), obs)

    # 🔥 SMART AUTO CONTROL (FIXED INDENTATION)
    label = 0

    for obs in obstacles:
        if 100 < obs.y < 450:

            if abs(obs.x - x) < 100:

                left_safe = True
                right_safe = True

                for other in obstacles:
                    if 100 < other.y < 450:

                        if abs((x - 60) - other.x) < 50:
                            left_safe = False

                        if abs((x + 60) - other.x) < 50:
                            right_safe = False

                if left_safe and x > 270:
                    x -= speed
                    label = -1

                elif right_safe and x < 480:
                    x += speed
                    label = 1

                else:
                    x += random.choice([-speed, speed])

                break

    # balanced movement
    if label == 0:
        direction = random.choice([-1, 1])

        if direction == -1:
            if x <= 270:
                x += speed
                label = 1
            else:
                x -= speed
                label = -1
        else:
            if x >= 480:
                x -= speed
                label = -1
            else:
                x += speed
                label = 1

    # boundary
    x = max(260, min(x, 490))

    # draw car
    pygame.draw.rect(screen, (0,255,0), (x,y,50,100))

    # optimized data capture
    frame_count += 1
    if frame_count % 5 == 0:
        img = pygame.surfarray.array3d(screen)
        img = cv2.resize(img, (200,66))
        data.append([img, label])

    # collision
    car_rect = pygame.Rect(x, y, 50, 100)
    for obs in obstacles:
        if car_rect.colliderect(obs):
            print("CRASH 💥")
            x = 400
            obstacles.clear()
            break

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()

# save data
X = np.array([i[0] for i in data])
y = np.array([i[1] for i in data])

np.save("data/X.npy", X)
np.save("data/y.npy", y)

print("Data saved!")