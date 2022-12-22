# Diary hack

Fixes the diary for the better .

## How to install

- Сlone this repository:
```bash
git clone git@github.com:MaxHC-vlop/diary_hack.git
```
- You must have python3.9 (or higher) installed.

- The file must be in the same directory as the manage.py .
```
.
├── README.md
│   requirements.txt
│   manage.py
│   scripts.py (your_file_here)
│
├── datacenter/
└── project/


```

## Arguments
`-f --full_name` - student's name (required argument)

`-m --marks` - fix bad grades by 5 (default `False`)

`-c --chastisement` - removes all bad comments (default `False`)

`-d --discipline` - name of the discipline (obligatory argument to create `praise`)

`-r --commendation` - produces `praise` on a specified subject (default `False`)

### Example
```bash
# Fixes all bad grades
python scripts.py -f 'Фролов Иван' -m

# Removes all bad comments
python scripts.py -f 'Фролов Иван' -c

# Creates good comments on music
python scripts.py -f 'Фролов Иван' -d 'Музыка' -r
```