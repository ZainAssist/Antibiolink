import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="author" content="Uff_Zainu" />
    <meta name="keywords" content="Antibiolink, Antibiolink,  Antibiolink" />
    <meta name="description" content="Bot for Bio Restriction ." />
    <meta property="og:description" content="Uff_Zainu Antibiolink.">	  
    <title> Save Restricted Bot - By •⊹٭Zain٭⊹•</title>
    <link rel="icon" type="image/x-icon" https://graph.org/file/c0af786775fd598580456-a4c3ec22e99c148b1d.jpg" type="image/x-icon" />
  </head>

   <body>
   <center>
       <img src="https://graph.org/file/c0af786775fd598580456-a4c3ec22e99c148b1d.jpg" alt="Antibiolink" style="width:50px;height:50px;border-radius: 100px;">
       <h1 class="font-bold" id="Antibiolink">Antibiolink </h1>
       <p class="font-bold" id="Bot successfully">Bot successfully Running...</p>
   </center>
   </body>
<center> 
    <img src="https://graph.org/file/c0af786775fd598580456-a4c3ec22e99c148b1d.jpg" height="200" width="200" style="border-radius: 12px;"/>
    <br>
    <a href="https://t.me/About_Zain" target="_blank"><img align="center" src="https://graph.org/file/c0af786775fd598580456-a4c3ec22e99c148b1d.jpg" alt="Star" height="200" width="200" /></a>
</p>
</center>
<br>
<footer class="bg-blue-500 font-bold text-white text-center py-3 mt-5">
<center>
        Powered By <a href="https://t.me/Uff_Zainu" target="_blank"> •⊹٭Zain٭⊹•</a>
		<div class="footer__copyright">
            <p class="footer__copyright-info">
                © 2025 Antibiolink. All rights reserved.
            </p></center>
        </div>
    </footer>
<style>
    body { 
        background: antiquewhite;
    }
</style>"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port)
