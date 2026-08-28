"""Habit Tracker - CLI simple para llevar el registro de habitos diarios."""

import json
import os
from datetime import date

DATA_FILE = "habits.json"


def load_habits():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_habits(habits):
    with open(DATA_FILE, "w") as f:
        json.dump(habits, f, indent=2)


def add_habit(name):
    habits = load_habits()
    habits.setdefault(name, [])
    save_habits(habits)
    print(f"Habito '{name}' agregado.")


def list_habits():
    habits = load_habits()
    if not habits:
        print("No hay habitos registrados.")
        return
    for name, dates in habits.items():
        print(f"- {name}: {len(dates)} dias completados")


def mark_done(name):
    habits = load_habits()
    if name not in habits:
        print(f"El habito '{name}' no existe.")
        return
    today = str(date.today())
    if today not in habits[name]:
        habits[name].append(today)
        save_habits(habits)
    print(f"'{name}' marcado como completado hoy ({today}).")


if __name__ == "__main__":
    print("=== Habit Tracker CLI (version rama conflict-demo) ===")
    list_habits()


def show_stats(name):
    habits = load_habits()
    if name not in habits:
        print(f"El habito '{name}' no existe.")
        return
    total = len(habits[name])
    print(f"Estadisticas de '{name}': {total} dias completados en total.")
# TODO: agregar comando delete_habit (en progreso)
