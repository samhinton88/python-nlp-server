from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import engine


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    print(request.args.get('text'))
    data = engine.parse(request.args.get('text'))

    res = {
      "data": [[ent.text, ent.start_char, ent.end_char, ent.label_] for ent in data.ents],
      "token": [[token.text, token.pos_, token.dep_] for token in data]
    }
    print(res)
    response = jsonify(res)
    response.status_code = 200
    response.headers['Content-Type'] = 'application/json'


    return response
