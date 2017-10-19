from flask import Flask, render_template, request, redirect
from exam_module import area_cono

app = Flask(__name__)

@app.route('/')
def hello() -> '302':
    return redirect('/entry')

@app.route('/entry')
def entry_page()-> 'html':
    return render_template('entry.html', the_tittle='The Practice of Unity 2')

@app.route('/calculate', methods=['POST'])
def calculate()->'html':
    g = float(request.form['g'])
    R = float(request.form['R'])
    r = float(request.form['r'])
    tittle = 'The result of area of cone is: '
    result = area_cono(g,R,r)
    return render_template('result.html',
                           the_tittle = tittle,
                           the_g = g,
                           the_R = R,
                           the_r = r,
                           the_result = result)

app.run(debug=True)
