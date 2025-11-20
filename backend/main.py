from config import app, db
from flask import jsonify, request
from models import Contact


@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = [contact.to_json() for contact in Contact.query.all()]
    return jsonify({"contacts": contacts})


@app.route("/contacts", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not all((first_name, last_name, email)):
        return jsonify(
            {"message": "You must provide 'firstName', 'lastName', and 'email'."},
        ), 400

    contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(contact)
        db.session.commit()
    except Exception as e:  # noqa: BLE001
        return jsonify({"message": str(e)}, 400)
    else:
        return jsonify({"message": "User created!"}), 201


@app.route("/contacts/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get_or_404(user_id)

    contact.first_name = request.json.get("firstName", contact.first_name)
    contact.last_name = request.json.get("lastName", contact.last_name)
    contact.email = request.json.get("email", contact.email)

    db.session.commit()

    return jsonify({"message": "User updated!"}), 200


@app.route("/contacts/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get_or_404(user_id)

    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted!"}), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
