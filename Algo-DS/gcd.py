"""This module is used to generate GDC of two given integer numbers.
    Elucids Algorithm states that for given two numbers m and n the GDC
    is n if n divides m evenly, if n does not divide m evenly then GDC of n and
    the remainder of m divided by n.
    It uses the Elicids Algorithm to dertermine the GDC.

    Example:
        >>> gdc(10,20)
        >>> 10
    """

def gcd(integer_m, integer_n):
  """" Function to caliculate GDC of given two numbers using Elucids Algorithm.

  Args:
      m: Integer value.
      n: Integer value.

  Return:
      Return GDC of m, n.
  """
  while integer_m%integer_n != 0:
    oldm = integer_m
    oldn = integer_n

    integer_m = oldn
    integer_n = oldm%oldn
  return integer_n


if __name__ == '__main__':
  print gcd(10, 20)
