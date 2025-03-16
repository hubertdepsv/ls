from flask import Flask, render_template, g, redirect, request
import yaml

app = Flask(__name__)

# {
#     'jamy': {
#         'email': 'jamy.rustenburg@gmail.com', 
#         'interests': ['woodworking', 'cooking', 'reading']
#     }, 
#     'nora': {
#         'email': 'nora.alnes@yahoo.com', 
#         'interests': ['cycling', 'basketball', 'economics']
#     }, 
#     'hiroko': {
#         'email': 'hiroko.ohara@hotmail.com', 
#         'interests': []
#     }
# }

def interest_list(interests):
    return ", ".join(interests)

app.jinja_env.filters['interest_list'] = interest_list

def total_interests(users):
    return len(users.keys()), sum(len(users[username]["interests"]) for username in users.keys())

@app.before_request
def load_users():
    with open("users.yaml", "r") as file:
        g.data = yaml.safe_load(file)

@app.errorhandler(404)
def page_not_found(_error):
    return redirect("/")

@app.route("/")
def home():
    return render_template('home.html', 
                        users=g.data)

@app.route("/users/<username>")
def user(username):
    email = g.data[username]["email"]
    interests = g.data[username]["interests"]
    other_users = [user for user in g.data.keys() if username != user]
    return render_template('user.html', 
                    username=username,
                    email=email,
                    interests=interests,
                    other_users=other_users)

if __name__ == "__main__":
    app.run(debug=True, port=5003)