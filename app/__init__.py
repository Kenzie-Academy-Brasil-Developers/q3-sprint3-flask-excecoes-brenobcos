from http import HTTPStatus
from flask import Flask, jsonify, request


from app.exceptions.user_exc import EmailAlreadyExistsError
from app.services.handler_json import (
    check_unique_email,
    generate_id,
    read_json,
    write_json,
)

app = Flask(__name__)

FILEPATH = "app/database/database.json"


@app.get("/user")
def get_users():
    return jsonify(read_json(FILEPATH)), HTTPStatus.OK


@app.post("/user")
def create_user():
    data = request.get_json()
    key_nome, key_email = data.values()
    nome, email = data.values()
    try:
        if type(nome) == str and type(email) == str:
            check_unique_email(email)
            idUser = generate_id()
            return (
                write_json(
                    FILEPATH,
                    {"nome": nome.title(), "id": idUser, "email": email.lower()},
                ),
                HTTPStatus.CREATED,
            )
        else:
            return {
                "wrong fields": [
                    {"nome": type(key_nome).__name__},
                    {"email": type(key_email).__name__},
                ]
            }, HTTPStatus.BAD_REQUEST
    except EmailAlreadyExistsError as e:
        return {"error": e.message}, e.status_code
