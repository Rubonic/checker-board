from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)

@app.route("/")
def checkerBoard():
        return render_template('index.html',width=8,height=8,color1="black",color2="red")

@app.route("/<int:width>")
def checkerBoard1(width):
         return render_template('index.html',width=width,height=8,color1="black",color2="red")

@app.route("/<int:width>/<int:height>")
def checkerBoard3(width,height):
         return render_template('index.html',width=width,height=height,color1="black",color2="red")

@app.route("/<int:width>/<int:height>/<string:color1>/<string:color2>")
def checkerBoard4(width,height,color1,color2):
         return render_template('index.html',width=width,height=height,color1=color1,color2=color2)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)