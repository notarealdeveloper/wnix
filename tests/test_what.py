from wnix import what

def test_what():
    q = ['red cow', 'blue cow', 'green chicken', 'purple chicken']
    k = ['dog', 'cat', 'bird', 'snake', 'cow', 'chicken', 'horse', 'pig']
    w = what(q, k)
    assert w.ravel().tolist() == ['cow', 'cow', 'chicken', 'chicken']
