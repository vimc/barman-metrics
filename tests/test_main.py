from datetime import datetime, timedelta
from app.app.main import parse_status, metrics
import app


def create_mock_data(timestamp):
    return {
        "utc_seconds": round(timestamp),
        "data": {
            "some_metrics": 32178
        }
    }


def test_endpoint_labels_metrics(monkeypatch):
    timestamp = datetime.utcnow().timestamp()

    def mockreturn(filename):
        return create_mock_data(timestamp)

    monkeypatch.setattr(app.app.main, "get_status", mockreturn)

    response = metrics()
    assert response.status_code == 200

    response_text = response.get_data(as_text=True)
    assert response_text == """some_metrics{db_name=\"montagu\"} 32178
cache_out_of_date{db_name=\"montagu\"} 0
metrics_responding{db_name=\"montagu\"} 1
"""


def test_endpoint_handles_stale_data(monkeypatch):

    def mockreturn(filename):
        return create_mock_data(1539089746)

    monkeypatch.setattr(app.app.main, "get_status", mockreturn)

    response = metrics()
    assert response.status_code == 200

    response_text = response.get_data(as_text=True)
    assert response_text == """cache_out_of_date{db_name=\"montagu\"} 1
metrics_responding{db_name=\"montagu\"} 1
"""


def test_sets_metrics_out_of_date_true_on_stale_data():

    timestamp = (datetime.now() - timedelta(minutes=15)).timestamp()
    stale_data = create_mock_data(timestamp)
    result = parse_status(stale_data, 600)
    assert result == {"cache_out_of_date": True}


def test_returns_fresh_data():

    timestamp = datetime.utcnow().timestamp()
    fresh_data = create_mock_data(timestamp)
    result = parse_status(fresh_data, 600)
    assert result == {
        "some_metrics": 32178,
        "cache_out_of_date": False
    }

