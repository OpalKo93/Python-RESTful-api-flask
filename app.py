import markdown
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from arithmetic import sum_strings, mul_strings


app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    with open('README.md', 'r') as markdown_file:
        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)


class Sum(Resource):
    def post(self):
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        try:
            result = sum_strings(num1, num2)
            return jsonify(dict(data=[num1, num2], result=result))
        except Exception as error:
            return jsonify({"error": str(error)})


class Mul(Resource):
    def post(self):
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        try:
            result = mul_strings(num1, num2)
            return jsonify(dict(data=[num1, num2], result=result))
        except Exception as error:
            return jsonify({"error": str(error)})


api.add_resource(Sum, "/sum")
api.add_resource(Mul, "/mul")

if __name__ == '__main__':
    app.run()
