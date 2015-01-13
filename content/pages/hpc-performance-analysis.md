Title: HPC Performance Analysis
Tags: teaching
Author: Jed Brown
Summary: CSCI-4830-014 / CSCI-7000-018 - HPC Performance Analysis
Status: hidden
Nosidebar: True

CU Boulder: CSCI 4830-014/7000-018 (Spring 2015)

Time: MW 6:30-7:45pm in ECCR 118

Instructor: [Jed Brown](https://jedbrown.org), [<tt>jed@jedbrown.org</tt>](mailto:jed@jedbrown.org), ECOT 626

## Class mailing list

Please use the [hpc-perf-analysis mailing list](https://jedbrown.org/lists/listinfo/hpc-perf-analysis) for general discussion about the course.
Notifications will be sent there.

## Git repositories and assignments

In-class exercises and homework will be organized through the [CUBoulder-HPCPerfAnalysis organization](https://github.com/CUBoulder-HPCPerfAnalysis) on [GitHub](https://github.com).
Each major topic will have a repository, questions should be asked using the issue tracker or inline comments, and changes submitted using pull requests.
You are encouraged to share work with others in the class, but please merge the original author's commit so that it is properly attributed.

* [memory](https://github.com/CUBoulder-HPCPerfAnalysis/memory)

New repositories will be created as we move to new topics.

# Abstract and scope

Each High Performance Computing (HPC) architecture is more challenging
than the last to utilize effectively.  This is due to changing
memory/CPU balance, higher performance variability, more complicated
software stacks, larger scale, the necessity of optimally scaling
algorithms, and changing science/engineering objectives.  This special
topics course will outline the current state of HPC architecture, design
tradeoffs in the roadmap, and modeling of performance-limiting factors
and whole-program performance.  We will use Janus for hands-on
experiments with representative applications, will analyze profiles from
larger machines of various architecture, and discuss examples from the
research literature.

### Architectural roadmaps and modeling
  * vectorization
  * instruction-level parallelism and hardware threads
  * memory hierarchy
  * coprocessors
  * modern networks
  * input/output and file systems
  * system software
  * variability and reliability

### Designing performance experiments
  * application requirements and figures of merit
  * instrumenting software
  * how and when to scale up
  * performance tools
  * diagnosing bottlenecks and scalability problems
  * presentation of results

### Application case studies
  * explicit PDE solvers (seismic wave propagation, turbulence)
  * implicit PDE solvers and multigrid methods (geodynamics, structural mechanics)
  * irregular graph algorithms (network analysis, genomics, game trees)
  * dense linear algebra and tensors (quantum chemistry)
  * fast methods for N-body problems (molecular dynamics, cosmology)
  * cross-cutting: data assimilation, uncertainty quantification

# Recommended References

* [Hager and Wellein, *Introduction to High Performance Computing for Scientists and Engineers*, CRC Press, 2010](http://www.crcpress.com/product/isbn/9781439811924)
* [Eijkhout, *Introduction to High-Performance Scientific Computing*, online, 2014](http://pages.tacc.utexas.edu/~eijkhout/istc/istc.html)
* [Drepper, *What Every Programmer Should Know About Memory*, online, 2007](http://www.akkadia.org/drepper/cpumemory.pdf)

#### Git

* [Official Git Documentation](http://git-scm.com/documentation)
* [Git for Computer Scientists](http://eagain.net/articles/git-for-computer-scientists/)
* [Learn Git Branching (interactive)](https://pcottle.github.io/learnGitBranching/)
* https://try.github.io/
* [Interactive Cheat Sheet](http://ndpsoftware.com/git-cheatsheet.html)


# Grading

50% in-class exercises & homework, 30% project, 20% oral exam
