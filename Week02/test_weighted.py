import sys


sys.path.append(".")


from Week02 import data
import os
import inspect


files = [f for f in os.listdir(os.path.dirname(__file__)) if f.startswith("weighted")]
for f in files:
    exec("import " + f[:-3] + " as " + f[:-3])


def test_names():
    for f in files:
        assert "weighted_srs" in dir(eval(f[:-3])), (
            "weighted_srs is not defined in " + f[:-3]
        )


def test_callables():
    for f in files:
        assert callable(eval(f[:-3]).weighted_srs), (
            "weighted_srs is not callable in " + f[:-3]
        )


def test_loc():
    for f in files:
        f = os.path.join(os.path.dirname(__file__), f)
        with open(f, "r") as file:
            loc = len(file.readlines())
            assert loc < 10, "Too many lines in " + f[:-3]


def test_import_random():
    for f in files:
        f = os.path.join(os.path.dirname(__file__), f)
        with open(f, "r") as file:
            content = file.read()
            assert "import random" in content, (
                "random module is not imported in " + f[:-3]
            )


def test_import_statements():
    for f in files:
        f = os.path.join(os.path.dirname(__file__), f)
        with open(f, "r") as file:
            content = file.read()
            assert content.count("import") == 1, (
                "More than one import statement is used in " + f[:-3]
            )


def test_signature():
    for f in files:
        sig = inspect.signature(eval(f[:-3]).weighted_srs)
        assert len(sig.parameters) == 4, (
            "weighted_srs should take 4 parameters in " + f[:-3]
        )
        assert sig.parameters["data"].default == inspect._empty, (
            "data should be a required parameter in " + f[:-3]
        )
        assert sig.parameters["n"].default == inspect._empty, (
            "n should be a required parameter in " + f[:-3]
        )
        assert sig.parameters["weights"].default == inspect._empty, (
            "weights should be a required parameter in " + f[:-3]
        )
        assert sig.parameters["with_replacement"].default == False, (
            "with_replacement should be a keyword only parameter in " + f[:-3]
        )


def test_true_random_sample():
    for f in files:
        true_random_sample = eval(f[:-3]).weighted_srs(data.cities, 25, None, True)
        assert len(true_random_sample) == 25, "Sample size should be 25 in " + f[:-3]
        assert len(set(true_random_sample)) <= 25, (
            "Sample should contain duplicates in " + f[:-3] + " to be True Random"
        )


def test_random_sample():
    for f in files:
        random_sample = eval(f[:-3]).weighted_srs(data.cities, 25, None)
        assert len(random_sample) == 25, "Sample size should be 25 in " + f[:-3]
        assert len(set(random_sample)) == 25, (
            "Sample should not contain duplicates in " + f[:-3]
        )


def test_weights():
    for f in files:
        weighted_cities = {
            "Manisa": 1000,
            "İzmir": 500,
            "Ankara": 200,
            "İstanbul": 200,
        }
        weights = []
        for city in data.cities:
            weights.append(weighted_cities.get(city, 1))
        sample = eval(f[:-3]).weighted_srs(data.cities, 50, weights)
        assert sample.count("Manisa") > 8, "Return value is incorrect in " + f[:-3]
        assert sample.count("İzmir") > 5, "Return value is incorrect in " + f[:-3]
        assert sample.count("Ankara") > 0, "Return value is incorrect in " + f[:-3]
        assert sample.count("İstanbul") > 0, "Return value is incorrect in " + f[:-3]
        weighted_cities = {
            "Tokat": 100,
            "Malatya": 100,
        }
        weights = []
        for city in data.cities:
            weights.append(weighted_cities.get(city, 1))
        sample = eval(f[:-3]).weighted_srs(data.cities, 50, weights)
        assert sample.count("Tokat") > 5, "Return value is incorrect in " + f[:-3]
        assert sample.count("Malatya") > 5, "Return value is incorrect in " + f[:-3]
