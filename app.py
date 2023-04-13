from flask import Flask, request, render_template
import pandas as pd
import io
  
app = Flask(__name__)
  
UPLOAD_FOLDER = 'static/uploads/'
  
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        file_content = file.read()

        #csvStringIO = StringIO(file_content)

        columns=['name','type']
        df = pd.read_csv(io.BytesIO(file_content), sep=",", header=None,names=columns)
        for i, row in df.iterrows():
            name = row['name']
            type = row['type']
            # people love yeast :D
            if (name == "yeasty"):
                return render_template("yeasty.html")
          
        # check if file loaded successfully or not
        if file_content:
            return "Uploaded Successful"
        else:
            return "Uploaded Unsuccessful"
  
    return render_template("index.html")
  
if __name__ == "__main__":
    app.run(debug=True)

# //////
## original source: https://www.geeksforgeeks.org/read-file-without-saving-in-flask/
##          source: https://medevel.com/flask-tutorial-upload-csv-file-and-insert-rows-into-the-database/
##          source: https://realpython.com/python-send-email/
# //////
## Inniciar APP
# python3 app.py    
## Acceder a: http://127.0.0.1:5000
## //////
# Paquetes a importar:
## pip install pandas
## pip install flask
# //////