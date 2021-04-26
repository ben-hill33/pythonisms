from ..decorator import my_decorator

def test_proof_of_life():
  @my_decorator
  def add(a, b):
    return a + b

  assert add(1,3) == 4


