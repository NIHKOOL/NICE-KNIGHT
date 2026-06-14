# NICE KNIGHT

> *"NICE KNIGHT FIGHT MIGHT LIKE MIKE"*

A small 2D action game built with **Python** and **Pygame**. Play as a knight who can walk, jump, and **blink** (a short-cooldown dash) to slay goblins for points — all before the timer runs out and an angry dragon charges across the screen.

---

## 🎮 Gameplay

- **Hunt goblins** — touch a goblin to slay it and earn **+1 score**. A new goblin instantly respawns at a random position.
- **Blink** — teleport a short distance left or right with a cooldown. Great for chasing goblins or dodging.
- **Beat the clock** — you start with **45 seconds**. When the timer hits zero, a **dragon** awakens and charges in from the right. If it reaches you, the game is over.
- Rack up as high a score as you can before the dragon catches you!

## ⌨️ Controls

| Key            | Action              |
| -------------- | ------------------- |
| `A`            | Move left           |
| `D`            | Move right          |
| `W` / `Space`  | Jump                |
| `O`            | Blink left          |
| `P`            | Blink right         |

> Blink has a **3.5 second cooldown**, shown on screen. A sound plays when it's ready again.

## 📋 Requirements

- [Python 3](https://www.python.org/downloads/) (3.8 or newer recommended)
- [Pygame](https://www.pygame.org/)

Install Pygame with:

```bash
pip install pygame
```

## 📁 Project Structure

The game expects its assets inside `img/` and `music/` folders. The files are currently in the repository root, so **move them into the folders below before running**:

```
NICE-KNIGHT/
├── GAME.py
├── img/
│   ├── bg3.jpg        # background
│   ├── pngegg.png     # the knight (player)
│   ├── Gob.png        # goblin
│   └── Dragon.png     # dragon
└── music/
    ├── Now-We-Ride(chosic.com).mp3              # background music
    ├── shining-anime-sound-effect-240582.mp3    # blink sound
    ├── key-get-39925.mp3                         # cooldown-ready sound
    ├── male-death-sound-128357.mp3               # goblin death sound
    └── dragon-growl-37570.mp3                    # dragon growl
```

On Windows (PowerShell) you can set this up quickly:

```powershell
mkdir img, music
move bg3.jpg, pngegg.png, Gob.png, Dragon.png img
move *.mp3 music
```

## ▶️ How to Run

```bash
python GAME.py
```

When the game ends, your final score is printed in the terminal — alongside a little ASCII sword. ⚔️

## 📝 Notes

- The window is **1200 × 675** and runs at **120 FPS**.
- Asset paths are relative, so run `python GAME.py` from the project root.

---

*Made for fun. Slay goblins, dodge the dragon, get a nice score!*
