import sqlite3
import flask

app = flask.Flask(__name__)

def get_user_info(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Vulnerable SQL query
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()

    return result

@app.route('/')
def index():
    user_id = flask.request.args.get('user_id')
    user_info = get_user_info(user_id)
    return f"User information: {user_info}"

if __name__ == '__main__':
    app.run(debug=True)