
import fp


def test_list():
    l1 = fp.L[1, 2, 3]
    assert l1 == [1, 2, 3]

    l2 = l1.map(str)
    assert l2 == ["1", "2", "3"]
    assert isinstance(l2, fp.L)
    assert l1 == [1, 2, 3]

    assert l1.map(str).join("-") == "1-2-3"

    result = []

    def collect(x, delta=0):
        result.append(x + delta)

    l1.foreach(collect, delta=1)
    assert result == [2, 3, 4]

    def inc(x, delta=1):
        return x + delta

    l2 = l1.map(inc, delta=2)
    assert l2 == [3, 4, 5]
    assert isinstance(l2, fp.L)

    l2 = l1.filter(fp.p_even)
    assert l2 == [2]
    assert isinstance(l2, fp.L)

    # todo
    assert l1.reduce(lambda a, b: a + b, 1) == 7

    assert l1.sum() == 6

    def summer(*nums):
        return sum(nums)

    assert l1.apply(summer) == 6

    res = l1 + (1, 2, 3)
    assert res == [1, 2, 3, 1, 2, 3]
    assert isinstance(res, fp.L)

    assert str(l1) == "List[1, 2, 3]"

    t1 = l1.T()
    assert t1 == (1, 2, 3)
    assert isinstance(t1, fp.Tuple)

    l2 = l1.group(2)
    assert l2 == [[1, 2], [3]]
    assert isinstance(l2, fp.L)
    el1, el2 = l2
    assert isinstance(el1, fp.L)
    assert isinstance(el2, fp.L)

    d1 = fp.L["a", 1, "b", 2].group(2).D()
    assert d1 == {"a": 1, "b": 2}
    assert isinstance(d1, fp.D)

    # todo slice
