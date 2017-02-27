(function() {
  var html2Pdf, html2PdfFile;

  html2Pdf = require('./html2Pdf');

  html2PdfFile = require('./html2PdfFile');

  module.exports = {
    html2Pdf: html2Pdf,
    html2PdfFile: html2PdfFile
  };

}).call(this);
