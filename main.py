from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form="""
<!doctype html>
<html>
       <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/ceaser" method="post">
        <label for="rot">rotate by:</label>
        <input id="rot" type="number" name="rot" value="0"/>
        </br>
        <input type="textarea" name="text" value="{0}"></textarea>
        </br>
        <input type= "submit"/>


        </form>
    </body>
</html> 
"""
@app.route("/ceaser", methods=['post'])
def encrypt ():
    rot=request.form['rot']
    text=request.form['text']
    new_text=rotate_string(str(text),int(rot))
    
    return form.format(new_text)

@app.route("/")
def index():
    return form.format("")


app.run()