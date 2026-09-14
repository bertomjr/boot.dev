# Asteroid Game

<img width="1340" height="815" alt="Screenshot From 2026-09-14 00-58-48" src="https://github.com/user-attachments/assets/5034a2d1-644b-492e-9da4-16f0d9e501a9" />

A small Asteroids-style arcade game built with Python and Pygame while following [Boot.dev's Build Asteroids guided project](https://www.boot.dev/courses/build-asteroids-python).

Pilot a spaceship, shoot incoming asteroids, and avoid collisions. This project helped me practice object-oriented programming, game loops, and collision detection.

[Back to my Boot.dev projects](../README.md)

## Gameplay

- Rotate the ship and move forward or backward.
- Shoot asteroids that spawn at random positions along the screen's edges.
- Break larger asteroids into two smaller, faster pieces; destroy the smallest asteroids completely.
- Avoid contact with asteroids: a collision ends the game.

The game uses simple white outlines on a black background in a 1280 × 720 window.

## Built with

- **Python 3.13** — the version selected for this project.
- **Pygame 2.6.1** — rendering, keyboard input, vectors, timing, and sprite groups.
- **uv** — Python environment and dependency management.

## Run locally

You will need Git, [uv](https://docs.astral.sh/uv/getting-started/installation/), and a desktop environment that can display a game window.

Clone the collection and open the game folder:

```bash
git clone https://github.com/bertomjr/boot.dev.git
cd "boot.dev/Asteroid Game"
```

Start the game from that folder:

```bash
uv run main.py
```

uv prepares the project's environment and installs the locked dependencies before running the game. It can download Python 3.13 if a suitable installation is unavailable. See the [uv project guide](https://docs.astral.sh/uv/guides/projects/) for details.

If you already cloned the repository, open its `Asteroid Game` folder and run the same command.

## Controls

| Input | Action |
| --- | --- |
| **W** | Move forward in the direction the ship faces |
| **S** | Move backward |
| **A** | Rotate left |
| **D** | Rotate right |
| **Space** | Shoot |
| **Close the window** | Quit |

When an asteroid hits the ship, the terminal prints `Game over!` and the program exits. Run `uv run main.py` again to play another round.

## Current limitations

- **Shooting cooldown:** holding Space after firing prevents the cooldown from counting down. Release Space briefly between shots; continuous fire needs a fix.
- **Screen boundaries:** the ship can move offscreen and does not wrap around to the opposite edge.
- **Game flow:** this version ends on the first collision and has no score counter or restart menu.

## What I practiced

- Sharing position, velocity, and collision logic through a `CircleShape` base class.
- Separating player movement, projectiles, and asteroid behavior into classes.
- Using Pygame sprite groups to update, draw, and remove game objects.
- Scaling movement by elapsed frame time (`dt`).
- Using vectors for movement and rotation, and distances between centers for circular collision checks.
- Handling collisions to remove shots, split asteroids, and end a round.

## Project structure

| File | Purpose |
| --- | --- |
| [`main.py`](./main.py) | Initializes the game and handles the main loop, rendering, and collision responses |
| [`player.py`](./player.py) | Ship drawing, movement, rotation, and shooting |
| [`asteroid.py`](./asteroid.py) | Asteroid movement and splitting |
| [`asteroidfield.py`](./asteroidfield.py) | Spawns asteroids along the screen's edges |
| [`shot.py`](./shot.py) | Projectile drawing and movement |
| [`circleshape.py`](./circleshape.py) | Shared game-object properties and collision detection |
| [`constants.py`](./constants.py) | Window dimensions, object sizes, speeds, and timing values |
| [`logger.py`](./logger.py) | Records game state and gameplay events |
| [`pyproject.toml`](./pyproject.toml) | Python requirement and project dependencies |
| [`uv.lock`](./uv.lock) | Locked dependency versions |

## Credits

Built while following [Boot.dev's Build Asteroids course](https://www.boot.dev/courses/build-asteroids-python). Boot.dev provides the project brief, instruction, and starter material; this repository contains my work on the guided project.

Project by [Roberto Marcillo Jr.](https://github.com/bertomjr)
