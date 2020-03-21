import subprocess


def test_does_it_work():
    """
    I had the option of either removing everyting related to testing from the
    project generated from my template or add at least one test as an alibi. :)
    """

    output = subprocess.check_output(['nice-ast', __file__], encoding='utf-8')

    assert 'test_does_it_work' in output
