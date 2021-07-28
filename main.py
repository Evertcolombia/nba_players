#!/usr/bin/python3

"""
    Program to get a serie of NBA Players
    based in their hinches heights
"""

import requests as req
import sys


def get_players():
    """
        send a get request to url and
        based in response get the NBA players that
        matches and print in list format the results

        Return: None
    """
    p_count = 0 # control the players print list
    hinches = "" # will be the argument validated
    values = [] # list of players

    if len(sys.argv) != 2:
        print("Must pass height parameter. Try again")
        exit()

    try:
        hinches = int(sys.argv[1])
    except ValueError:
        print("Error: Must be a number. Try again")
        exit()

    res = req.get('https://mach-eight.uc.r.appspot.com/')
    if res.status_code != 200:
        print("Error {}".format(res.status_code))
        exit()

    hinches = str(hinches)
    if res.text.count(hinches) == 0: # test fastly if matches with a player
        print("No matches found")
        exit()

    try:
        values = res.json()["values"]
    except req.exceptions.JSONDecodeError:
        print("Error: Can't convert response to JSON")
        exit()

    print("> app {}\n".format(hinches))
    for p in values: # loop by all players
        if p["h_in"] == hinches:
            st = "{} {}".format(p["first_name"], p["last_name"])
            if p_count % 2 == 0:
                print("- {:<15}".format(st), end='\t')
            else:
                print(st)

            p_count += 1
            if p_count == res.text.count(hinches):
                if p_count % 2 != 0:
                    print()
                break # ends the loop if gets all the players


if __name__ == "__main__":
    get_players()
