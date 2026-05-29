from weighted_mustafaenes_dag import weighted_srs

def test_weighted_srs_exists():
    assert callable(weighted_srs), "weighted_srs fonksiyonu bulunamadı!"

def test_weighted_srs_functionality():
    # Basit bir test
    data = [1, 2, 3]
    weights = [0.1, 0.1, 0.8]
    result = weighted_srs(data, 1, weights, with_replacement=True)
    assert len(result) == 1
