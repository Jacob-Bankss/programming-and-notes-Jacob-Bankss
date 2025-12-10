import csv
import sys
import os



# Player class to store individual player data

class Player:
    def __init__(self, firstname, surname, club, goals, assists, appearances):
        self.firstname = firstname
        self.surname = surname
        self.club = club
        self.goals = int(goals)
        self.assists = int(assists)
        self.appearances = int(appearances)

    def full_name(self):
        return f"{self.firstname} {self.surname}"

    def total_contributions(self):
        return self.goals + self.assists

    def efficiency(self):
        if self.appearances == 0:
            return 0
        return self.goals / self.appearances



# Read the CSV file and return a list of Player objects

def load_players(filename):
    players = []

    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist.")
        sys.exit(1)

    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                p = Player(
                    row["Firstname"],
                    row["Surname"],
                    row["Club"],
                    row["Goals"],
                    row["Assists"],
                    row["Appearances"],
                )
                players.append(p)

            except Exception as e:
                print(f"Warning: Skipping invalid row: {row} ({e})")

    return players



# Generate rankings based on goals, assists, etc.

def rank_players(players, sort_key):
    if sort_key == "goals":
        return sorted(players, key=lambda p: p.goals, reverse=True)

    elif sort_key == "assists":
        return sorted(players, key=lambda p: p.assists, reverse=True)

    elif sort_key == "contributions":
        return sorted(players, key=lambda p: p.total_contributions(), reverse=True)

    elif sort_key == "efficiency":
        return sorted(players, key=lambda p: p.efficiency(), reverse=True)

    else:
        print(f"Unknown sort type '{sort_key}'. Defaulting to goals.")
        return sorted(players, key=lambda p: p.goals, reverse=True)



# Optional club filter

def apply_club_filter(players, club_name):
    if club_name is None:
        return players
    return [p for p in players if p.club.lower() == club_name.lower()]



# Print player rankings

def print_ranking(players, sort_type, limit, outfile=None):
    ranking = rank_players(players, sort_type)
    header = f"=== Ranking by {sort_type.capitalize()} ===\n"

    output = header
    for p in ranking[:limit]:
        output += (
            f"{p.full_name():25}  "
            f"Goals: {p.goals:2}  Assists: {p.assists:2}  "
            f"Contrib: {p.total_contributions():2}  "
            f"Eff: {p.efficiency():.2f}\n"
        )

    print(output)

    if outfile:
        outfile.write(output + "\n")



# Club summary statistics

def print_club_summary(players, outfile=None):
    output = "\n=== Club Summary ===\n"

    clubs = {}
    for p in players:
        if p.club not in clubs:
            clubs[p.club] = {"goals": 0, "assists": 0, "players.csv": []}

        clubs[p.club]["goals"] += p.goals
        clubs[p.club]["assists"] += p.assists
        clubs[p.club]["players.csv"].append(p)

    for club, stats in clubs.items():
        top_player = max(stats["players.csv"], key=lambda p: p.total_contributions())

        block = (
            f"\n{club}\n"
            f" Total Goals:   {stats['goals']}\n"
            f" Total Assists: {stats['assists']}\n"
            f" Best Player: {top_player.full_name()} "
            f"({top_player.total_contributions()} contributions)\n"
        )

        output += block

    print(output)

    if outfile:
        outfile.write(output + "\n")



# Parse command-line arguments

def parse_arguments():
    args = sys.argv[1:]

    if len(args) == 0:
        print("Usage: python stats_analyser.py players.csv.csv "
              "[--limit N] [--club NAME] [--sort TYPE] [--export FILE]")
        sys.exit(1)

    filename = args[0]
    limit = 10
    club = None
    sort_type = "goals"
    export_file = None

    i = 1
    while i < len(args):
        if args[i] == "--limit":
            limit = int(args[i + 1])
            i += 2

        elif args[i] == "--club":
            club = args[i + 1]
            i += 2

        elif args[i] == "--sort":
            sort_type = args[i + 1]
            i += 2

        elif args[i] == "--export":
            export_file = args[i + 1]
            i += 2

        else:
            print(f"Unknown argument: {args[i]}")
            sys.exit(1)

    return filename, limit, club, sort_type, export_file



# Program entrypoint

def main():
    filename, limit, club, sort_type, export_file = parse_arguments()

    players = load_players(filename)

    # Apply club filter if needed
    filtered_players = apply_club_filter(players, club)

    if len(filtered_players) == 0:
        print("No players.csv match your filter.")
        sys.exit(0)

    outfile = open(export_file, "w") if export_file else None

    print_ranking(filtered_players, sort_type, limit, outfile)
    print_club_summary(filtered_players, outfile)

    if outfile:
        outfile.close()


if __name__ == "__main__":
    main()
