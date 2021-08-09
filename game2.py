import pygame

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)

X = 400
Y = 400

display_surface = pygame.display.set_mode((X, Y))
font = pygame.font.Font('freesansbold.ttf', 32)

def show_text(t):
    text = font.render(t, True, white, black)
    text_rect = text.get_rect()
    text_rect.center = (X // 2, Y // 2)
    display_surface.blit(text, text_rect)

txts = ["a", "b", "opcoes 1, 2"]
txts_1 = ["resultado 1", "mee", "oww"]
txts_2 = ["resultado 2", "nya", "nyan"]

class Dialog:
    def __init__(sentences, next_key, back_key):
        self.sentences = sentences
        self.current = 0
        self.first = 0
        self.last = len(sentences) - 1

    def next_sentence():
        if self.current + 1 <= self.last:
            self.current += 1

    def previous_sentence():
        if self.current - 1 >= self.first:
            self.current -= 1

    def show_current():
        show_text(self.sentences[self.current])

    def handle_key(key):
        if key == self.next_key:
            next_sentence()
            show_current()
        if key == self.back_key:
            previous_sentence()
            show_current()

current = 0
show_text(txts[current])
while True:
    display_surface.fill(black)
    if current >= 0 and current <= 2:
        show_text(txts[current])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current -= 1
                print("left", current)
            if event.key == pygame.K_RIGHT:
                current += 1
                print("right", current)
            if event.key == pygame.K_UP:
                current += 1
                print("up", current)
            if event.key == pygame.K_DOWN:
                current -= 1
                print("down", current)
        pygame.display.update()
