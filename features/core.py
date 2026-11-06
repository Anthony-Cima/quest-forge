"""Core QuestForge logic: the world, moving between rooms, and small helpers."""


def get_rooms(data):
    return data["rooms"]


def start_room(data):
    return data["start"]


def describe(room):
    return room["description"]


def exits_for(room):
    return list(room["exits"].keys())


def count_exits(room):
    return len(room["exits"])


def room_count(data):
    return len(data["rooms"])


def move(data, current_key, direction):
    return data["rooms"][current_key]["exits"].get(direction.upper(), current_key)


def exits_by_room(data):
    counts = {}
    for key, room in data["rooms"].items():
        counts[key] = len(room["exits"])
    return counts


def first_exit(room):
    return list(room["exits"].keys())[0]
