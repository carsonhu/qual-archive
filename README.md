# qual-archive
Archive of UCI Qualification Exam Problems, with problems split into different categories. Let me know if you believe any categories should be created / removed, or if you believe problems should be added / removed from a category.

complex_archive.pdf is the PDF that contains all the UCI Qual problems. COMPLEX_QUALIFYING_EXAM_ARCHIVE.tex holds the list of qual problems.

# Tags

Problems are tagged with a unique **tag** ([SEASON][YEAR].[QUESTION NUMBER]) such as S06.3 for Spring 2006 Problem 3, or F11.8 for Fall 2011 Problem 11.

Problems also have an **ID** to classify them in one or more categories (e.g entire, meromorphic, integral, etc.).

A problem's ID is considered based on the wording of the question, not the method used to solve it.

Currently, the list of IDs is:

1. **Misc** - Miscelleaneous problems which I couldn't figure out how to categorize.
2. **Integral** - Problems which have to do with solving an integral.
3. **Entire** - Problems that have to deal with entire functions (this is naturally a very broad topic)
4. **Meromorphic** - Problems that deal with meromorphic functions.
5. **Bound** - Problems which investigate functions bounded by an inequality.
6. **Zeros** - Problems which investigate the zeros of a holomorphic function.
7. **Normal** - Problems which deal with normal familys, or functions which converge uniformly on compact subsets.
8. **Series** - Problems that deal with series.
9. **Automorphism** - Problems that deal with automorphisms.
10. **Conformal** - Problems that deal with conformal maps.
11. **Holomorphic** - Problems that are primarily focused on holomorphicity of functions.
12. **Product** - Problems involving infinite products.
13. **Harmonic** - Problems involving harmonic functions.
14. **Singularity** - Problems involving singularities of functions.
15. **Subharmonic** - Problems involving subharmonic functions.
16. **Cauchy** - Problems that look suspiciously similar to the Cauchy integral formula (should probably be removed)

# Modifying the Archive

archive_creator.py generates the output tex file (complex_archive.tex) based off of the data from COMPLEX_QUALIFYING_EXAM_ARCHIVE.tex. 

To edit a problem's IDs or tag, search it up in COMPLEX_QUALIFYING_EXAM_ARCHIVE.tex and modify the problem's ID's or tag. Then run archive_creator.py to update the PDF.

# Usage

Requires python 3.6. Built in MiKTeX. Ideally, you open up command line and run
```
python archive_creator.py
```
And this constructs complex_archive.tex and builds complex_archive.pdf.
