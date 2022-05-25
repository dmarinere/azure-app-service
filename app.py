from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)


@app.route('/')
def index():
   date = str(datetime.now()).split()[0]
   return render_template('index.html', date=date)
  
  
if __name__ == '__main__':
   app.run()
