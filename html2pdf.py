import sys
from six import BytesIO
from xhtml2pdf import pisa


def link_fallback(uri, rel):
    print '-----------------'
    print uri, rel
    return uri

def html_top_pdf(content, encoding='utf-8'):
    src = BytesIO(content.encode(encoding))
    dest = BytesIO()

    pdf = pisa.pisaDocument(src, dest, encoding=encoding, link_fallback=link_fallback)
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

    if pdf.warn:
        print 'Warn rendering PDF document'
        for entry in pdf.log:
            if entry[0] == xhtml2pdf.default.PML_WARNING:
                print "Line %s, msg: %s, fragment: %s" % (entry[1], entry[2], entry[3])

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
