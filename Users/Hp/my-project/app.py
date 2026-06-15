from flask import flask, jsonify
app= FLSK(__name__)
@app.route('/health')
def health();
return jsonify({"status"; "healthy","version":"1.0"})
if __name__=='__main__';
app.run(debug=true)
@app.route('/version')
def version();
rerturn jsonify({"version": "1.0.0"})
@app.route('/login' , methods={'POST'})
def login ():
return {"message": "login incorrect"}

