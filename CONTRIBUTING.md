# Installation

## Installing Python 3 with Tkinter

Mac OS X:

    $ xcode-select install
    $ brew install homebrew/dupes/tcl-tk
    $ brew install python3 --with-tcl-tk

Refer more to this [StackOverflow question](https://stackoverflow.com/questions/36760839/why-my-python-installed-via-home-brew-not-include-tkinter).

## Installing in a Virtual Environment \[RECOMMENDED\]

### `virtualenv`

### `virtualenvwrapper` \[RECOMMENDED\]

## Pip packages

```
(Hex) $ pip install -U pip
(Hex) $ pip install pip-tools
(Hex) $ pip-sync requirements_dev.txt
```
