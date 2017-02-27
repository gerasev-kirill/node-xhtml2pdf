# -*- coding: utf-8 -*-
import sys, logging
from six import BytesIO
from xhtml2pdf import pisa



class PisaNullHandler(logging.Handler):
    def emit(self, record):
        pass

logging.getLogger("xhtml2pdf").addHandler(PisaNullHandler())





def html_top_pdf(content, encoding='utf-8'):
    try:
        src = BytesIO(content.encode(encoding))
    except:
        src = BytesIO(content)
    dest = BytesIO()

    pdf = pisa.pisaDocument(src, dest, encoding=encoding)

    if pdf.err:
        err = [
            "Error rendering PDF document\n",
            "==============================",
            content+'\n',
            "=============================="
            ]
        for entry in pdf.log:
            if entry[0] == xhtml2pdf.default.PML_ERROR:
                err.append(
                    "Error: line %s, msg: %s, fragment: %s" % (entry[1], entry[2], entry[3])
                )
        return ("\n".join(err), None)

    return (None, dest.getvalue())



def main():
    lines = sys.stdin.readlines()
    data = ''.join(lines)
    err, pdf = html_top_pdf(data)
    if err:
        print >> sys.stderr, err
    else:
        print pdf


if __name__ == '__main__':
    main()
