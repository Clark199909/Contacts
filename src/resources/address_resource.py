from src import db
from src.models.address import Address
from src.models.address_type import AddressType
from src.models.student import Student


class AddressResource:
    def __int__(self):
        pass

    @staticmethod
    def add_new_address(type_id, uni, country, state, city, zip_code, street):
        address = Address(type_id=type_id, uni=uni, country=country, state=state, city=city, zip_code=zip_code,
                          street=street)
        db.session.add(address)
        db.session.commit()

    @staticmethod
    def search_address_by_type_id_and_uni(type_id, uni):
        return db.session.query(Address).filter_by(type_id=type_id, uni=uni).first()

    @staticmethod
    def search_type_id(description):
        return db.session.query(AddressType.id).filter_by(description=description).first()

    @staticmethod
    def search_all_addresses_of_a_student(uni):
        res = db.session.query(Student).filter_by(uni=uni).first()
        if res is None:
            return {}

        addresses = res.addresses
        address_list = []
        AddressResource.parse_address_info(addresses, address_list)
        return address_list

    @staticmethod
    def search_all_address_of_all_students():
        students = db.session.query(Student).all()

        address_list = []
        for student in students:
            addresses = student.addresses
            AddressResource.parse_address_info(addresses, address_list)

        return address_list

    @staticmethod
    def parse_address_info(addresses, address_list):

        for address in addresses:
            address_dict = {'id': address.id,
                            'uni': address.uni,
                            'country': address.country,
                            'state': address.state,
                            'city': address.city,
                            'zip_code': address.zip_code,
                            'street': address.street,
                            'address_type': address.address_type.description}
            address_list.append(address_dict)
