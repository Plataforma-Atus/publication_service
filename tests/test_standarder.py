from publisher.commute.freplace import find_replace


def test_find_replace(format_parameters_cropper):
    response = find_replace(format_parameters=format_parameters_cropper)
    breakpoint()
    assert True