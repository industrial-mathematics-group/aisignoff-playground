from playground.io import read_column


def test_read_column(tmp_path):
    p = tmp_path / "data.csv"
    p.write_text("t,y\n0,1.5\n1,\n2,3.0\n", encoding="utf-8")
    assert read_column(p, "y") == [1.5, 3.0]
