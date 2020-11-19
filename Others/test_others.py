from Next_closest_time import next_closest_time


def test_next_closest_time():
    assert next_closest_time("19:34") == "19:39"
    assert next_closest_time("23:59") == "22:22"
    assert next_closest_time("00:00") == "00:00"
    assert next_closest_time("22:22") == "22:22"
    assert next_closest_time("11:11") == "11:11"
    assert next_closest_time("19:29") == "21:11"
    assert next_closest_time("12:34") == "12:41"

