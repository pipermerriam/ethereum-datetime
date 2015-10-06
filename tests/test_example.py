def test_it(deployed_contracts):
    example = deployed_contracts.Example
    assert example.address
