(function() {
  var BASE_DIR, path, spawn;

  path = require('path');

  spawn = require('child_process').spawn;

  BASE_DIR = path.dirname(__dirname);

  module.exports = function(htmlData, cb) {
    var err, pdf, pyHtml2Pdf;
    pdf = '';
    err = '';
    pyHtml2Pdf = spawn(path.join(BASE_DIR, 'html2pdf.sh'));
    pyHtml2Pdf.stdout.on('data', function(data) {
      return pdf = pdf + data;
    });
    pyHtml2Pdf.stderr.on('data', function(data) {
      return err = err + data.toString();
    });
    if (cb) {
      pyHtml2Pdf.stdout.on('end', function() {
        if (!err.length) {
          err = null;
        }
        return cb(err, pdf);
      });
    }
    pyHtml2Pdf.stdin.write(htmlData);
    return pyHtml2Pdf.stdin.end();
  };

}).call(this);
