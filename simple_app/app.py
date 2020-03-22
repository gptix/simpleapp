# from flask import Flask, request, jsonify

# def create_app():
#     app = Flask(__name__)

#     @app.route('/recommend', methods=['GET'])
#     def recommended():

#         return jsonify('1PM')

#     return app



from flask import Flask, request, jsonify

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return "Did not crash"

    return app
