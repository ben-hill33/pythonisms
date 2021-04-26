from functools import wraps
import time

def my_decorator(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    return result
  return wrapper

@my_decorator
def add(a, b):
  "Add function"
  return a + b

print(add(1, 3))


