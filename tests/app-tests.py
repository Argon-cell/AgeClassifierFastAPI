
def test_old_man(client):
    response = client.get(
        "/get-age-by-photo",
        params={
            'url': 'https://static01.nyt.com/images/2022/06/16/arts/16OLD-MAN1/16OLD-MAN1-mediumSquareAt3X-v3.jpg',
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
        'Age': '3-9'}

def test_pustoi_query(client):
    response = client.get(
        "/get-age-by-photo",
        params={
            'url': '',
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        'Age': 'This is not url'}