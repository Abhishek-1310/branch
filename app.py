from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route("/math", methods=['POST'])
def math_ops():
    if(request.method=='POST'):
        ops=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        if(ops=='add'):
            r=num1+num2
            res='The sum of  '+str(num1)+' and '+str(num2)+' is:-'+str(r)
            return render_template('result.html',result=res)
        if(ops=='subtract'):
            r=num1-num2
            res='The subtract of  '+str(num1)+' and '+str(num2)+' is:-'+str(r)
            return render_template('result.html',result=res)
        if(ops=='multiply'):
            r=num1*num2
            res='The multiply of  '+str(num1)+' and '+str(num2)+' is:-'+str(r)
            return render_template('result.html',result=res)
        if(ops=='divide'):
            r=num1/num2
            res='The divide of  '+str(num1)+' and '+str(num2)+' is:-'+str(r)
            return render_template('result.html',result=res)
        if(ops=='log'):
            r=num1%num2
            res='The reminder of  '+str(num1)+' and '+str(num2)+' is:-'+str(r)
            return render_template('result.html',result=res)

@app.route("/postman_data", methods=['POST'])
def math_ops1():
    if(request.method=='POST'):
        ops=request.json['operation']
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])
        if(ops=='add'):
            r=num1+num2
            res='The sum of  '+str(num1)+' and '+str(num2)+' is:-'+str(r)
            
        if(ops=='subtract'):
            r=num1-num2
            res='The subtract of  '+str(num1)+' and '+str(num2)+' is:-'+str(r)
            
        if(ops=='multiply'):
            r=num1*num2
            res='The multiply of  '+str(num1)+' and '+str(num2)+' is:-'+str(r)
            
        if(ops=='divide'):
            r=num1/num2
            res='The divide of  '+str(num1)+' and '+str(num2)+' is:-'+str(r)
            
        if(ops=='log'):
            r=num1%num2
            res='The reminder of  '+str(num1)+' and '+str(num2)+' is:-'+str(r)
        
        return jsonify(res)

if __name__=="__main__":
    app.run(host="0.0.0.0")
