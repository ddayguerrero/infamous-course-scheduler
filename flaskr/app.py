from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def login():
    return render_template('home.html')

# returns the main Schedule html page
@app.route("/Schedule/<username>")
def Schedule(username):
	return render_template('schedule.html',name=username)


#returns list of classes in JSON format from sql
@app.route("/classes")
def classes():
	my_people = {'Alice': 25,
		     'Bob': 21,
		     'Charlie': 20,
		     'Doug': 28}
	return jsonify(my_people);

if __name__ == "__main__":
    app.run(debug=True)
