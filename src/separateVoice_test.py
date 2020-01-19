from . import separateVoice

def test_separateVoice():
    assert separateVoice.apply("Jane") == "hello Jane"
