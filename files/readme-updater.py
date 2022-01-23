#!/usr/bin/env python3
import os
import re
import subprocess
from pathlib import Path

from rich import print

# groups and sites for README.md
sites = []
groups = ['Legacy', 'pcroland', 'NFC', 'NaGa', 'boOk', 'SFY', 'PTHD', 'FULCRUM', 'DenZo', 'ARROW', 'prldm', 'VARYG', '14V1', 'NYH']
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
    grps = f'`{"`, `".join(grps)}`\n' if grps else ''
    bgrps = f'`{"`, `".join(bgrps)}`\n' if bgrps else ''
    sts = f'`{"`, `".join(sts)}`\n' if sts else ''

    t1 = gettime('series-and-movies-x264-sd-and-480p.md')
    t2 = gettime('series-and-movies-x264-hd.md')
    t3 = gettime('series-and-movies-x265-hd-uhd.md')
    t4 = gettime('series-and-movies-remux.md')
    print(f'modification dates:\nSD    : [not bold cyan]{t1}[/not bold cyan]\nHD    : [not bold cyan]{t1}[/not bold cyan]\nUHD   : [not bold cyan]{t1}[/not bold cyan]\nRemux : [not bold cyan]{t1}[/not bold cyan]')
    readme = f'''## A magyar release-ek készítésénél követendő szabályok
| kategória                                                     | utolsó frissítés | érvényben         |
| :-                                                            | :-               | :-                |
| [**x264 SD és 480p**](series-and-movies-x264-sd-and-480p.md)  | {   t1    }      | 2020.02.19.       |
| [**x264 HD**](series-and-movies-x264-hd.md)                   | {   t2    }      | 2020.02.19.       |
| [**x265 UHD-HD**](series-and-movies-x265-hd-uhd.md)           | {   t3    }      | 2020.06.14.       |
| [**REMUX**](series-and-movies-remux.md)                       | {   t4    }      | 2020.06.14.       |
| **DVD, MP3 és lossless audio** (korábbi szabályzat érvényben) |                  |                   |

## [Nuke indokok](nuke-reasons.md)

## [Toolok](files/tools.md)

## Csapatok, akik aláírták és tudomásul vették (ábécé sorrendben) - 14 csapat ([link](https://github.com/encoding-hun/rules-and-standards/issues/14))
{grps}
## Oldalak, amelyek aláírták ([link](https://github.com/encoding-hun/rules-and-standards/issues/18))
{sts}
## Banned groups
{bgrps}'''

    readme_file = open(os.path.join(os.path.dirname(__file__), '..', 'README.md'), 'w')
    readme_file.write(readme)
    readme_file.close()
    print('[green]File saved. ✅[/green]')

if __name__=='__main__':
    main()
