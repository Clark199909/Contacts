from flask import request, jsonify

from src import app
from src.resources.student_resource import StudentResource
from src.resources.phone_resource import PhoneResource
from src.resources.address_resource import AddressResource
from src.resources.email_resource import EmailResource


@app.route("/api/contacts/new_student", methods=['POST'])
def add_new_student():
    """JSON copy to test on Postman
    {
        "uni": "dw3013"
    }
    """
    data = request.json
    if StudentResource.search_student_by_uni(data['uni']) is not None:
        response = jsonify('Student already exists!')
        response.status_code = 400
        return response

    StudentResource.add_new_student(data['uni'])

    response = jsonify('Successfully added')
    response.status_code = 200
    return response


@app.route("/api/contacts/del_student/<uni>", methods=['DELETE'])
def del_a_student(uni):

    if StudentResource.search_student_by_uni(uni) is None:
        response = jsonify('Student does not exist!')
        response.status_code = 400
        return response

    AddressResource.del_all_addresses_of_a_student(uni)
    PhoneResource.del_all_phones_of_a_student(uni)
    EmailResource.del_all_emails_of_a_student(uni)
    StudentResource.del_a_student(uni)

    response = jsonify('Successfully deleted')
    response.status_code = 200
    return response


@app.route("/api/contacts/<uni>/new_address", methods=['POST'])
def add_new_address(uni):
    """JSON copy to test on Postman
    {
        "description": "home",
        "country": "USA",
        "state": "NY",
        "city": "NY",
        "zip_code": "10025",
        "street": "125W 109th St"
    }
    """
    data = request.json
    if StudentResource.search_student_by_uni(uni) is None:
        response = jsonify('Student does not exist!')
        response.status_code = 400
        return response

    type_id = AddressResource.search_type_id(data["description"])
    if AddressResource.search_address_by_type_id_and_uni(type_id[0], uni) is not None:
        response = jsonify('This address type already exists for this student!')
        response.status_code = 400
        return response

    AddressResource.add_new_address(type_id[0], uni, data["country"], data["state"], data["city"], data["zip_code"],
                                    data["street"])

    response = jsonify('Successfully added')
    response.status_code = 200
    return response


@app.route("/api/contacts/<uni>/del_address/<note>", methods=['DELETE'])
def del_an_address(uni, note):
    """ JSON copy to test on Postman
    {
        "description": "home"
    }
    """

    if StudentResource.search_student_by_uni(uni) is None:
        response = jsonify('Student does not exist!')
        response.status_code = 400
        return response

    type_id = AddressResource.search_type_id(note)
    if AddressResource.search_address_by_type_id_and_uni(type_id[0], uni) is None:
        response = jsonify('This address does not exist for this student!')
        response.status_code = 400
        return response

    AddressResource.del_an_address_by_uni_and_type(type_id[0], uni)

    response = jsonify('Successfully deleted')
    response.status_code = 200
    return response


@app.route("/api/contacts/<uni>/update_address", methods=['PUT'])
def update_an_address(uni):
    """ JSON copy to test on Postman
    {
        "description": "home",
        "country": "USA",
        "state": "NY",
        "city": "NY",
        "zip_code": "10026",
        "street": "125W 109th St"
    }
    """
    data = request.json
    if StudentResource.search_student_by_uni(uni) is None:
        response = jsonify('Student does not exist!')
        response.status_code = 400
        return response

    type_id = AddressResource.search_type_id(data["description"])

    if AddressResource.search_address_by_type_id_and_uni(type_id[0], uni) is None:
        response = jsonify('This address does not exist for this student!')
        response.status_code = 400
        return response

    AddressResource.update_an_address_by_uni_and_type(type_id[0], uni, data["country"], data["state"], data["city"],
                                                      data["zip_code"], data["street"])

    response = jsonify('Successfully updated')
    response.status_code = 200
    return response


@app.route("/api/contacts/<uni>/new_phone", methods=['POST'])
def add_new_phone(uni):
    """JSON copy to test on Postman
    {
        "description": "mobile",
        "country_code": "1",
        "phone_no": "3476290991"
    }
    """
    data = request.json

    if StudentResource.search_student_by_uni(uni) is None:
        response = jsonify('Student does not exist!')
        response.status_code = 400
        return response

    type_id = PhoneResource.search_type_id(data["description"])
    if PhoneResource.search_phone_by_type_id_and_uni(type_id[0], uni) is not None:
        response = jsonify('This phone type already exists for this student!')
        response.status_code = 400
        return response

    PhoneResource.add_new_phone(type_id[0], uni, data["country_code"], data["phone_no"])

    response = jsonify('Successfully added')
    response.status_code = 200
    return response


@app.route("/api/contacts/<uni>/del_phone/<note>", methods=['DELETE'])
def del_a_phone(uni, note):
    """ JSON copy to test on Postman
    {
        "description": "mobile"
    }
    """
    if StudentResource.search_student_by_uni(uni) is None:
        response = jsonify('Student does not exist!')
        response.status_code = 400
        return response

    type_id = PhoneResource.search_type_id(note)
    if PhoneResource.search_phone_by_type_id_and_uni(type_id[0], uni) is None:
        response = jsonify('This phone does not exist for this student!')
        response.status_code = 400
        return response

    PhoneResource.del_a_phone_by_uni_and_type(type_id[0], uni)

    response = jsonify('Successfully deleted')
    response.status_code = 200
    return response


@app.route("/api/contacts/<uni>/update_phone", methods=['PUT'])
def update_a_phone(uni):
    """ JSON copy to test on Postman
    {
        "description": "mobile",
        "country_code": "1",
        "phone_no": "1234567890"
    }
    """
    data = request.json
    if StudentResource.search_student_by_uni(uni) is None:
        response = jsonify('Student does not exist!')
        response.status_code = 400
        return response

    type_id = PhoneResource.search_type_id(data["description"])

    if PhoneResource.search_phone_by_type_id_and_uni(type_id[0], uni) is None:
        response = jsonify('This phone does not exist for this student!')
        response.status_code = 400
        return response

    PhoneResource.update_a_phone_by_uni_and_type(type_id[0], uni, data["country_code"], data["phone_no"])

    response = jsonify('Successfully updated')
    response.status_code = 200
    return response


@app.route("/api/contacts/<uni>/new_email", methods=['POST'])
def add_new_email(uni):
    """JSON copy to test on Postman
    {
        "description": "personal",
        "address": "dw3013@columbia.edu"
    }
    """
    data = request.json

    if StudentResource.search_student_by_uni(uni) is None:
        response = jsonify('Student does not exist!')
        response.status_code = 400
        return response

    type_id = EmailResource.search_type_id(data["description"])
    if EmailResource.search_email_by_type_id_and_uni(type_id[0], uni) is not None:
        response = jsonify('This email type already exists for this student!')
        response.status_code = 400
        return response

    EmailResource.add_new_email(type_id[0], uni, data["address"])

    response = jsonify('Successfully added')
    response.status_code = 200
    return response


@app.route("/api/contacts/<uni>/del_email/<note>", methods=['DELETE'])
def del_an_email(uni, note):
    """ JSON copy to test on Postman
    {
        "description": "personal"
    }
    """
    if StudentResource.search_student_by_uni(uni) is None:
        response = jsonify('Student does not exist!')
        response.status_code = 400
        return response

    type_id = EmailResource.search_type_id(note)

    if EmailResource.search_email_by_type_id_and_uni(type_id[0], uni) is None:
        response = jsonify('This email does not exist for this student!')
        response.status_code = 400
        return response

    EmailResource.del_an_email_by_uni_and_type(type_id[0], uni)

    response = jsonify('Successfully deleted')
    response.status_code = 200
    return response


@app.route("/api/contacts/<uni>/update_email", methods=['PUT'])
def update_an_email(uni):
    """ JSON copy to test on Postman
    {
        "description": "personal",
        "address": "12345678@columbia.edu"
    }
    """
    data = request.json
    if StudentResource.search_student_by_uni(uni) is None:
        response = jsonify('Student does not exist!')
        response.status_code = 400
        return response

    type_id = EmailResource.search_type_id(data["description"])

    if EmailResource.search_email_by_type_id_and_uni(type_id[0], uni) is None:
        response = jsonify('This email does not exist for this student!')
        response.status_code = 400
        return response

    EmailResource.update_an_email_by_uni_and_type(type_id[0], uni, data['address'])

    response = jsonify('Successfully updated')
    response.status_code = 200
    return response


@app.route("/api/contacts/<uni>/all_addresses", methods=['GET'])
def get_all_addresses_of_a_student(uni):
    """response body be like
    [
        {
            "address_type": "home",
            "city": "NY",
            "country": "USA",
            "id": 1,
            "state": "NY",
            "street": "125W 109th St",
            "uni": "dw3013",
            "zip_code": "10025"
        },
        {
           (second address)
        }
    ]
    """
    addresses = AddressResource.search_all_addresses_of_a_student(uni)

    response = jsonify(addresses)
    response.status_code = 200
    return response


# Zhengkai
@app.route("/api/contacts/<uni>/all_phones", methods=['GET'])
def get_all_phones_of_a_student(uni):
    """response body be like
    [
        {
            "country_code": "1",
            "id": 1,
            "phone_no": "3476290991",
            "phone_type": "mobile",
            "uni": "dw3013"
        },
        {
           (second phone)
        }
    ]
    """
    phones = PhoneResource.search_all_phones_of_a_student(uni)

    response = jsonify(phones)
    response.status_code = 200
    return response


@app.route("/api/contacts/<uni>/all_emails", methods=['GET'])
def get_all_emails_of_a_student(uni):
    """response body be like
    [
        {
            "address": "dw3013@columbia.edu",
            "email_type": "personal",
            "id": 1,
            "uni": "dw3013"
        },
        {
           (second email)
        }
    ]
    """
    emails = EmailResource.search_all_emails_of_a_student(uni)

    response = jsonify(emails)
    response.status_code = 200
    return response


@app.route("/api/contacts/<uni>/all_contacts", methods=['GET'])
def get_all_contacts_of_a_student(uni):
    """response body be like
    [
        # all addresses
        [
            { (address1)},{(address2)},{(address3)}
        ],
        # all phones
        [
            { (phone1)},{(phone2)},{(phone3)}
        ]
        # all emails
        [
            { (email1)},{(email2)},{(email3)}
        ]
    ]
    """
    addresses = AddressResource.search_all_addresses_of_a_student(uni)
    phones = PhoneResource.search_all_phones_of_a_student(uni)
    emails = EmailResource.search_all_emails_of_a_student(uni)

    response = jsonify(addresses, phones, emails)
    response.status_code = 200
    return response


@app.route("/api/contacts/all_addresses", methods=['GET'])
def get_all_addresses_of_all_students():
    """response body be like
    [
        { (address1)},{(address2)},{(address3)}
    ]
    """
    addresses = AddressResource.search_all_address_of_all_students()

    response = jsonify(addresses)
    response.status_code = 200
    return response


# Zhengkai
@app.route("/api/contacts/all_phones", methods=['GET'])
def get_all_phones_of_all_students():
    """response body be like
    [
        { (phone1)},{(phone2)},{(phone3)}
    ]
    """
    phones = PhoneResource.search_all_phones_of_all_students()

    response = jsonify(phones)
    response.status_code = 200
    return response


@app.route("/api/contacts/all_emails", methods=['GET'])
def get_all_emails_of_all_students():
    """response body be like
    [
        { (email1)},{(email2)},{(email3)}
    ]
    """
    emails = EmailResource.search_all_email_of_all_students()

    response = jsonify(emails)
    response.status_code = 200
    return response


@app.route("/api/contacts/all_contacts", methods=['GET'])
def get_all_contacts_of_all_students():
    """response body be like
    [
        # all addresses
        [
            { (address1)},{(address2)},{(address3)}
        ],
        # all phones
        [
            { (phone1)},{(phone2)},{(phone3)}
        ]
        # all emails
        [
            { (email1)},{(email2)},{(email3)}
        ]
    ]
    """
    addresses = AddressResource.search_all_address_of_all_students()
    phones = PhoneResource.search_all_phones_of_all_students()
    emails = EmailResource.search_all_email_of_all_students()

    response = jsonify(addresses, phones, emails)
    response.status_code = 200
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5014)
