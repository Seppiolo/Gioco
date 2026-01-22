import arcade

# Costanti per le dimensioni
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TITOLO = "Tower Defense - Sukuna"
PLAYER_SCALE = 0.5

class Tower_Defense(arcade.Window):
    def __init__(self, larghezza, altezza, titolo):
        super().__init__(larghezza, altezza, titolo)
        
        # 1. Inizializziamo la SpriteList che conterrà tutte le torri
        self.lista_torri = arcade.SpriteList()
        
        # 2. Carichiamo la texture dello sfondo
        self.sfondo = arcade.load_texture("C:/Users/sebastiano.scarpa/Desktop/Gioco(Tower-Defense)/Mappa.png")
        
        # Salviamo il percorso dell'immagine di Sukuna per usarlo dopo
        self.path_sukuna = "C:/Users/sebastiano.scarpa/Desktop/Gioco(Tower-Defense)/Sukuna.png.png"

    def on_draw(self):
        # Pulisce lo schermo
        self.clear()
        
        # Disegna lo sfondo (usa draw_lrwh per coprire tutta l'area)
        arcade.draw_texture_rect(
            self.sfondo,
            arcade.LBWH(0, 0, 600, 600)
        )
        
        # 3. Disegna tutte le torri aggiunte alla lista
        self.lista_torri.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        # Controlliamo se è stato premuto il tasto sinistro
        if button == arcade.MOUSE_BUTTON_LEFT:
            
            # 4. Creiamo un nuovo Sprite di Sukuna ad ogni click
            # Regola 'scale' se lo sprite dovesse apparire troppo grande o piccolo
            nuova_torre = arcade.Sprite(self.path_sukuna, scale=0.2)
            
            # Impostiamo la posizione dello sprite dove abbiamo cliccato
            nuova_torre.center_x = x
            nuova_torre.center_y = y
            
            # 5. Aggiungiamo lo sprite alla lista così on_draw può disegnarlo
            self.lista_torri.append(nuova_torre)
            
            print(f"Torre posizionata in coordinate: {x}, {y}")

def main():
    # Avviamo il gioco
    gioco = Tower_Defense(SCREEN_WIDTH, SCREEN_HEIGHT, TITOLO)
    arcade.run()

if __name__ == "__main__":
    main()
