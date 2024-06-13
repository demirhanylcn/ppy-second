import pytest
from io import BytesIO
from spell import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'<h1><i class="fas fa-spell-check" style="color: #007bff;"></i> Spell Checker</h1>' in rv.data

def test_no_file_selected(client):
    rv = client.post('/check_spell', data={})
    assert rv.status_code == 200
    assert b'No file part' in rv.data

def test_spellcheck(client, monkeypatch):
    def mock_spellcheck_text(text):
        return "This is a corrected text.", 1

    monkeypatch.setattr('spell.spellcheck_text', mock_spellcheck_text)

    data = {
        'file': (BytesIO(b'This is a testt.'), 'test.txt')
    }
    rv = client.post('/check_spell', content_type='multipart/form-data', data=data)
    assert rv.status_code == 200
    assert b'This is a corrected text.' in rv.data

if __name__ == '__main__':
    pytest.main()
