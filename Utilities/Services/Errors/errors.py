from flask import Flask, jsonify, make_response

def custom_error(message, status_code): 
    return make_response(jsonify(message), status_code)

if __name__ == "__main__":
    custom_error()