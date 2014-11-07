# Installation

Clone the website repository using

```
git clone --recursive https://github.com/jedbrown/jedbrown.org
```

## Dependencies
Python version 2.7 or 3.3+.

Install [Pelican](http://getpelican.com) from your package manager, via
`pip`, via `easy_install`, or manually.  Check that `pelican --version`
returns at least `3.4.0`.

Install [beautifulsoup4](https://pypi.python.org/pypi/beautifulsoup4/)
and [Markdown](https://pypi.python.org/pypi/Markdown) from your package
manager, via `pip`, via `easy_install`, or manually.  Check that `python
-c 'import bs4'` does not error.

Install [pybtex](http://sourceforge.net/projects/pybtex/) and the
development version (or 1.0.2, when released) of
[latexcodec](https://github.com/mcmtroffaes/latexcodec/).

### virtualenv (optional)

A portable way to install Pelican in a local sandbox without any special
permissions is to use
[virtualenv](https://pypi.python.org/pypi/virtualenv).  After installing
virtualenv,

```
$ cd hpgmg.org
$ virtualenv .
$ . bin/activate
$ pip install pelican beautifulsoup4 markdown
```

In the future, use `. bin/activate` before using this installation.

## Running

Run `make html` to build the website and `make serve` to activate a
local web server.  While this is running, visit `http://localhost:8000`
in a web browser.  Use `CTRL-C` to stop the server.
