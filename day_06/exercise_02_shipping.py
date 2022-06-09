# Ground shipping
def ground_shipping(weight: int) -> int:
    """
    :type: weight: int - the price per pound weight of the package.
    :rtype: Int
    """

    # total cost list
    cost = 0

    two_lb_or_less = 1.50
    over_2_lb_but_less_than_or_equal_to_6_lb = 3.00
    over_6_lb_but_less_than_or_equal_to_10_lb = 4.00
    over_10_lb = 4.75
    flat_charge = 20.00

    if weight <= 2:
        cost += weight * two_lb_or_less + flat_charge
    elif 2 < weight < 6:
        cost += weight * over_2_lb_but_less_than_or_equal_to_6_lb + flat_charge
    elif 6 < weight < 10:
        cost += weight * over_6_lb_but_less_than_or_equal_to_10_lb + flat_charge
    elif weight >= 10:
        cost += weight * over_10_lb + flat_charge

    return cost


customer_calc = ground_shipping(3)
print(customer_calc)

