import pygame
import os
import sys


def load_image(name, colorkey=None):
    """Функция загрузки изображения"""
    fullname = os.path.join("origin","media", 'img', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image
