from tabulate import tabulate


class Table:

    def __init__(self, principal, interest, num_years):
        self.principal = principal
        self.interest = interest
        self.num_years = num_years


table = Table(1000, 0.5, 3)

si_calculation = table.principal*(1+table.interest*table.num_years)

simple_interest = [1, table.num_years, table.interest, si_calculation]

monthly_compound = [12, 12*table.num_years, table.interest/12,
                    table.principal*(1+table.interest/12)**(12*table.num_years)]

quarterly_compound = [4, 4*table.num_years, table.interest/4,
                      table.principal*(1+table.interest/4)**(4*table.num_years)]

semiannual_compound = [2, 2*table.num_years, table.interest/2,
                       table.principal*(1+table.interest/2)**(2*table.num_years)]

annual_compound = [1, 1*table.num_years, table.interest/1,
                   table.principal*(1+table.interest/1)**(1*table.num_years)]

daily_compound = [365, 365*table.num_years, table.interest/365,
                  table.principal*(1+table.interest/365)**(365*table.num_years)]

print(tabulate([simple_interest, monthly_compound, quarterly_compound, semiannual_compound, annual_compound, daily_compound],
               headers=["# of compounding periods per year(m)", "# of compounding periods in t years",
                        "periodic rate of interest", "Future Value"]))
