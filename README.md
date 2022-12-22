# Contacts
This is a microservice for student contact management. Operations with database are done here.
Please connect to your database before usage in init.py.
## Functionalities and APIs
### Create
- /api/contact/new_student
- /api/contacts/\<uni\>/new_address
- /api/contacts/\<uni\>/new_phone
- /api/contacts/\<uni\>/new_email

### Read
- /api/contacts/\<uni\>/all_addresses
- /api/contacts/\<uni\>/all_phones
- /api/contacts/\<uni\>/all_emails
- /api/contacts/\<uni\>/all_contacts
- /api/contacts/all_addresses
- /api/contacts/all_phones
- /api/contacts/all_emails
- /api/contacts/all_contacts

### Update
- /api/contacts/\<uni\>/update_address
- /api/contacts/\<uni\>/update_phone
- /api/contacts/\<uni\>/update_email

### Delete
- /api/contacts/del_student
- /api/contacts/\<uni\>/del_address
- /api/contacts/\<uni\>/del_phone
- /api/contacts/\<uni\>/del_email

## Running Unit Test