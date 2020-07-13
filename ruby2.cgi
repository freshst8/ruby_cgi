#!"C:\absolute\path\to\ruby.exe"

require '\path\to\ruby\module\cgi'

cgi = CGI.new

cgi.http_header(
                  "Connection" => "keep-alive",
                  "Type"       => "text/html",
                  "Charset"    => "utf-8"
                )

print cgi.http_header

print "Hello World \n"
