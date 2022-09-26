# Demo of output cluttering by Matplotlib plot directive

[Matplotlib plot directive](https://matplotlib.org/stable/api/sphinxext_plot_directive_api.html)
in some cases copies unnecessary files to the output directory.
This is a minimal working example for
[issue #24005](https://github.com/matplotlib/matplotlib/issues/24005).

Steps to reproduce:

1. Stray files in a “clean” build:

   a. Run `make clean`, just in case, to ensure a clean build.
   b. Run `make singleghtml` to produce a “single HTML” build.
   c. Inspect the output directory `build/singleghtml` — in addition to the
      necessary file `index.html` and the `_static` and `_images` directories
      (the latter contains all the necessary images used in `index.html`),
      there are also absolutely unnecessary and unreferenced SVG and PDF files
      directly and inside the absolutely unnecessary and unreferenced
      subdirectory `subdir`.

2. No stray files when reusing another build:

   a. Run `make clean` to clean the previous build results.
   b. Run `make html` to produce a regular “HTML” build in `build/html`.
      The output also has the same unnecessary and unreferenced files, as
      above, but this is not the point.
   c. Run `make singleghtml` to produce a “single HTML” build, which will reuse
      the images already produced by the previous build.
   d. Inspect the output directory `build/singleghtml` — now it looks as
      expected, without any unnecessary and unreferenced SVG and PDF files and
      subdirectories (all used images are properly inside `_images`).
