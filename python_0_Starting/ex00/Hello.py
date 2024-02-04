# Modify the strings in each data object
ft_list = ["Hello", "World!"]
ft_tuple = ("Hello", "France!")
ft_set = {"Hello", "Paris!"}
ft_dict = {"Hello": "42Paris!"}

# Print the modified data objects
if __name__=='__main__':
    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)
    assert ft_list == ["Hello", 'World!']
    assert ft_tuple == ("Hello", 'France!')
    assert ft_set == {'Hello', 'Paris!'}
    assert ft_dict == {'Hello': '42Paris!'}
