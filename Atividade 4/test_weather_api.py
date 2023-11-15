import pytest

from weather_api import get_weather_data

def test_get_weather_data():
    api_key = "d1a60b029f36bb0ca25230acee600c60"
    city = "Rio de Janeiro"
    result = get_weather_data(api_key, city)
    assert result is not None


if __name__ == '__main__':
    test_get_weather_data()
    print("Todos os testes passaram!")