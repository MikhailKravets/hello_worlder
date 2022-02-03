from worlder import Hello
from worlder.utils import string_multiplier


def test_hello():
    name = "jon doe"
    h = Hello(name)

    assert h.world() == f"Hello World! From {name}"


def test_string_multiplier():
    s = "hello"
    power = 2

    mul_s = string_multiplier(s, power=power)

    assert mul_s == s * power
