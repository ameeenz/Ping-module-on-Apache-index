#!/usr/bin/env python3
          import subprocess
          import cgi
          import ipaddress

          print("Content-Type: text/html\n")

          form = cgi.FieldStorage()
          target_ip = form.getvalue("target_ip")

          def is_valid_ip(ip):
              try:
                  ipaddress.ip_address(ip)
                  return True
              except ValueError:
                  return False

          def ping_server(ip, count=4):
              try:
                  result = subprocess.run(
                      ["ping", "-c", str(count), ip],
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE,
                      text=True
                  )
                  
                  if result.returncode == 0:
                      print(f"<h2>ping {ip} was successful</h2>")
                      print(f"<pre>{result.stdout}</pre>")
                  else:
                      print(f"<h2>ping {ip} was not successful</h2>")
                      print(f"<pre>{result.stderr}</pre>")

              except Exception as e:
                  print(f"<p>error:  {e}</p>")
              
          if not target_ip:
              print("<p>Please enter the customer ip</p>")

          if not is_valid_ip(target_ip):
              print("<p>Please enter the correct IP format</p>")

          print("<h1>Customer server ping result:</h1>")
          ping_server(target_ip)
