import tkinter as tk
import random

# =====================
# Datos del juego: personajes, locaciones, armas e historias finales
# =====================
personajes = [
    ("Freddy Fazbear", "Animatrónico cantante"),
    ("Bonnie", "Guitarrista animatrónico"),
    ("Chica", "Cocinera de la pizzería"),
    ("Foxy", "Pirata del escenario"),
    ("Security Mike", "Guardia nocturno")
]

locaciones = ["Escenario Principal", "Cocina", "Cuarto de Seguridad", "Pasillo Oeste", "Sala de Mantenimiento"]
armas = ["Micrófono roto", "Guitarra eléctrica", "Bandeja metálica", "Garra oxidada", "Linterna descargada"]

# Historias finales correspondientes a cada personaje culpable
historias = {
    "Freddy Fazbear": "Freddy se descontroló cuando las luces parpadearon. El eco metálico de su micrófono roto marcó el fin de la calma...",
    "Bonnie": "Bonnie desapareció del escenario, y minutos después, un chillido y una cuerda de guitarra rota revelaron la tragedia...",
    "Chica": "El olor a aceite quemado y pizza invadió el aire. Chica estaba allí, sosteniendo una bandeja cubierta de algo más que salsa...",
    "Foxy": "Desde el corredor oscuro, un grito y el sonido de metal raspando el suelo. Foxy no perdonó esa noche...",
    "Security Mike": "El guardia no resistió más. Entre la locura y el miedo, usó la linterna como su única defensa... que terminó siendo mortal."
}

# =====================
# Función para generar un nuevo caso aleatorio
# =====================
def nuevo_caso():
    return {
        "culpable": random.choice(personajes),  # Selecciona un culpable aleatorio
        "lugar": random.choice(locaciones),     # Selecciona un lugar aleatorio
        "arma": random.choice(armas)           # Selecciona un arma aleatoria
    }

# =====================
# Clase principal del juego con GUI
# =====================
class ClueFNAF:
    def __init__(self, root):
        self.root = root
        self.root.title("🎃 Clue: FNAF Mystery Edition 🎃")
        self.root.geometry("750x650")
        self.root.config(bg="#111")

        # Generar el caso inicial
        self.caso = nuevo_caso()
        self.intentos = 0  # Contador de intentos de adivinanza
        self.pistas = 0     # Contador de pistas pedidas

        # Título principal del juego
        titulo = tk.Label(root, text="🕯️ Misterio en Freddy Fazbear’s Pizza 🕯️", font=("Arial", 18, "bold"), bg="#111", fg="#ffcc00")
        titulo.pack(pady=15)

        # Texto de la narrativa inicial (prólogo aleatorio)
        self.texto_historia = tk.Label(root, text=self.generar_prologo(), wraplength=700, justify="center", bg="#111", fg="white", font=("Arial", 11))
        self.texto_historia.pack(pady=10)

        # Frame para selección de sospechoso, lugar y arma
        frame_seleccion = tk.Frame(root, bg="#111")
        frame_seleccion.pack(pady=10)

        # Selección de personaje sospechoso
        tk.Label(frame_seleccion, text="Sospechoso:", bg="#111", fg="#ffcc00", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=5)
        self.sospechoso_var = tk.StringVar(value=personajes[0][0])
        tk.OptionMenu(frame_seleccion, self.sospechoso_var, *[p[0] for p in personajes]).grid(row=0, column=1)

        # Selección de locación
        tk.Label(frame_seleccion, text="Lugar:", bg="#111", fg="#ffcc00", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=5)
        self.lugar_var = tk.StringVar(value=locaciones[0])
        tk.OptionMenu(frame_seleccion, self.lugar_var, *locaciones).grid(row=1, column=1)

        # Selección de arma
        tk.Label(frame_seleccion, text="Arma:", bg="#111", fg="#ffcc00", font=("Arial", 12, "bold")).grid(row=2, column=0, padx=5)
        self.arma_var = tk.StringVar(value=armas[0])
        tk.OptionMenu(frame_seleccion, self.arma_var, *armas).grid(row=2, column=1)

        # Frame para botones de acción
        frame_botones = tk.Frame(root, bg="#111")
        frame_botones.pack(pady=15)

        # Botón para adivinar
        tk.Button(frame_botones, text="🎯 Adivinar", command=self.adivinar, bg="#ff4444", fg="white", font=("Arial", 12, "bold"), width=12).grid(row=0, column=0, padx=5)
        # Botón para pedir pista
        tk.Button(frame_botones, text="🔍 Pedir pista", command=self.dar_pista, bg="#ffaa00", fg="black", font=("Arial", 12, "bold"), width=12).grid(row=0, column=1, padx=5)
        # Botón para reiniciar el juego
        tk.Button(frame_botones, text="🔁 Reiniciar", command=self.reiniciar, bg="#33aa33", fg="white", font=("Arial", 12, "bold"), width=12).grid(row=0, column=2, padx=5)
        # Botón para salir del juego
        tk.Button(frame_botones, text="🚪 Salir", command=root.destroy, bg="#555", fg="white", font=("Arial", 12, "bold"), width=12).grid(row=0, column=3, padx=5)

        # Label para mostrar pistas o resultado final
        self.resultado_label = tk.Label(root, text="", bg="#111", fg="#ccc", font=("Arial", 12), wraplength=700, justify="center")
        self.resultado_label.pack(pady=15)

    # Generar una narrativa introductoria aleatoria
    def generar_prologo(self):
        introducciones = [
            "La noche cayó sobre la pizzería. Los animatrónicos estaban inquietos, y algo oscuro se movía entre los pasillos...",
            "Luces parpadeantes, cámaras sin señal y un silencio inquietante. Algo terrible ocurrió en Freddy Fazbear’s Pizza...",
            "El reloj marcó la medianoche. Los monitores mostraron sombras que no deberían estar allí...",
            "Un olor metálico y una risa distorsionada llenaron el aire. Solo tú puedes descubrir qué pasó esta vez...",
            "La pizzería cerró hace años, pero esta noche, todo volvió a la vida... y a la muerte."
        ]
        return random.choice(introducciones)

    # Dar una pista al jugador (máx. 3 pistas)
    def dar_pista(self):
        if self.pistas >= 3:
            self.resultado_label.config(text="Ya no hay más pistas disponibles.")
            return

        pistas_texto = [
            f"Alguien vio una figura parecida a {self.caso['culpable'][0]} cerca del {random.choice(locaciones)}...",
            f"Se escuchó un ruido proveniente del {self.caso['lugar']}. Algo metálico chocó contra el suelo...",
            f"Una sombra sostenía lo que parecía ser un(a) {self.caso['arma']}. La escena se vuelve más clara..."
        ]
        pista = pistas_texto[self.pistas]
        self.resultado_label.config(text=pista)
        self.pistas += 1

    # Verificar si la adivinanza es correcta
    def adivinar(self):
        self.intentos += 1
        sospechoso = self.sospechoso_var.get()
        lugar = self.lugar_var.get()
        arma = self.arma_var.get()

        if (sospechoso == self.caso["culpable"][0] and lugar == self.caso["lugar"] and arma == self.caso["arma"]):
            historia = historias[self.caso["culpable"][0]]
            self.resultado_label.config(fg="#00ff88", text=f"✅ ¡Correcto! Has resuelto el caso tras {self.intentos} intentos.\n\n{historia}")
        else:
            self.resultado_label.config(fg="#ff6666", text=f"❌ No es correcto. Intenta de nuevo...")

    # Reiniciar el juego generando un nuevo caso y reiniciando contadores
    def reiniciar(self):
        self.caso = nuevo_caso()
        self.intentos = 0
        self.pistas = 0
        self.resultado_label.config(text="")
        self.texto_historia.config(text=self.generar_prologo())


# =====================
# Ejecutar la aplicación
# =====================
if __name__ == "__main__":
    root = tk.Tk()
    app = ClueFNAF(root)
    root.mainloop()