from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/conta')
def conta():
    n1 = float(request.args.get('valor1',0))
    n2 = float(request.args.get('valor2',0))

    conta = n1 + n2 

    return {
            
            'Resultado': conta
            
        }

@app.route('/conta2')
def conta2():
    n1 = float(request.args.get('valor1',0))
    n2 = float(request.args.get('valor2',0))

    conta2 = n1 - n2 

    return {
            
           'Resultado': conta2
        }

@app.route('/conta3')
def conta3():
    n1 = float(request.args.get('valor1',0))
    n2 = float(request.args.get('valor2',0))

    conta3 = n1 * n2 

    return {
            
           'Resultado': conta3
            
        }

@app.route('/conta4')
def conta4():
    n1 = float(request.args.get('valor1',0))
    n2 = float(request.args.get('valor2',0))

    conta4 = n1 / n2 

    return {
            
            'Resultado': conta4
            
        }




if __name__ == '__main__':
    app.run(debug =True)
