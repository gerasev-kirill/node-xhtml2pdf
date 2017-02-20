(function() {
  var fs, html2Pdf;

  fs = require('fs');

  html2Pdf = require('./html2Pdf');

  module.exports = function(htmlData, filename, cb) {
    return html2Pdf(htmlData, function(err, pdf) {
      if (!err) {
        fs.writeFileSync(filename, pdf);
      }
      return cb(err, pdf);
    });
  };

}).call(this);
