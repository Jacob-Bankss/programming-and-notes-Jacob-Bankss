# Stats Analyser

This Python program reads a CSV file of football player statistics and produces rankings based on goals, assists, total contributions, or efficiency. It can also filter players by club and export results to a file.

---

## How to Run

```bash
python stats_analyser.py players.csv --sort goals --limit 10
```

### Optional arguments

| Argument        | Purpose                                           |
|-----------------|---------------------------------------------------|
| `--limit N`     | Number of players to show                         |
| `--club NAME`   | Filter by club                                    |
| `--sort TYPE`   | `goals`, `assists`, `contributions`, `efficiency` |
| `--export FILE` | Save output to a file                             |

### Example:

```bash
python stats_analyser.py players.csv --sort efficiency --club Chelsea --limit 5
```

---

## CSV Format

The CSV file must contain the following columns **and is provided**:

```
Firstname,Surname,Club,Appearances,Goals,Assists
```

---

## AI Assistance Declaration

> **AI Assistance Declaration:**  
> This program and parts of this README were created with the assistance of generative AI (ChatGPT). AI was used to help draft code and explanations. I have reviewed and tested all material to ensure I understand how the program works and take full responsibility for the final submission, in line with Leeds Beckett University’s Principles for the use of Generative AI.

