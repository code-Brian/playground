from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')  # Return the index file as a response

@app.route('/play/<int:num>/<string:color>')          
def play(num, color):
    return render_template('play.html', num = num, color = color)  # This will display the passed in amount of divs.

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

