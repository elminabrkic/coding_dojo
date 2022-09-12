from re import X
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def standard_board(row_num = None, col_num = None):
    return render_template('checkerboard.html', row_num = 8, col_num = 8)

@app.route('/<int:x>')
def board_only_row(x, col_num = None):
    return render_template('checkerboard.html', row_num = x, col_num = 8)

@app.route('/<int:x>/<int:y>')
def board_xy(x, y):
    return render_template('checkerboard.html', row_num = x, col_num = y)

if __name__ == "__main__":
    app.run(debug=True)
