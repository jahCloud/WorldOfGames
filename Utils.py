from pathlib import Path

SCORES_FILE_NAME = open(Path("Scores.txt"), "x", encoding='utf-8')
BAD_RETURN_CODE = int(401)

def Screen_cleaner():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
