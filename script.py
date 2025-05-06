#!/usr/bin/env python3
import re
import sys
import argparse
from pathlib import Path

# Recognize "1st", "2nd", "3rd", "4th", etc.
ORDINAL_SUFFIX = r'(?:st|nd|rd|th)'

# Map file extensions to the desired case style
EXT_MAP = {
    '.java': 'pascal',
    '.py':   'snake',
    '.cpp':  'snake',
    '.c':    'snake',
}

def split_words(s: str):
    """
    Break a string into alphanumeric chunks.
    E.g. "BinaryTreeLevelOrder" → ["binary", "tree", "level", "order"]
         "find_common_elements"   → ["find", "common", "elements"]
    """
    parts = re.findall(r'[A-Z]?[a-z]+|[0-9]+', s)
    if parts:
        return [p.lower() for p in parts]
    # fallback on non-alphanumeric separators
    return [p.lower() for p in re.split(r'[\W_]+', s) if p]

def to_snake(words):
    return '_'.join(words)

def to_pascal(words):
    return ''.join(w.capitalize() for w in words)

def normalize_solution(base: str, width: int, lang_style: str):
    """
    Normalize a non-daily-challenge solution filename.
    Returns the new basename, or None if there's no leading number.
    E.g. "3_longestSubstring" → "0003_LongestSubstring" (Pascal) or "0003_longest_substring" (snake)
    """
    m = re.match(r'^(\d+)[_\- ]*(.+)$', base)
    if not m:
        return None
    num, rest = m.groups()
    words = split_words(rest)
    rest_norm = to_pascal(words) if lang_style == 'pascal' else to_snake(words)
    return f'{int(num):0{width}d}_{rest_norm}'

def normalize_daily(base: str, day_width: int, pid_width: int):
    """
    Normalize a daily-challenge filename.
    Matches both "16th_2956_title" and "16_2956_title".
    Outputs: zero-padded day, zero-padded problem ID, snake_case title.
    """
    m = re.match(rf'^(\d+){ORDINAL_SUFFIX}?[_-](\d+)[_\-](.+)$', base)
    if not m:
        return None
    day, pid, rest = m.groups()
    words = split_words(rest)
    title = to_snake(words)
    return f'{int(day):0{day_width}d}_{int(pid):0{pid_width}d}_{title}'

def main(dry_run=False):
    root = Path('.')
    sol_ids = set()
    daily_files = []

    # First pass: collect all solution IDs to determine padding width
    for p in root.rglob('*'):
        if '.git' in p.parts or p.name.startswith('.'):
            continue
        if p.is_file() and p.suffix.lower() in EXT_MAP:
            rel_parts = [part.lower() for part in p.parts]
            if 'daily challenge' in rel_parts:
                daily_files.append(p)
            else:
                m = re.match(r'^(\d+)', p.stem)
                if m:
                    sol_ids.add(int(m.group(1)))

    sol_width = len(str(max(sol_ids))) if sol_ids else 4
    day_width, pid_width = 2, sol_width

    # Second pass: rename files
    for p in sorted(root.rglob('*')):
        if '.git' in p.parts or p.name.startswith('.'):
            continue
        if not p.is_file() or p.suffix.lower() not in EXT_MAP:
            continue

        ext = p.suffix.lower()
        base = p.stem
        rel_parts = [part.lower() for part in p.parts]

        # Choose which normalization to apply
        if 'daily challenge' in rel_parts:
            new_base = normalize_daily(base, day_width, pid_width)
        else:
            new_base = normalize_solution(base, sol_width, EXT_MAP[ext])

        if not new_base:
            # Skip files without a leading number
            continue

        new_name = new_base + ext
        new_path = p.with_name(new_name)
        if p == new_path:
            continue

        cmd = f'git mv "{p}" "{new_path}"'
        if dry_run:
            print(cmd)
        else:
            print(f'> {cmd}')
            p.rename(new_path)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(
        description="Normalize solution & daily-challenge filenames"
    )
    ap.add_argument('--dry-run', action='store_true',
                    help="Print git mv commands without executing")
    args = ap.parse_args()
    main(dry_run=args.dry_run)
