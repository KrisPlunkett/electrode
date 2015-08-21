# Electrode

## Setup

Prerequisites:
* [Homebrew](http://brew.sh/)
* [Python with pip](http://stackoverflow.com/a/17271838)
* [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)

### Python environment

Clone the repo and `cd` into it.

*Run all commands from the project root*

Create the virtual environment:
```Bash
$ mkvirtualenv electrode
```

Install Python dependencies
```Bash
$ pip install -r requirements.txt
```

## Git practices

Adding features:

1. Create a branch off `master`

2. Do your work, commit often, write tests first (if possible).

3. When ready, push up your branch.  

4. Make a pull request from your branch into `master`

5. Let **someone else** code review and merge your PR.

Bug fixes:

1. Report an [issue](https://guides.github.com/features/issues/).

2. In the issue, document how to recreate the bug.

## Resources
- https://www.fyears.org/2015/06/electron-as-gui-of-python-apps.html
- https://medium.com/developers-writing/building-a-desktop-application-with-electron-204203eeb658
- http://flask.pocoo.org/
