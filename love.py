import pygame
import sys

# تهيئة Pygame
pygame.init()

# إعدادات الشاشة
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dot Matrix Text")

# الألوان
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# تحميل الخط
pygame.font.init()
font = pygame.font.Font(None, 100)  # يمكنك استبداله بخط أكثر جمالية

# النصوص
text_1 = "I LOVE YOU"
text_2 = "MOHAMED KAREM"
current_text = text_1  # النص الحالي

def render_dotted_text(text, color, position):
    """ ترسم النص على شكل نقاط """
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    for x in range(text_rect.left, text_rect.right, 10):
        for y in range(text_rect.top, text_rect.bottom, 10):
            if text_surface.get_at((x - text_rect.left, y - text_rect.top))[3] > 0:  # يتحقق من وجود لون في البكسل
                pygame.draw.circle(screen, color, (x, y), 2)

# حلقة التشغيل
running = True
while running:
    screen.fill(BLACK)  # خلفية سوداء
    render_dotted_text(current_text, RED, (WIDTH // 2, HEIGHT // 2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # عند النقر، يتغير النص
            current_text = text_2 if current_text == text_1 else text_1

    pygame.display.flip()

pygame.quit()
sys.exit()
