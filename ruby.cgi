#!"C:\xampp\ruby\mingw64\bin\ruby.exe"

require 'C:\xampp\ruby\mingw64\lib\ruby\2.6.0\cgi'

cgi = CGI.new

cgi.http_header(
                  "Connection" => "close",
                  "Type"       => "text/html",
                  "Charset"    => "utf-8"
                )

print cgi.http_header

print "Hello World \n"
