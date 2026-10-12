# The Legend of the Dot Escape 🏰

A keyboard-controlled Python escape game developed in **2022** by **Emilion Berger and Johan Marrakchi** as a collaborative project for the open online course **Apprendre à coder avec Python** on FUN-MOOC. The work was also submitted through ULB's virtual learning environment for INFO-H100.

> **Attribution:** This repository preserves the names of both student authors. The maze, door-question and object datasets, as well as the `CONFIGS.py` configuration, were supplied as part of the MOOC. Their reuse and redistribution permissions should be confirmed before making this repository public.

## Features

- Grid-based castle rendered with Python's standard-library `turtle` graphics
- Keyboard navigation using the four arrow keys
- Walls and collision handling
- Collectible items and an on-screen inventory
- Locked doors that open after correct quiz answers
- A win condition at the exit tile

The project implements the features of the **fourth (complete) level** described in the MOOC assignment.

## Requirements

- Python 3 with Tkinter / Turtle support
- A graphical desktop environment (Windows, macOS or Linux)
- No third-party Python packages

## Run

Open a terminal **in the directory containing the game files** and execute:

```bash
# Windows (Python launcher)
py BERGER_MARRAKCHI.py

# macOS / Linux (or Windows where python is configured)
python3 BERGER_MARRAKCHI.py
```

Click inside the Turtle window if needed to focus it, then use the arrow keys. Answer door questions in the dialog boxes, collect items, and reach the yellow exit.

## Project structure

| File | Purpose | Origin |
|---|---|---|
| `BERGER_MARRAKCHI.py` | Original student game implementation | Emilion Berger and Johan Marrakchi |
| `CONFIGS.py` | Colors, dimensions and input filenames | Course-provided |
| `plan_chateau.txt` | Castle grid (27 rows × 19 columns) | Course-provided |
| `dico_portes.txt` | Questions and answers for 10 doors | Course-provided |
| `dico_objets.txt` | Descriptions of 6 collectible objects | Course-provided |

The original game logic is preserved; only the introductory project attribution was clarified for this portfolio copy.

## Testing

- The game started in a virtual graphical environment without an immediate error.
- A simulated traversal collected all six items and reached the exit after 306 moves.
- The original author has also reported that the game launches and appears to work on Windows.
- Automated tests mock Turtle input and do not replace a full manual visual QA session.

See [`TESTING.md`](TESTING.md) for details.

## Screenshot

Add a screenshot of the running Turtle game to `screenshots/gameplay.png`, then uncomment the following line:

<!-- ![Castle gameplay](screenshots/gameplay.png) -->

## Historical context and limitations

This is a **student MOOC project**, not a CERN project or an independent ULB research internship. The separate 2023 ULB *Engin-Hearing* cochlear implant group project is not part of this repository.

The historical `Projet_valeurs.py` script is **not included** here: it is not required for this game, and its missing `valeurs.txt` input prevents reproduction. No replacement data were fabricated.

## Licensing

No open-source license has been assigned to the co-authored code or the MOOC-provided assets. **Do not assume public redistribution or reuse rights** without checking the relevant permissions and agreement of the co-author. This repository is prepared for review before publication.
