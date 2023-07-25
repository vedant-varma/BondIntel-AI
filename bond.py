class Bond:
    """Class representing a Bond."""

    def __init__(self, name, ytm, current_price, coupon, par_value, ai_text="N/A"):
        """Initialize the bond with given parameters."""
        self.name = name
        self.ytm = ytm
        self.current_price = current_price
        self.coupon = coupon
        self.par_value = par_value
        self.ai_text = ai_text

    def __str__(self):
        """Return a string representation of the bond."""
        s = "Name: " + self.name + "\n"
        s += "Years to Maturity: " + str(self.ytm) + "\n"
        s += "Current Price: " + str(self.current_price) + "\n"
        s += "Coupon: " + str(self.coupon) + "\n"
        s += "Par Value: " + str(self.par_value) + "\n"
        return s

    def to_string(self):
        """Convert the bond's data to a string."""
        s = "Name: " + self.name + "\n"
        s += "Years to Maturity: " + str(self.ytm) + "\n"
        s += "Current Price: " + str(self.current_price) + "\n"
        s += "Coupon: " + str(self.coupon) + "\n"
        s += "Par Value: " + str(self.par_value) + "\n"
        return s


