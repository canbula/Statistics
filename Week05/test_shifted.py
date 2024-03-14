import os
import inspect


files = [f for f in os.listdir(os.path.dirname(__file__)) if f.startswith("shifted")]
for f in files:
    exec("import " + f[:-3] + " as " + f[:-3])


def test_names():
    for f in files:
        assert "shifted" in dir(eval(f[:-3])), (
            "shifted is not defined in " + f[:-3]
        )


def test_callables():
    for f in files:
        assert callable(eval(f[:-3]).shifted), (
            "shifted is not callable in " + f[:-3]
        )


def test_loc():
    for f in files:
        f = os.path.join(os.path.dirname(__file__), f)
        with open(f, "r") as file:
            loc = len(file.readlines())
            assert loc < 10, "Too many lines in " + f[:-3]


def test_perfect_samples():
    perfect_samples = [
        [1, 2, 3],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ]
    for f in files:
        for sample in perfect_samples:
            assert eval(f[:-3]).shifted(sample) == 0, (
                "The return value should be 0 for perfect samples in " + f[:-3]
            )


def test_low_shift():
    low_shift = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10],
    ]
    for f in files:
        for sample in low_shift:
            assert 0 < eval(f[:-3]).shifted(sample) < 20, (
                "The return value should be between 0 and 10 for low shift in " + f[:-3]
            )


def test_moderate_shift():
    moderate_shift = [
        [1, 2, 5, 9, 30],
        [1, 1, 1, 5, 9, 18],
    ]
    for f in files:
        for sample in moderate_shift:
            assert 20 < eval(f[:-3]).shifted(sample) < 50, (
                "The return value should be between 10 and 20 for moderate shift in " + f[:-3]
            )


def test_high_shift():
    high_shift = [
        [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 100, 100, 100],
        [2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 90, 90, 100, 100],
        [3, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 90, 90, 90, 90, 90],
        [4, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 70, 70, 70, 80, 80, 80],
    ]
    for f in files:
        for sample in high_shift:
            assert 50 < eval(f[:-3]).shifted(sample) < 80, (
                "The return value should be between 20 and 30 for high shift in " + f[:-3]
            )


def test_very_high_shift():
    very_high_shift = [
        [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 100, 100, 100, 100, 100],
        [2, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 100, 100, 100, 100, 100],
        [3, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 100, 100, 100, 100, 100, 100, 100],
        [4, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 100, 100, 100, 100, 100, 100, 100],
    ]
    for f in files:
        for sample in very_high_shift:
            assert 80 < eval(f[:-3]).shifted(sample), (
                "The return value should be between 30 and 40 for very high shift in " + f[:-3]
            )


def test_with_negative_numbers():
    for f in files:
        assert 0 < eval(f[:-3]).shifted(
            [-1, -2, -2, -3, -4, -5, -5, -5, -6, -7, -8, -9, -100, -100, -100, -100]
        ) > 0, (
            "The return value should be positive even if the numbers are negative in " + f[:-3]
        )
