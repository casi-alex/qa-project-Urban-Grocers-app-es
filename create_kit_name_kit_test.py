import sender_stand_request
import data

    # Función cambiar name de card
def get_kit_body(name):
    current_card = data.card.copy()
    current_card["name"] = name
    return current_card

    # Función nuevo token
def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    return user_response.json()["authToken"]

    # Función positiva
def positive_assert(name):
    auth_token = get_new_user_token()
    card = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(card, auth_token)
    print(f"Código recibido: {kit_response.status_code}")
    print(f"Respuesta: {kit_response.json()}")
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name

    # Función negativa
def negative_assert_symbol(name):
    card = get_kit_body(name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(card, auth_token)
    print(f"Código recibido: {kit_response.status_code}")
    print(f"Respuesta: {kit_response.json()}")
    assert kit_response.status_code == 400
    assert kit_response.json()["name"] == name

    # Prueba 1:
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")
#test_create_kit_1_letter_in_name_get_success_response()

    # Prueba 2:
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
#test_create_kit_511_letter_in_name_get_success_response()

    # Prueba 3:
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_symbol("")
#test_create_kit_0_letter_in_name_get_error_response()

    # Prueba 4:
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_symbol("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
#test_create_kit_512_letter_in_name_get_error_response()

    #Prueba 5:
def test_create_kit_special_letter_in_name_get_success_response():
    positive_assert("''№%@,")

    # Prueba 6:
def test_create_kit_space_in_name_get_success_response():
    positive_assert("A Aaa")
#test_create_kit_space_in_name_get_success_response()

    # Prueba 7:
def test_create_kit_string_numbers_in_name_get_success_response():
    positive_assert("123")
#test_create_kit_numbers_in_name_get_success_response()

    # Prueba 8:
def test_create_kit_empty_name_get_error_response():
    negative_assert_symbol(None)
#test_create_kit_empty_name_get_error_response()

    #Prueba 9:
def test_create_kit_numbers_in_name_get_success_response():
    negative_assert_symbol(123)
#test_create_kit_empty_name_get_error_response()

