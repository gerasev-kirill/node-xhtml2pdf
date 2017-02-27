# out: false
expect = require('chai').expect
assert = require('chai').assert
log = require('logging').from(__filename)
fs = require('fs-extra')
path = require('path')
spawn = require('child_process').spawn

html2Pdf = require('../lib/html2Pdf')
html2PdfFile = require('../lib/html2PdfFile')

BASE_DIR = path.dirname(__dirname)
FIXTURES_DIR = BASE_DIR + '/test/fixtures'





it 'should generate pdf from html', (done)->
    data = fs.readFileSync(path.join(FIXTURES_DIR, 'test.html'))
    html = data.toString()
    html = html.replace('FIXTURES_DIR', FIXTURES_DIR)
    html2PdfFile html, '/tmp/test.pdf', (err, pdf)->
        spawn('evince', ['/tmp/test.pdf'])
        console.log err
        done()
