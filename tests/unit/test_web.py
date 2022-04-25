import time

def test_index_route(app, client):

    print("\r")
    print(" -- / GET test")
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b"Welcome to VTM!" in res.data


def test_about_route(app, client):
  
    print("-- /about GET test")
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200
        assert b"About Vertical Tank Maintenance" in res.data


def test_estimate_route(app, client):

    print("-- /estimate GET test")
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 200
        #assert res.headers["Location"] == "/estimate"

def test_estimate_functionality(app, client):

    print("-- /estimate POST test")
    with app.test_client() as test_client:
        size = {"radius":180, "height":360}
        res = test_client.post('estimate', data=size)
        assert res.status_code == 200
