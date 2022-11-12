from flask import request, jsonify

from src import app
from src.resources.student_resource import StudentResource
from src.resources.phone_resource import PhoneResource


@app.route("/api/contacts/new_student", methods=['POST'])
def add_new_student():
    data = request.json
    if StudentResource.search_student_by_uni(data['uni']) is not None:
        response = jsonify('Student already exists!')
        response.status_code = 400
        return response

    StudentResource.add_new_student(data['uni'])

    response = jsonify('Successfully added')
    response.status_code = 200
    return response


@app.route("/api/contacts/<uni>/new_address", methods=['POST'])
def add_new_address(uni):
    pass


@app.route("/api/contacts/<uni>/new_phone", methods=['POST'])
def add_new_phone(uni):
    data = request.json

    if StudentResource.search_student_by_uni(uni) is None:
        response = jsonify('Student does not exist!')
        response.status_code = 400
        return response

    type_id = PhoneResource.search_type_id(data["description"])
    if PhoneResource.search_phone_by_type_id_and_uni(type_id, uni) is not None:
        response = jsonify('This phone type already exists for this student!')
        response.status_code = 400
        return response

    PhoneResource.add_new_phone(type_id[0], uni, data["country_code"], data["phone_no"])

    response = jsonify('Successfully added')
    response.status_code = 200
    return response


@app.route("/api/contacts/<uni>/new_email", methods=['POST'])
def add_new_email(uni):
    pass


# Zhengkai
@app.route("/api/contacts/<uni>/all_addresses", methods=['GET'])
def get_all_addresses_of_a_student(uni):
    data = request.json
    return get_all_addresses_of_a_student_helper(uni, data)


def get_all_addresses_of_a_student_helper(uni, data):
    pass


@app.route("/api/contacts/<uni>/all_phones", methods=['GET'])
def get_all_phones_of_a_student(uni):
    pass


@app.route("/api/contacts/<uni>/all_emails", methods=['GET'])
def get_all_emails_of_a_student(uni):
    pass


@app.route("/api/contacts/<uni>/all_contacts", methods=['GET'])
def get_all_contacts_of_a_student(uni):
    pass


# Zhengkai
@app.route("/api/contacts/all_phones", methods=['GET'])
def get_all_addresses_of_all_students():
    pass


@app.route("/api/contacts/all_phones", methods=['GET'])
def get_all_phones_of_all_students():
    pass


@app.route("/api/contacts/all_emails", methods=['GET'])
def get_all_emails_of_all_students():
    pass


@app.route("/api/contacts/all_contacts", methods=['GET'])
def get_all_contacts_of_all_students():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
