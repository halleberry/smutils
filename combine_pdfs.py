import os

# pip install "pypdf[image]"
from pypdf import PdfWriter


def combine_pdfs(infiles, outfile):
    """
    Combine multiple PDF files into a single PDF file.

    Args:
        infiles (list): List of file paths of the PDF files to be combined.
        outfile (str): File path of the output PDF file.

    >>> _infiles = ['~/Pictures/1.pdf', '~/Pictures/2.pdf', '~/Pictures/3.pdf', '~/Pictures/4.pdf']
    ... _outfile = '~/Pictures/combined.pdf'
    ... combine_pdfs(_infiles, _outfile)

    Returns:
        None
    """
    
    _merge(infiles, outfile)


def _merge(infiles, outfile):
    outfile = os.path.expanduser(outfile)
    if not os.path.exists(outfile):
        os.makedirs(os.path.dirname(outfile), exist_ok=True)

    merger = PdfWriter()

    for infile in infiles:
        infile = os.path.expanduser(infile)
        if infile.endswith('.pdf'):
            merger.append(infile)
        else:
            print(f"Skipping non-PDF file: {infile}")

    outfile_tbd = os.path.join(os.path.dirname(outfile), 'tbd.pdf')
    merger.write(outfile_tbd)
    merger.close()

    _reduce_size(infile=outfile_tbd, outfile=outfile)


def _reduce_size(infile, outfile):
    writer = PdfWriter(clone_from=infile)

    for _page in writer.pages:
        _page.compress_content_streams(1)

    with open(outfile, "wb") as f:
        writer.write(f)

    writer.close()




