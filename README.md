# P4_Clue
Practica numero 4 de sistemas expertos
# 🎃 Clue: FNAF Mystery Edition 🎃

**Clue: FNAF Mystery Edition** es un juego de mesa interactivo adaptado al estilo de *Five Nights at Freddy's*, implementado en Python usando **Tkinter**. El objetivo del juego es descubrir al culpable, el lugar y el arma de un misterio generado aleatoriamente, usando pistas y deducción.

---

## 🕹️ Características

- Generación aleatoria de un caso con:
  - **Culpable**: entre los animatrónicos y el guardia.
  - **Locación**: diferentes áreas de Freddy Fazbear's Pizza.
  - **Arma**: objetos que podrían haber causado el incidente.
- Narrativa introductoria aleatoria para cada partida.
- Sistema de pistas (máximo 3 por juego) para ayudar al jugador.
- Registro de intentos de adivinanza.
- Mensaje final con la historia del culpable al resolver el caso.
- Botones para:
  - Adivinar
  - Pedir pista
  - Reiniciar juego
  - Salir del juego

---

## 📜 Personajes

| Personaje       | Descripción                        |
|-----------------|------------------------------------|
| Freddy Fazbear  | Animatrónico cantante              |
| Bonnie          | Guitarrista animatrónico           |
| Chica           | Cocinera de la pizzería            |
| Foxy            | Pirata del escenario               |
| Security Mike   | Guardia nocturno                   |

---

## 🏠 Locaciones

- Escenario Principal
- Cocina
- Cuarto de Seguridad
- Pasillo Oeste
- Sala de Mantenimiento

---

## 🔪 Armas

- Micrófono roto
- Guitarra eléctrica
- Bandeja metálica
- Garra oxidada
- Linterna descargada

---

## ⚙️ Requisitos

- Python 3.x
- Librería Tkinter (generalmente incluida en Python)
- Librería PIL (opcional si deseas agregar imágenes más adelante)

Instalación de PIL:

```bash
pip install pillow
