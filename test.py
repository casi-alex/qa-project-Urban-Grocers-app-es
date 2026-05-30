import utilities
import data

def set_card_name(name):
    current_card = data.card.copy()
    current_card["name"] = name
    return current_card

def get_new_user_token():
    user_response = utilities.post_new_user(data.user_body)
    return user_response.json()["authToken"]

def positive_assert(name):
    auth_token = get_new_user_token()
    card = set_card_name(name)
    kit_response = utilities.post_new_client_kit(card, auth_token)
    print(f"Código recibido: {kit_response.status_code}")
    print(f"Respuesta: {kit_response.json()}")
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name

def negative_assert_symbol(name):
    card = set_card_name(name)
    auth_token = get_new_user_token()
    kit_response = utilities.post_new_client_kit(card, auth_token)
    print(f"Código recibido: {kit_response.status_code}")
    print(f"Respuesta: {kit_response.json()}")
    assert kit_response.status_code == 400
    assert kit_response.json()["name"] == name

def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_symbol("")

def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_symbol("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_kit_special_letter_in_name_get_success_response():
    positive_assert("''№%@,")

def test_create_kit_space_in_name_get_success_response():
    positive_assert("A Aaa")

def test_create_kit_string_numbers_in_name_get_success_response():
    positive_assert("123")

def test_create_kit_empty_name_get_error_response():
    negative_assert_symbol(None)

def test_create_kit_numbers_in_name_get_success_response():
    negative_assert_symbol(123)

