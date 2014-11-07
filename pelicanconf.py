# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jed Brown'
SITENAME = 'Jed Brown'
SITEURL = 'http://jedbrown.org'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [('Publications', '/pubs/')]

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}/index.html'

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

PORTRAIT_IMG = 'images/jed.jpg'
PORTRAIT_ALT = "Jed's head"

SOFTWARE = [dict(name='PETSc', url='http://mcs.anl.gov/petsc',
                 description='Portable Extensible Toolkit for Scientific computing: an library of parallel algebraic solvers and time integrators'),
            dict(name='PISM', url='http://pism-docs.org',
                 description='Parallel Ice Sheet Model.'),
            dict(name='Dohp', url='https://github.com/jedbrown/dohp',
                 description='Dual-order h- and p-version finite element library.'),
            dict(name='git-fat', url='https://github.com/jedbrown/git-fat',
                 description='A simple approach to large file support for Git.'),]
#PROJECTS = SOFTWARE             # Some themes use the other name

# Social widget
SOCIAL = [('github', 'https://github.com/jedbrown'),
          ('bitbucket', 'https://bitbucket.org/jedbrown'),
          ('scicomp.stackexchange', 'http://scicomp.stackexchange.com/users/119/jed-brown'),
          ('diaspora', 'https://diasp.org/u/jed'),
          ('scholar', 'http://scholar.google.com/citations?hl=en&user=x_9_NGwAAAAJ')]

DEFAULT_PAGINATION = False

PLUGINS = ['render_math',
           'pelican_bibtex',
           'extract_toc']
PLUGIN_PATHS = ['./pelican-plugins', './pelican-bibtex']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
STATIC_PATHS = ['theme/images', 'images', 'files']

LANDING_PAGE_ABOUT = dict(title='Jed Brown',
                          details=
"""
<p>
  <a href="mailto:jedbrown@mcs.anl.gov">jedbrown at mcs.anl.gov</a> <br />

  <strong>Assistant Computational Mathematician</strong> <br />
  <a href="http://mcs.anl.gov/research/LANS">Laboratory for Advanced Numerical Simulation</a><br />
  <a href="http://mcs.anl.gov">Mathematics and Computer Science Division</a><br />
  Argonne National Laboratory<br />
  9700 S Cass, Bldg 240<br />
  Lemont, IL 60439

</p>

<p>
  <strong>Assistant Professor Adjoint</strong> <br />
  <a href="http://colorado.edu/cs/">Department of Computer Science</a><br />
  University of Colorado Boulder<br />
  430 UCB, Boulder, CO 80309
</p>

<h5><a href="files/jed-cv.pdf">CV (pdf)</a></h5>
<h5><a href="research">Research</a></h5>
""" % dict(SITEURL=SITEURL))

THEME = 'theme'
BOOTSTRAP_THEME = 'spacelab'
PYGMENTS_STYLE = 'default'

PUBLICATIONS_SRC = 'content/jedpub.bib'
DIRECT_TEMPLATES = ('index', 'pubs/index', 'tags', 'archives')

def latex_decode(latexsrc):
    import codecs
    import latexcodec
    utf8src = codecs.decode(latexsrc, 'ulatex')
    s = utf8src.replace('{','').replace('}','')
    return s
JINJA_FILTERS = dict(latex_decode=latex_decode, strip=str.strip)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
