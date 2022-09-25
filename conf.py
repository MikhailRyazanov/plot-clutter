project = 'Demo'

source_suffix = ['.rst']
master_doc = 'index'
extensions = ['matplotlib.sphinxext.plot_directive']

# Options for matplotlib.sphinxext.plot_directive:

# save SVG for HTML and PDF for pdfLaTeX (omitted from Makefile for clarity)
# (all formats must be saved at once because real plotting scipts are too
# computationally expensive for rerunning them multiple times)
plot_formats = ['svg', 'pdf']

# do not add links to image formats
plot_html_show_formats = False

# do not add links to source automatically
plot_html_show_source_link = False
