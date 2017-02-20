fs = require('fs')
html2Pdf = require('./html2Pdf')


module.exports = (htmlData, filename, cb)->
    html2Pdf htmlData, (err, pdf)->
        if !err
            fs.writeFileSync(filename, pdf)
        cb(err, pdf)
