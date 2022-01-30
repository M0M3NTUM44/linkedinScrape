import pip
try:
    module = "linkedin-api~=2.0.0a"
    __import__("linkedin_api")
    module = "beautifulsoup4"
    __import__("bs4")
    module = "requests"
    __import__(module)

except ImportError as e:
    print(e)
    pip.main(['install', module])


from linkedin_api import Linkedin


def print_all_employees(api, company):
    print("[+] Searching...It may take a while")
    print("[!!] Keep in mind that due to LinkedIn's privacy reasons i cannot show all of the profiles.")
    print("----------------------------------------")
    employees = api.search_people(current_company=company)
    for i in range(len(employees)):
        employee = api.get_profile(public_id=employees[i]['public_id'])
        print(f"[{i+1}] First Name: {employee.get('firstName')}")
        print(f"[+] Last Name: {employee.get('lastName')}")
        print(f"[+] Location: {employee.get('locationName')}")
        print(f"[+] Is Student: {employee.get('student')}")
        print(f"[+] HeadLine: {employee.get('headline')}")
        print(f"[+] Summary: {employee.get('summary')}")
        print(f"[+] Profile Link: https://www.linkedin.com/in/{employees[i].get('public_id')}")
        print("----------------------------------------")


def search_company(api, keyword):
    print("[+] Searching...It may take a while")
    print("----------------------------------------")
    companies = api.search_companies(keywords=keyword)
    for i in range(len(companies)):
        company = api.get_company(public_id=companies[i]['urn_id'])
        try:
            print(f"\n[{i + 1}] Company Name: {company.get('name')}")
            print(f"[+] Location: {dict(company.get('headquarter')).get('city')} {dict(company.get('headquarter')).get('geographicArea')}, {dict(company.get('headquarter')).get('country')}")
            print(f"[+] URL: {company.get('companyPageUrl')}")
            print(f"[+] Numbers of employees: {company.get('staffCount')}")
            print(f"[+] description: {company.get('description')}")
        except:
            print("[!] Error getting details")
        finally:
            print("------------------------------------------------------")
    print("\n[?] Which company do you want to gather all of its employees? (0 for none)\n")
    choice = input("choice> ")
    while not choice.isnumeric():
        print("\n[!] Invalid choice. Choose again.\n")
        choice = input("choice> ")

    choice = int(choice)
    while choice < 0 and choice > len(companies):
        print("\n[!] Invalid choice. Choose again.\n")
        choice = input("choice> ")

    if choice > 0:
        print_all_employees(api, [companies[choice-1]['urn_id']])


def search_user(api, keyword):
    print("[+] Searching...It may take a while")
    print("----------------------------------------")
    users = api.search_people(keywords=keyword)
    for i in range(len(users)):
        user = api.get_profile(public_id=users[i]['public_id'])
        print(f"[{i+1}] First Name: {user.get('firstName')}")
        print(f"[+] Last Name: {user.get('lastName')}")
        print(f"[+] Location: {user.get('locationName')}")
        print(f"[+] Is Student: {user.get('student')}")
        print(f"[+] HeadLine: {user.get('headline')}")
        print(f"[+] Summary: {user.get('summary')}")
        print(f"[+] Profile Link: https://www.linkedin.com/in/{users[i].get('public_id')}")
        print("----------------------------------------")


def main():
    print("[+] Welcome to LinkedIn enumeration tool.\n")

    # Authenticate using any Linkedin account credentials
    print("[?] Authenticating")
    api = Linkedin(username='pythonsender123@gmail.com', password='PythonScript123')
    print("[+] Authenticated\n")

    print("What do you want to search?\n")
    print("[?] For users search, press 1\n[?] For companies search, press 2\n")
    choice = input("choice> ")
    while choice != "1" and choice != "2":
        print("\n[!] Invalid choice. Choose again.\n")
        choice = input("choice> ")

    if choice == "1":
        search = input("Please enter user to search for:")
        search_user(api,search)

    elif choice == "2":
        search = input("Please enter company to search for:")
        search_company(api, search)


if __name__ == '__main__':
    main()
