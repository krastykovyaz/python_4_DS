from DiamondTrap import King

def main():
    """
    Main function to instantiate King Joffrey and modify his attributes.
    """
    joffrey = instantiate_joffrey()
    print(joffrey.__dict__)
    modify_joffrey_attributes(joffrey)
    print(joffrey.get_eyes())
    print(joffrey.get_hairs())
    print(joffrey.__dict__)

def instantiate_joffrey():
    """
    Instantiate King Joffrey with default attributes.
    """
    return King("Joffrey")

def modify_joffrey_attributes(joffrey):
    """
    Modify King Joffrey's attributes.
    """
    joffrey.set_eyes("blue")
    joffrey.set_hairs("light")

if __name__ == "__main__":
    main()
