#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Dade Murphy
# Created Date: Wed April 21 2021
# =============================================================================
"""Hunt the Wumpus"""
# =============================================================================
# Built while reading through chapter 2 of "Hello! Python" by Anthony Briggs
# =============================================================================
# STANDARD FIELDS
# =============================================================================
__author__ = "Dade Murphy"
__email__ = "cr45hmurphy@gmail.com"
__credits__ = ["Anthony Briggs"]
__date__ = "2021/04/21"
__deprecated__ = False
__license__ = "GPLv3"
__maintainer__ = "Dade Murphy"
__status__ = "Production"
__version__ = "1.0.0"


# =============================================================================
# Imports
# =============================================================================
from random import choice
from os import system, name


# =============================================================================
# Required Functions
# =============================================================================

def clear():
    """ Clear screen """
    #for windows
    if name == 'nt':
        _ = system('cls')

    #for mac and linux
    else:
        _ = system('clear')


def setup_caves(cave_numbers):
    """ Create the starting list of caves. """
    caves = []
    for cave in cave_numbers:
        caves.append([])
    return caves

def link_caves():
    """ Make sure all of the caves are connected
    with two-way tunnels """
    while unvisited_caves != []:
        this_cave = choose_cave(visited_caves)
        next_cave = choose_cave(unvisited_caves)
        create_tunnel(this_cave, next_cave)
        visit_cave(next_cave)

def finish_caves():
    """ Link the rest of the caves with 
    one-way tunnels. """
    for cave in cave_numbers:
        while len(caves[cave]) < 3:
            passage_to = choice(cave_numbers)
            while (passage_to in caves[cave]) or (passage_to == cave):
                passage_to = choice(cave_numbers)
            caves[cave].append(passage_to)

def create_tunnel(cave_from, cave_to):
        """ Create a tunnel between cave_from and cave_to"""
        caves[cave_from].append(cave_to)
        caves[cave_to].append(cave_from)

def visit_cave(cave_number):
    """ Mark a cave as visited """
    visited_caves.append(cave_number)
    unvisited_caves.remove(cave_number)

def choose_cave(cave_list):
    """ Pick a cave from a list, provided
    that the cave has less than 3 tunnels. """
    cave_number = choice(cave_list)
    while len(caves[cave_number]) >= 3:
        cave_number = choice(cave_list)
    return cave_number


def print_location(player_location):
    """ Tell the player about where they are """
    print()
    print("You are in the",cave_names[player_location])
    neighbors = caves[player_location]
    for tunnel in range(0,3):
        next_cave = neighbors[tunnel]
        print("  ", tunnel+1, "-", cave_names[next_cave])
    if wumpus_location in neighbors:
        print("You smell a wumpus!")
        print()
    if bat_location in neighbors:
        print("You can hear squeaks and the rustling of wings nearby.")
        print()


def ask_for_cave():
    """ Get the player's next location. """
    player_input = input("Which cave next? ")
    if player_input in ['1','2','3']:
        index = int(player_input) - 1
        neighbors = caves[player_location]
        cave_number = neighbors[index]
        return cave_number
    else:
        print(player_input + "?")
        print("That's not a direction that you can see!")
        return None

def get_action():
    """ Find out what the player wants to do next. """
    print()
    print("What do you want to do next?")
    print(" m) move")
    print(" a) fire an arrow")
    action = input("> ")
    if action == "m" or action == "a":
        return action
    else:
        print()
        print(action + "?")
        print("That's not an action that I know about")
        print()
        return None

def do_movement():
    #clear()
    print()
    print("Moving...")
    print()
    #print_location(player_location)
    new_location = ask_for_cave()
    if new_location is None:
        return player_location
    else:
        return new_location

def do_shooting():
    print()
    print("Firing...")
    print()
    shoot_at = ask_for_cave()
    if shoot_at is None:
        return False

    if shoot_at == wumpus_location:
        clear()
        print("Twang ... Aargh! You shot the wumpus!")
        print("Well done, mighty wumpus hunter!")
        print()
        print("Game Over")
        print()
    else:
        clear()
        print("Twang ... clatter, clatter!")
        print("You wasted an arrow!")
        print("Empty handed, you begin the ")
        print("long trek back to your village...")
        print()
        print("Game Over")
        print()
    return True

# =============================================================================
# Optional Functions
# =============================================================================

def print_caves():
    """ Print out the current cave structure
    for debugging purposes. """
    for number in cave_numbers:
        print(number, ":", caves[number])
    print('----------')


def bat_grab():
    """ Move player to another location """
    print()
    print("A flurry of bats fills the cave! The rush of wind lifts you up and carries you to another location.")
    print()
    player_location = choice(cave_numbers)
    bat_location = choice(cave_numbers)
    while player_location == wumpus_location:
        player_location = choice(cave_numbers)
    while ((bat_location == player_location) or (bat_location == wumpus_location)):
        bat_location = choice(cave_numbers)
    return (player_location, bat_location)

# =============================================================================
# Initialize Game
# =============================================================================

cave_numbers = range(0,20)
unvisited_caves = list(cave_numbers)
visited_caves = []
caves = setup_caves(cave_numbers)

cave_names = [
    "Arched cavern",
    "Twisty passages",
    "Dripping cave",
    "Dusty crawlspace",
    "Underground lake",
    "Black pit",
    "Fallen cave",
    "Shallow pool",
    "Icy underground river",
    "Sandy hollow",
    "Old firepit",
    "Tree root cave",
    "Narrow ledge",
    "Winding steps",
    "Echoing chamber",
    "Musty cave",
    "Gloomy cave",
    "Low ceilinged cave",
    "Wumpus lair",
    "Spooky Chasm",
]

visit_cave(0)
#print_caves()
link_caves()
#print_caves()
finish_caves()
#print_caves()


# Set home location of all entitites
wumpus_location = choice(cave_numbers)
player_location = choice(cave_numbers)
bat_location = choice(cave_numbers)
while player_location == wumpus_location:
    player_location = choice(cave_numbers)
while ((bat_location == player_location) or (bat_location == wumpus_location)):
    bat_location = choice(cave_numbers)

# Welcome message
print("Welcome to Hunt the Wumpus!")
print()
print("You can see", len(cave_numbers), "caves")
print()
print("To play, just type the number")
print("of the cave you wish to enter next.")


# =============================================================================
# Main Loop
# =============================================================================


while 1:
    print_location(player_location)

    action = get_action()
    if action is None:
        continue
    
    if action == "m":
        player_location = do_movement()
        if player_location == wumpus_location:
            clear()
            print("Aargh! You got eaten by wumpus!")
            print()
            print("Game Over")
            print()
            break
        elif player_location == bat_location:
            clear()
            player_location, bat_location = bat_grab()


    if action == "a":
        game_over = do_shooting()
        if game_over:
            break
