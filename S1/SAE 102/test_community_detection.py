network = {
  "Alice" : ["Bob", "Dominique"],
  "Bob" : ["Alice", "Dominique", "Charlie"],
  "Charlie" : ["Bob"],
  "Dominique" : ["Bob", "Alice"]}

def test_create_network():
    assert create_network(["Alice", "Bob", "Alice", "Charlie", "Bob", "Charlie"]) == {"Alice": ["Bob", "Charlie"],
        "Bob": ["Alice", "Charlie"],
        "Charlie": ["Alice", "Bob"]}
    assert create_network(["Alice", "John", "John", "Charlie", "Charlie", "Alice"]) == {"Alice": ["John", "Charlie"],"John": ["Alice", "Charlie"],"Charlie": ["John", "Alice"]}
    assert create_network(["Alice", "Bob"]) == {"Alice": ["Bob"],"Bob": ["Alice"]}
    assert create_network([]) == {}
    print("Test de la fonction create_network ok !")

def test_get_people():
    assert get_people({"Alice": ["Bob", "Charlie", "Dominique"],"Bob": ["Alice", "Charlie"],"Charlie": ["Alice", "Bob"],"Dominique": ["Alice"]}) == ["Alice","Bob","Charlie","Dominique"]
    assert get_people({"Alice": ["Bob", "Charlie", "Dominique"],"Bob": ["Alice", "Charlie"]}) == ["Alice", "Bob"]
    assert get_people({}) == []
    print("Test de la fonction get_people ok !")

def test_are_friends():
    assert are_friends(network, "Alice", "Bob") == True
    assert are_friends(network, "Alice", "Charlie") == False
    assert are_friends(network, "Charlie", "Dominique") == False
    assert are_friends(network, "Bob", "Dominique") == True
    print("Test de la fonction are_friends ok !")

def test_all_his_friends():
    assert all_his_friends(network, "Alice", ["Bob", "Dominique"]) == True
    assert all_his_friends(network, "Alice", ["Bob", "Charlie"]) == False
    print("Test de la fonction all_his_friends ok !")

def test_is_a_community():
    assert is_a_community(network,["Alice", "Bob", "Dominique"]) == True
    assert is_a_community(network,["Alice", "Bob", "Charlie"]) == False
    print("Test de la fonction is_a_community ok!")

def test_find_community():
    assert find_community(network,["Alice", "Bob", "Charlie", "Dominique"]) == ["Alice", "Bob", "Dominique"]
    assert find_community(network,["Charlie", "Alice", "Bob", "Dominique"]) == ["Charlie", "Bob"]
    assert find_community(network,["Charlie", "Alice", "Dominique"]) == ["Charlie"]
    print("Test de la fonction find_community ok!")

def test_order_by_decreasing_popularity():
    assert order_by_decreasing_popularity(network, ["Alice", "Bob", "Charlie"]) == ["Bob", "Alice", "Charlie"]
    assert order_by_decreasing_popularity(network, ["Alice", "Charlie"]) == ["Alice", "Charlie"]
    assert order_by_decreasing_popularity(network, ["Charlie", "Bob"]) == ["Bob", "Charlie"]
    print("Test de la fonction order_by_decreasing_popularity ok!")

def test_find_community_by_decreasing_popularity():
    assert test_find_community_by_decreasing_popularity(network) == ["Bob", "Alice", "Dominique"]
    print("Test de la fonction find_community_by_decreasing_popularity ok!")

def test_find_community_from_person():
    assert find_community_from_person(network, "Alice") == ["Alice", "Bob", "Dominique"]
    assert find_community_from_person(network, "Charlie") == ["Charlie", "Bob"]
    print("Test de la fonction test_find_community_from_person ok!")

def test_find_max_community():
    assert find_max_community(network) == ["Alice", "Bob", "Dominique"]
    print("Test de la fonction find_max_community ok!")
