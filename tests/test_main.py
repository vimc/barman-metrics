from datetime import datetime
from app.main import parse_status, metrics


def create_mock_data(timestamp):
    return """
    metrics_created_at: 20180921T133331
    some_metrics: 32178
""".format(timestamp)


def test_endpoint_handles_arbitrary_error():
    response = metrics()
    assert response.status_code == 200

    response_text = response.get_data(as_text=True)
    assert response_text == "something{target_name=\"fake-target\"} 2135423\n"


def test_sets_responding_false_on_stale_data():

    stale_data = create_mock_data("20180921T133331")
    result = parse_status(stale_data)
    assert result == {"responding": False}


def test_returns_fresh_data():

    # setup
    timestamp = datetime.utcnow().timestamp()
    fresh_data = create_mock_data(timestamp)
    result = parse_status(fresh_data)
    assert result == {
        "metrics_created_at": timestamp,
        "some_metrics": 32178
    }

