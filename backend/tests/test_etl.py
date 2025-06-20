from etl import fetch_sce_ica


def test_etl():
    data = fetch_sce_ica.get_data()
    assert len(data) > 0
    ids = [row["id"] for row in data]
    assert len(ids) == len(set(ids))
