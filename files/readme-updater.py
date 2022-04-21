#!/usr/bin/env python3
import os
import re
import subprocess
from pathlib import Path
import difflib

from rich import print

# groups and sites for README.md
sites = []
groups = ['Legacy', 'pcroland', 'NFC', 'NaGa', 'boOk', 'SFY', 'PTHD', 'FULCRUM', 'DenZo', 'ARROW', 'prldm', 'VARYG', '14V1', 'NYH', 'GS88', 'JBR', 'MGM']
banned_groups = []


def gettime(fl):
    fl = os.path.join(os.path.dirname(__file__), '..', fl)
    args = ['git', '--no-pager', 'log', '-1', '--pretty="%ci"', fl]
    r = str(subprocess.run(args, capture_output=True).stdout)
    r = re.findall('b\'\"(.*?) ', r)[0].replace('-', '.')
    r = f'{r}.'
    return r

def main():
    grps = sorted(list(dict.fromkeys(groups)), key=str.casefold)
    bgrps = sorted(list(dict.fromkeys(banned_groups)), key=str.casefold)
    sts  = sorted(list(dict.fromkeys(sites)), key=str.casefold)
    print(f'sorted deduplicated groups:\n[cyan]{", ".join(grps)}[/cyan]')
    print(f'sorted deduplicated sites:\n[cyan]{", ".join(sts)}[/cyan]')
    print(f'sorted deduplicated banned groups:\n[cyan]{", ".join(bgrps)}[/cyan]')
    grps_j = f'`{"`, `".join(grps)}`\n' if grps else ''
    bgrps_j = f'`{"`, `".join(bgrps)}`\n' if bgrps else ''
    sts_j = f'`{"`, `".join(sts)}`\n' if sts else ''

    t1 = gettime('series-and-movies-x264-sd-and-480p.md')
    t2 = gettime('series-and-movies-x264-hd.md')
    t3 = gettime('series-and-movies-x265-hd-uhd.md')
    t4 = gettime('series-and-movies-remux.md')
    print(f'modification dates:\nSD    : [not bold cyan]{t1}[/not bold cyan]\nHD    : [not bold cyan]{t1}[/not bold cyan]\nUHD   : [not bold cyan]{t1}[/not bold cyan]\nRemux : [not bold cyan]{t1}[/not bold cyan]')
    readme = f'''## A magyar release-ek készítésénél követendő szabályok
| kategória                                                     | utolsó frissítés | érvényben         |
| :-                                                            | :-               | :-                |
| [**x264 SD és 480p**](/series-and-movies-x264-sd-and-480p.md) | {   t1    }      | 2020.02.19.       |
| [**x264 HD**](/series-and-movies-x264-hd.md)                  | {   t2    }      | 2020.02.19.       |
| [**x265 UHD-HD**](/series-and-movies-x265-hd-uhd.md)          | {   t3    }      | 2020.06.14.       |
| [**REMUX**](/series-and-movies-remux.md)                      | {   t4    }      | 2020.06.14.       |
| **DVD, MP3 és lossless audio** (korábbi szabályzat érvényben) |                  |                   |

## [Nuke indokok](/nuke-reasons.md)

## [Toolok](/files/tools.md)

## Csapatok, akik aláírták és tudomásul vették (ábécé sorrendben){" - " + str(len(grps)) + " csapat" if len(grps) > 0 else ""} ([link](https://github.com/encoding-hun/rules-and-standards/issues/14))
{grps_j}
## Oldalak, amelyek aláírták{" - " + str(len(sts)) + " oldal" if len(sts) > 0 else ""} ([link](https://github.com/encoding-hun/rules-and-standards/issues/18))
{sts_j}
## Banned groups{" - " + str(len(bgrps)) + " csapat" if len(bgrps) > 0 else ""}
{bgrps_j}'''

    new_readme = open(os.path.join(os.path.dirname(__file__), '..', 'README2.md'), 'w')
    new_readme.write(readme)
    new_readme.close()

    diff_old = open(os.path.join(os.path.dirname(__file__), '..', 'README.md'), 'r')
    diff_new = open(os.path.join(os.path.dirname(__file__), '..', 'README2.md'), 'r')
    diff = difflib.unified_diff(diff_old.readlines(), diff_new.readlines(), n=0)
    diff_old.close()
    diff_new.close()
    print(f'difference between old and new README.md:\n[cyan]{"".join(diff)}[/cyan]')
    os.remove(os.path.join(os.path.dirname(__file__), '..', 'README.md'))
    os.rename(os.path.join(os.path.dirname(__file__), '..', 'README2.md'), os.path.join(os.path.dirname(__file__), '..', 'README.md'))
    print('[green]File saved. ✅[/green]')

if __name__=='__main__':
    main()
