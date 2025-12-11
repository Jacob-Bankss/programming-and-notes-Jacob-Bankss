# AI Assistance Declaration:
# This program was created with assistance from generative AI (ChatGPT).
# I have reviewed and tested all content and take full responsibility for the final work.

import csv
import sys
import os


# -------------------------------------------
# Player class to store individual player data
# -------------------------------------------
class Player:
    def __init__(self, firstname, surname, club, appearances, goals, assists):
        # Store all player details, converting stats to integers
        self.firstname = firstname
        self.surname = surname
        self.club = club
        self.appearances = int(appearances)
        self.goals = int(goals)
        self.assists = int(assists)

    def full_name(self):
        return f"{self.firstname} {self.surname}"

    def total_contributions(self):
        return self.goals + self.assists

    def efficiency(self):
        # Avoid division by zero if player has no appearances
        if self.appearances == 0:
            return 0.0
        return self.goals / self.appearances


# ------------------------------------------------
# the function that reads CSV and returns a list of players
# ------------------------------------------------
def load_players(filename):
    players = []

    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist.")
        sys.exit(1)

    try:
        with open(filename, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                try:
                    # Create a Player object for each valid CSV row
                    p = Player(
                        row["Firstname"],
                        row["Surname"],
                        row["Club"],
                        row["Appearances"],
                        row["Goals"],
                        row["Assists"],
                    )
                    players.append(p)

                except Exception as e:
                    # Skip rows with missing or invalid data
                    print(f"Warning: Skipping invalid row: {row} ({e})")

    except OSError as e:
        print(f"Error reading file '{filename}': {e}")
        sys.exit(1)

    return players


# -----------------------------------------------------
# All the Functions that generate the rankings and summary statistics
# -----------------------------------------------------
def rank_players(players, sort_key):
    """Return a list of players sorted by the chosen metric."""
    match sort_key:
        case "goals":
            return sorted(players, key=lambda p: p.goals, reverse=True)
        case "assists":
            return sorted(players, key=lambda p: p.assists, reverse=True)
        case "contributions":
            return sorted(players, key=lambda p: p.total_contributions(), reverse=True)
        case "efficiency":
            return sorted(players, key=lambda p: p.efficiency(), reverse=True)
        case _:
            print(f"Unknown sort type '{sort_key}'. Defaulting to goals.")
            return sorted(players, key=lambda p: p.goals, reverse=True)


def apply_club_filter(players, club_name):
    """Return only players belonging to the specified club."""
    if club_name is None:
        return players
    return [p for p in players if p.club.lower() == club_name.lower()]


def print_ranking(players, sort_type, limit, outfile=None):
    """Generate and print the ranking table."""
    ranking = rank_players(players, sort_type)
    header = f"=== Ranking by {sort_type.capitalize()} ===\n"

    output = header
    for p in ranking[:limit]:
        output += (
            f"{p.full_name():25}  "
            f"{p.club:15}   "
            f"Apps: {p.appearances:2}   "
            f"Goals: {p.goals:2}  Assists: {p.assists:2}  "
            f"Contributions: {p.total_contributions():2}  "
            f"Efficiency: {p.efficiency():.2f}\n"
        )

    print(output)

    if outfile:
        outfile.write(output + "\n")


# ---------------------------
# Club summary
# ---------------------------
def print_club_summary(players, outfile=None):
    """Print total club-level stats and identify each club's top contributor."""
    output = "\n=== Club Summary ===\n"

    clubs = {}
    for p in players:
        if p.club not in clubs:
            clubs[p.club] = {"goals": 0, "assists": 0, "players": []}

        clubs[p.club]["goals"] += p.goals
        clubs[p.club]["assists"] += p.assists
        clubs[p.club]["players"].append(p)

    for club, stats in clubs.items():
        top_player = max(stats["players"], key=lambda p: p.total_contributions())

        block = (
            f"\n{club}\n"
            f" Total Goals:   {stats['goals']}\n"
            f" Total Assists: {stats['assists']}\n"
            f" Best Player: {top_player.full_name()} "
            f"({top_player.total_contributions()} goal contributions)\n"
        )

        output += block

    print(output)

    if outfile:
        outfile.write(output + "\n")


# -----------------------
#Argumentparsing helper
# -----------------------
def parse_arguments():
    """Interpret command-line arguments and return configuration values."""
    args = sys.argv[1:]

    if len(args) == 0:
        print(
            "Usage: python stats_analyser.py players.csv "
            "[--limit N] [--club NAME] [--sort TYPE] [--export FILE]"
        )
        sys.exit(1)

    filename = args[0]
    limit = 10
    club = None
    sort_type = "goals"
    export_file = None

    i = 1
    while i < len(args):
        match args[i]:
            case "--limit":
                limit = int(args[i + 1])
                i += 2
            case "--club":
                club = args[i + 1]
                i += 2
            case "--sort":
                sort_type = args[i + 1]
                i += 2
            case "--export":
                export_file = args[i + 1]
                i += 2
            case _:
                print(f"Unknown argument: {args[i]}")
                sys.exit(1)

    return filename, limit, club, sort_type, export_file
# --------------
# Main code entrypoint area
# --------------
def main():
    filename, limit, club, sort_type, export_file = parse_arguments()
    players = load_players(filename)

    # Apply an optional club filter
    filtered_players = apply_club_filter(players, club)

    if not filtered_players:
        print("No players match your filter.")
        sys.exit(0)

    outfile = open(export_file, "w", encoding="utf-8") if export_file else None

    # Produces the ranking and a club summary
    print_ranking(filtered_players, sort_type, limit, outfile)
    print_club_summary(filtered_players, outfile)

    if outfile:
        outfile.close()


if __name__ == "__main__":
    main()