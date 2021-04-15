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
MENUITEMS = [('Publications', '/pubs/'),
             ('Presentations', '/presentations/')]

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
            dict(name='CEED', url='http://ceed.exascaleproject.org/',
                 description="Center for Efficient Exascale Discretization"),
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
          ('twitter', 'https://twitter.com/five9a2'),
          #('diaspora', 'https://diasp.org/u/jed'),
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
  <a href="mailto:jed@jedbrown.org">jed at jedbrown.org</a> <br />

  <strong>Assistant Professor</strong> <br />
  <a href="http://colorado.edu/cs/">Department of Computer Science</a><br />
  University of Colorado Boulder<br />
  430 UCB, Boulder, CO 80309
</p>

<h5><a href="research">Research</a></h5>
<p>Our research is in fast algorithms and robust community software for physically-based modeling, prediction, inference, and design.
Check out our <a href="https://phypid.org">PhyPID research group website</a> for more about our research as well as current and former members.</p>

<h5>Editorial Board</h5>
<ul>
  <li>Associate Editor for <a href="http://joss.theoj.org/">Journal of Open Source Software (JOSS)</a></li>
</ul>

<h5>Awards</h5>
<ul>
  <li>2015 SIAM/ACM Prize in Computational Science and Engineering (PETSc team)</li>
  <li>2014 IEEE TCSC Young Achiever</li>
  <li>2014 SIAG/SC Junior Scientist Prize</li>
  <li>2010 Piolet d'Or for the first ascent of Xuelian West (6422 m, China) via "The Great White Jade Heist" (with Kyle Dempster and Bruce Normand)</li>
</ul>
<h5><a href="files/jed-cv.pdf">CV (pdf)</a></h5>
<h3>Teaching</h3>
<p><a href="//github.com/cu-numcomp/numcomp-class/"><strong>Numerical Computation</strong>: CSCI-3656, Spring 2020</a></p>
<p><a href="//cucs-hpsc.github.io/fall2019/"><strong>High Performance Scientific Computing</strong>: CSCI-5576/4576, Fall 2019</a></p>
<p><a href="//github.com/cu-numcomp/numcomp-class-spring19/"><strong>Numerical Computation</strong>: CSCI-3656, Spring 2019</a></p>
<p><a href="//github.com/cucs-numpde/numpde"><strong>Numerical Solution of Partial Differential Equations</strong>: CSCI-5636, Fall 2018</a></p>
<p><a href="//github.com/jedbrown/csci-3656"><strong>Numerical Computation</strong>: CSCI-3656, Spring 2018</a></p>
<p><a href="//github.com/cucs-numpde/numpde-fall2017"><strong>Numerical Solution of Partial Differential Equations</strong>: CSCI-5636, Fall 2017</a></p>
<p><a href="//github.com/cucs-hpla/class"><strong>High-Performance Linear Algebra</strong>: CSCI-4830/7000, Spring 2017</a></p>
<p><a href="//github.com/jedbrown/numerical-computation"><strong>Numerical Computation</strong>: CSCI-3656, Fall 2016</a></p>
<p><a href="topics-in-cse"><strong>Topics in Computational Science and Engineering</strong>: CSCI-4830-008/7000-014, Fall 2015</a></p>
<p><a href="hpc-performance-analysis"><strong>HPC Performance Analysis</strong>: CSCI-4830-014/7000-018, Spring 2015</a></p>

<h3>Identity</h3>
<p><a href="files/jed-pgp.asc">PGP Public Key</a> to verify my signed mail or encrypt to me.</p>
<p><a href="files/jed-id_ed25519.pub">SSH Public Key</a> to grant me login access, git push, etc.</p>
""" % dict(SITEURL=SITEURL))

THEME = 'theme'
BOOTSTRAP_THEME = 'spacelab'
PYGMENTS_STYLE = 'default'

PUBLICATIONS_SRC = 'content/jedpub.bib'
DIRECT_TEMPLATES = ('index', 'pubs/index', 'tags', 'archives')

def latex_decode(latexsrc):
    import codecs
    import latexcodec
    utf8src = codecs.decode(latexsrc.encode(), 'latex+utf-8')
    s = utf8src.replace('{','').replace('}','')
    return s
JINJA_FILTERS = dict(latex_decode=latex_decode, strip=str.strip)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
