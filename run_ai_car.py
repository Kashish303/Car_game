import pygame
import numpy as np
import cv2
from tensorflow.keras.models import load_model
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

model = load_model("model.h5", compile=False)

x, y = 400, 500
speed = 5
obstacles = []

clock = pygame.time.Clock()
running = True

last_move = 0   # 🔥 smoothing memory

while running:
    clock.tick(25)

    screen.fill((50,50,50))

    # road
    pygame.draw.rect(screen, (30,30,30), (250, 0, 300, HEIGHT))

    # lane line
    for i in range(0, HEIGHT, 40):
        pygame.draw.line(screen, (255,255,255), (400, i), (400, i+20), 5)

    # spawn obstacles
    if len(obstacles) < 5 and random.randint(1, 40) == 1:
        obstacles.append(pygame.Rect(random.randint(260,480), 0, 40, 40))

    # move obstacles
    for obs in obstacles[:]:
        obs.y += 5

        if obs.y > HEIGHT:
            obstacles.remove(obs)

        pygame.draw.rect(screen, (255,0,0), obs)

    # 🚗 DRAW CAR
    pygame.draw.rect(screen, (0,255,0), (x,y,50,100))

    # 🔥 LOOK-AHEAD INPUT (better vision)
    img = pygame.surfarray.array3d(screen)[200:600, :, :]
    img = cv2.resize(img, (200,66))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)[0][0]

    # 🔥 SAFETY OVERRIDE (emergency dodge)
    danger = False

    for obs in obstacles:
        if 350 < obs.y < 550 and abs(obs.x - x) < 80:
            danger = True

            if obs.x < x:
                x += speed * 2
                last_move = 1
            else:
                x -= speed * 2
                last_move = -1

            break

    # 🤖 AI CONTROL (only if safe)
    if not danger:

        if prediction < -0.2:
            move = -1
        elif prediction > 0.2:
            move = 1
        else:
            move = 0

        # 🔥 smoothing
        if move == 0:
            move = last_move

        x += move * speed
        last_move = move

    # boundary
    x = max(260, min(x, 490))

    # collision
    car_rect = pygame.Rect(x,y,50,100)
    for obs in obstacles:
        if car_rect.colliderect(obs):
            print("AI CRASH 💥")
            x = 400
            obstacles.clear()
            break

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()