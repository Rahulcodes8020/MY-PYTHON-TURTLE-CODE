def generate_certificate(login_name):
    certificate_text = f"""
    ******************************************************
    *                                                    *
    *            Bajrang Dal Army Certificate             *
    *                                                    *
    ******************************************************

    This is to certify that

                      {login_name}

    is a proud member of the Bajrang Dal Army.

    Given on this day with honor and respect.

    ******************************************************
    """
    return certificate_text

def main():
    print("Welcome to Bajrang Dal Army Certificate Generator")
    login_name = input("Please enter your login name: ").strip()

    if not login_name:
        print("Error: Login name cannot be empty.")
        return

    certificate = generate_certificate(login_name)
    print("\n" + certificate)

    filename = f"certificate_{login_name.replace(' ', '_')}.txt"
    with open(filename, "w") as f:
        f.write(certificate)
    print(f"Certificate saved as '{filename}'")

if __name__ == "__main__":
    main()
