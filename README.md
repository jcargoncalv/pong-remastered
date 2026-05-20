# 🏓 Pong Remastered

A modern implementation of the classic Pong game built with Python and Pygame, designed as a focused exploration of game development fundamentals and clean software architecture.

---

## 🚀 Overview

**Pong Remastered** recreates the classic arcade experience while emphasizing technical clarity and extensibility.
The project serves as a hands-on study of real-time systems and structured game design in Python.

Key areas explored:

* Real-time game loop design
* Object-oriented modeling of game entities
* Collision detection and response
* Basic AI behavior (auto-paddle)
* Frame-rate independent movement

---

## 🎮 Features

* Player vs Player mode
* Optional AI-controlled paddle
* Smooth and consistent ball physics
* Score tracking system
* Configurable gameplay parameters (speed, paddle size, etc.)

---

## 🧠 Technical Highlights

* **Game Loop Architecture**
  Structured update → render cycle with delta time support for consistent gameplay across frame rates

* **Entity Abstraction**
  Core objects (`Ball`, `Paddle`) derive from a reusable `GameObject` base class

* **Collision System**
  Axis-Aligned Bounding Box (AABB) detection with directional response logic

* **Auto Paddle (AI)**
  Position tracking based on ball movement, with extensibility for human-like error modeling

---

## 📁 Project Structure

```
pong-remastered/
│
├── classes/
│   ├── game_object.py
│   ├── paddle.py
│   ├── auto_paddle.py
│   └── ball.py
├── main.py
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pong-remastered.git
cd pong-remastered
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
```

### 3. Install dependencies

```bash
pip install pygame
```

---

## ▶️ Running the Game

```bash
python main.py
```

---

## 🎯 Controls

| Action            | Key |
| ----------------- | --- |
| Left Paddle Up    | W   |
| Left Paddle Down  | S   |
| Right Paddle Up   | ↑   |
| Right Paddle Down | ↓   |

---

## 🔧 Future Improvements

* Add sound effects and background music
* Implement menus (start, pause, game over)
* Enhance AI with prediction and error modeling
* Introduce spin and angle mechanics
* Package as a standalone executable

---

## 📚 Learning Goals

This project is part of a broader effort to deepen understanding of:

* Game development fundamentals
* Python for real-time applications
* Clean and modular code architecture

---

## 📄 License

This project is open-source and licensed under the GPL-3 License.

---

## 👤 Author

**João Carlos de A. R. Gonçalves**
Systems Engineer | Python & Linux | Game Development

* GitHub: https://github.com/jcgoncalv

---
