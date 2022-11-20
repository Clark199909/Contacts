from flask import request, jsonify

from src import app
from src.resources.student_resource import StudentResource
from src.resources.phone_resource import PhoneResource
from src.resources.address_resource import AddressResource
from src.resources.email_resource import EmailResource


@app.route("/api/contacts/<uni>/new_address", methods=['POST'])
def add_new_address(uni):
    data = request.json
    if StudentResource.search_student_by_uni(uni) is None:
        response = jsonify('Student does not exist!')
        response.status_code = 400
        return response

    type_id = AddressResource.search_type_id(data["description"])
    if AddressResource.search_address_by_type_id_and_uni(type_id, uni) is not None:
        response = jsonify('This address type already exists for this student!')
        response.status_code = 400
        return response

    AddressResource.add_new_address(type_id[0], uni, data["country"], data["state"], data["city"], data["zip_code"],
                                    data["street"])

    response = jsonify('Successfully added')
    response.status_code = 200
    return response


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
    data = request.json

    if StudentResource.search_student_by_uni(uni) is None:
        response = jsonify('Student does not exist!')
        response.status_code = 400
        return response

    type_id = EmailResource.search_type_id(data["description"])
    if EmailResource.search_email_by_type_id_and_uni(type_id, uni) is not None:
        response = jsonify('This email type already exists for this student!')
        response.status_code = 400
        return response

    EmailResource.add_new_email(type_id[0], uni, data["address"])

    response = jsonify('Successfully added')
    response.status_code = 200
    return response


@app.route("/api/contacts/<uni>/all_addresses", methods=['GET'])
def get_all_addresses_of_a_student(uni):
    addresses = AddressResource.search_all_addresses_of_a_student(uni)

    response = jsonify(addresses)
    response.status_code = 200
    return response


# Zhengkai
@app.route("/api/contacts/<uni>/all_phones", methods=['GET'])
def get_all_phones_of_a_student(uni):
    phones = PhoneResource.search_all_phones_of_a_student(uni)

    response = jsonify(phones)
    response.status_code = 200
    return response


@app.route("/api/contacts/<uni>/all_emails", methods=['GET'])
def get_all_emails_of_a_student(uni):
    emails = EmailResource.search_all_emails_of_a_student(uni)

    response = jsonify(emails)
    response.status_code = 200
    return response


@app.route("/api/contacts/<uni>/all_contacts", methods=['GET'])
def get_all_contacts_of_a_student(uni):
    addresses = AddressResource.search_all_addresses_of_a_student(uni)
    phones = PhoneResource.search_all_phones_of_a_student(uni)
    emails = EmailResource.search_all_emails_of_a_student(uni)

    response = jsonify(addresses, phones, emails)
    response.status_code = 200
    return response


@app.route("/api/contacts/all_addresses", methods=['GET'])
def get_all_addresses_of_all_students():
    addresses = AddressResource.search_all_address_of_all_students()

    response = jsonify(addresses)
    response.status_code = 200
    return response


# Zhengkai
@app.route("/api/contacts/all_phones", methods=['GET'])
def get_all_phones_of_all_students():
    phones = PhoneResource.search_all_phones_of_all_students()

    response = jsonify(phones)
    response.status_code = 200
    return response


@app.route("/api/contacts/all_emails", methods=['GET'])
def get_all_emails_of_all_students():
    emails = EmailResource.search_all_email_of_all_students()

    response = jsonify(emails)
    response.status_code = 200
    return response


@app.route("/api/contacts/all_contacts", methods=['GET'])
def get_all_contacts_of_all_students():
    addresses = AddressResource.search_all_address_of_all_students()
    phones = PhoneResource.search_all_phones_of_all_students()
    emails = EmailResource.search_all_email_of_all_students()

    response = jsonify(addresses, phones, emails)
    response.status_code = 200
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5012)
