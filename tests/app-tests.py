
def test_old_man(client):
    response = client.get(
        "/get-age-by-photo",
        params={
            "url": "https://s1.hostingkartinok.com/uploads/images/2023/12/bed997e1ae3dff00704fffe7aff26df9.jpg",
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        'Age': 'more than 70'}


def test_young_man(client):
    response = client.get(
        "/get-age-by-photo",
        params={
            'url': 'https://family3.ru/wp-content/uploads/2020/02/200217_sad-1024x536.jpg',
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        'Age': '5-10'}

def test_pustoi_query(client):
    response = client.get(
        "/get-age-by-photo",
        params={
            'url': '',
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "Age": "This's not url"}