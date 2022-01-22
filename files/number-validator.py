#!/usr/bin/env python3
from pathlib import Path
from rich import print
import os
import re
import sys


def printexit(number):
    print(f'[red]error at: [/red][cyan]{number}[/cyan]')
    sys.exit(1)


def validate(f):
    print(f'[bold green]{f}: [/bold green]', end='')
    t = Path(os.path.join('..', f)).read_text()
    numbers = re.findall('(?:  -|##) ([0-9.]+)\)', t)
    for n in range(1, len(numbers)):
        p = numbers[n - 1]
        c = numbers[n]
        p_len = len(p.split('.'))
        c_len = len(c.split('.'))
        p_last = int(p.split('.')[-1])
        c_last = int(c.split('.')[-1])
        if c_len == p_len:
            if c_last - p_last != 1: printexit(c)
        elif c_len - p_len == 1:
            if c != f'{p}.1': printexit(c)
        elif c_len - p_len < 0:
            if int(c.split('.')[c_len-1]) - int(p.split('.')[c_len-1]) != 1: printexit(c)
        else:
            printexit(f'[red]4 error at: [/red][cyan]{c}[/cyan]')
    print('✅')


def main():
    files = ['nuke-reasons.md', 'series-and-movies-x264-sd-and-480p.md', 'series-and-movies-x264-hd.md', 'series-and-movies-remux.md', 'series-and-movies-x265-hd-uhd.md']
    for f in files:
        validate(f)


if __name__=='__main__':
    main()
