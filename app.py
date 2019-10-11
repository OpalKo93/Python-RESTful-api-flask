from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from arithmetic import sum_strings, mul_strings

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
#     maybe showing the README file
    return "index"


class Sum(Resource):
    def get(self):
        args = request.args
        num1 = args["num1"]
        num2 = args["num2"]
        try:
            result = sum_strings(num1, num2)
            return jsonify(dict(data=[num1, num2], result=result))
        except Exception as error:
            return jsonify({"error": str(error)})


class Mul(Resource):
    def get(self):
        args = request.args
        num1 = args["num1"]
        num2 = args["num2"]
        try:
            result = mul_strings(num1, num2)
            return jsonify(dict(data=[num1, num2], result=result))
        except Exception as error:
            return jsonify({"error": str(error)})


api.add_resource(Sum, "/sum")
api.add_resource(Mul, "/mul")

if __name__ == '__main__':
    app.run()
