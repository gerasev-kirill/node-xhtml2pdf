path = require('path')
spawn = require('child_process').spawn

BASE_DIR = path.dirname(__dirname)





module.exports = (htmlData, cb)->
    pdf = []
    err = ''
    pyHtml2Pdf = spawn(path.join(BASE_DIR, 'html2pdf.sh'), {
        cwd: BASE_DIR
    })

    pyHtml2Pdf.stdout.on 'data', (data)->
        pdf.push(data)

    pyHtml2Pdf.stderr.on 'data', (data)->
        err = err + data.toString()

    if cb
        pyHtml2Pdf.stdout.on 'end', ()->
            if !err.length
                err = null
                pdf = Buffer.concat(pdf)
            else
                pdf = null
            cb(err, pdf)

    pyHtml2Pdf.stdin.write(htmlData)
    pyHtml2Pdf.stdin.end()
