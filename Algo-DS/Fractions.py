class Fractions(object):
  """Fractions Type.

      Fractions class to represent fractions.

      Attributes:
          numerator: A integer denoting numerator value.
          denominator: A integer denoting denominator value.
  """

  def __init__(self, top, bottom):
    """Constructor for Fractions class.

        Args:
            top: A integer denoting numerator.
            bottom: A integer denoting denominator.
    """
    self.numerator = top
    self.denominator = bottom

  def show(self):
    """Print the fraction in numerator / denominator format."""
    print "%d/%d" %(self.numerator, self.denominator)

  def __str__(self):
    """Stringify the fraction in numerator / denominator format"""
    return "%d/%d" % (self.numerator, self.denominator)

  def __add__(self, other_fraction):
    """Method to add two fractions.

       Args:
           other_fraction: A instance of Fractions class.

       Returns:
           Sum of two fractions.
           eg:
               >>> f1 = Fraction(1/2)
               >>> f2 = Fraction(3/4)
               >>> f1.__add__(f2)
               >>> print f1
               >>> 10/8
    """
    combined_numerator = (self.numerator*other_fraction.denominator+other_fraction.numerator*self.denominator)
    combined_denominator = self.denominator*other_fraction.denominator
    return "%d/%d" %(combined_numerator, combined_denominator)

