

@pytest.fixture
def fix():
    user = User("Karina", 18, 7)
    return user

def test1_append(user):
    fix = user

def test2():
    