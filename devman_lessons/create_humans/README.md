# Create humans

The program creates 10 game character cards in `svg` format. Developed using the `file_operations` module and the `Faker` library.

# How to start

Clone the repository with ssh:
```bash
git clone git@github.com:MaxHC-vlop/create_humans.git
```

Create a virtual environment on directory project:
```bash
python3.10 -m venv env
```

Start the virtual environment:
```bash
. env/bin/activate
```

Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```bash
pip install -r requirements.txt
```

Directory structure :
```
.
├── main.py
│   file_operations.py
│   README.md
│   requirements.txt
│
├── src
│   └── template.svg
└── output
    └── svg
        └── result.svg
```

## Run

Launch on Linux(Python 3.10) or Windows as simple:
```bash
python main.py
```