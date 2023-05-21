class Animation:
    def __init__(self, frames, frame_duration):
        self.frames = frames  # Liste des images de l'animation
        self.frame_duration = frame_duration  # Durée de chaque image (en millisecondes)
        self.current_frame = 0  # Index de l'image courante
        self.animation_timer = 0  # Timer pour gérer le passage à l'image suivante


    def update(self, dt):
        self.animation_timer += dt  # Temps écoulé depuis le dernier appel à update()

        # Vérifier si le temps écoulé dépasse la durée de l'image courante
        if self.animation_timer >= self.frame_duration:
            self.animation_timer = 0  # Réinitialiser le timer
            self.current_frame = (self.current_frame + 1) % len(self.frames)  # Passage à l'image suivante

    def get_current_frame(self):
        return self.frames[self.current_frame]
