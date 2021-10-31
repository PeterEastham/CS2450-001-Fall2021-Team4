#Gets all the Properties of a Class, Coverts it to a CSV, and returns that string.
def class_csv_headers(object):
    properties = ""
    for property in object.__dict__.keys():
        properties += property
        properties += ","

    return properties[:-1] + "\n"



header_to_version = {
    "add_screen" : "add_screen",
    "ID,Name,Address,City,State,Zip,Classification,PayMethod,Salary,Hourly,Commission,Route,Account" : "emp_1.0",
    "id,first_name,last_name,archived,social_security,title,department,office_email,office_phone,start_date,imported,street_address,city,state,zipcode,classification,payment_Method,salary,rate,route,account,valid" : "emp_1.3"
}
