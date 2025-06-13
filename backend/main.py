from flask import request, jsonify
from config import app, db
from models import Contact
from sqlalchemy.exc import SQLAlchemyError
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

@app.route("/contacts", methods=["GET"])
def get_contacts():
    try:
        contacts = Contact.query.all()
        json_contacts = list(map(lambda x: x.to_json(), contacts))
        return jsonify({"contacts": json_contacts, "status": "success"}), 200
    except Exception as e:
        return jsonify({"message": "Error fetching contacts", "error": str(e)}), 500

@app.route("/create_contact", methods=["POST"])
def create_contact():
    try:
        data = request.json
        first_name = data.get("firstName", "").strip()
        last_name = data.get("lastName", "").strip()
        email = data.get("email", "").strip()

        if not all([first_name, last_name, email]):
            return jsonify({
                "message": "Semua field (firstName, lastName, email) harus diisi",
                "status": "error"
            }), 400

        if not validate_email(email):
            return jsonify({
                "message": "Format email tidak valid",
                "status": "error"
            }), 400

        if Contact.query.filter_by(email=email).first():
            return jsonify({
                "message": "Email sudah terdaftar",
                "status": "error"
            }), 400

        new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
        db.session.add(new_contact)
        db.session.commit()

        return jsonify({
            "message": "Kontak berhasil dibuat",
            "contact": new_contact.to_json(),
            "status": "success"
        }), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({
            "message": "Database error",
            "error": str(e),
            "status": "error"
        }), 500
    except Exception as e:
        return jsonify({
            "message": "Terjadi kesalahan",
            "error": str(e),
            "status": "error"
        }), 500

@app.route("/update_contact/<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    try:
        contact = Contact.query.get(user_id)
        if not contact:
            return jsonify({
                "message": "Kontak tidak ditemukan",
                "status": "error"
            }), 404

        data = request.json
        if "email" in data and data["email"] != contact.email:
            if not validate_email(data["email"]):
                return jsonify({
                    "message": "Format email tidak valid",
                    "status": "error"
                }), 400
            if Contact.query.filter_by(email=data["email"]).first():
                return jsonify({
                    "message": "Email sudah terdaftar",
                    "status": "error"
                }), 400

        contact.first_name = data.get("firstName", contact.first_name).strip()
        contact.last_name = data.get("lastName", contact.last_name).strip()
        contact.email = data.get("email", contact.email).strip()

        db.session.commit()

        return jsonify({
            "message": "Kontak berhasil diperbarui",
            "contact": contact.to_json(),
            "status": "success"
        }), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({
            "message": "Database error",
            "error": str(e),
            "status": "error"
        }), 500
    except Exception as e:
        return jsonify({
            "message": "Terjadi kesalahan",
            "error": str(e),
            "status": "error"
        }), 500

@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    try:
        contact = Contact.query.get(user_id)
        if not contact:
            return jsonify({
                "message": "Kontak tidak ditemukan",
                "status": "error"
            }), 404

        db.session.delete(contact)
        db.session.commit()

        return jsonify({
            "message": "Kontak berhasil dihapus",
            "status": "success"
        }), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({
            "message": "Database error",
            "error": str(e),
            "status": "error"
        }), 500
    except Exception as e:
        return jsonify({
            "message": "Terjadi kesalahan",
            "error": str(e),
            "status": "error"
        }), 500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
