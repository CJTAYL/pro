def sharpe_ratio(investment_returns, market_returns):
  """
  Financial metric used to evaluate the risk-adjusted return of an investment. It measures how much excess return (or return above the risk-free rate) an investor earns for each unit of risk they take on. 

  Parameters:
  - investment_returns = list of investment returns 
  - market_returns = list of market returns
  """
  excess_returns = investment_returns - market_returns
  mean_excess_return = np.mean(excess_returns)
  investment_std = np.std(investment_returns)
  sharpe_ratio = mean_excess_return / investment_std
  
  return sharpe_ratio
  
  
def investment_beta(investment_returns, market_returns):
  """
  An investment's beta is its sensitivity to movements in the overall market. It indicates how much the investment's price is expected to change in response to changes in the market. 

  Parameters:
  - investment_returns = list of investment returns 
  - market_returns = list of market returns
  """
  covariance = np.cov(investment_returns, market_returns)
  market_variance = np.var(market_returns)
  beta = covariance / market_variance 
  
  return beta


def traynor_ratio(investment_returns, market_returns, investment_beta):
  """
  A financial metric used to evaluate the risk-adjusted margin of an investment or portfolio. It is similar to the Sharpe ratio, except it uses systematic risk (measured by beta) in the denominator of the ratio. It measures how much excess return an investment generates for each unit of market risk. 

  Parameters:
  - investment_returns: list of investment returns 
  - market_returns: list of market returns 
  - investment_beta: beta of investment
  """
  excess_returns = investment_returns - market_returns
  mean_excess_return = np.mean(excess_returns)
  beta = investment_beta(investment_returns, market_returns)
  traynor_ratio = mean_excess_return / investment_std
  
  return traynor_ratio


def calculate_mortgage_portfolio_return(
    total_loan_amount, 
    average_interest_rate, 
    average_loan_term_years, 
    average_funding_cost_rate, 
    annual_operational_costs, 
    prepayment_rate, 
    default_rate, 
    annual_fee_revenue
):
    """
    Calculate the return on a portfolio of fixed-rate mortgages.

    Parameters:
    - total_loan_amount: Total value of loans in the portfolio ($)
    - average_interest_rate: Average fixed interest rate (as a decimal, e.g., 0.04 for 4%)
    - average_loan_term_years: Average loan term in years
    - average_funding_cost_rate: Average funding cost rate (as a decimal, e.g., 0.02 for 2%)
    - annual_operational_costs: Total annual operational costs ($)
    - prepayment_rate: Annual prepayment rate (as a decimal, e.g., 0.10 for 10%)
    - default_rate: Annual default rate (as a decimal, e.g., 0.02 for 2%)
    - annual_fee_revenue: Annual fee revenue from the portfolio ($)

    Returns:
    - A dictionary containing total revenue, total expenses, net income, and return on portfolio (%).
    """
    # Calculate revenue components
    annual_interest_income = total_loan_amount * average_interest_rate
    effective_loan_amount = total_loan_amount * (1 - prepayment_rate - default_rate)
    adjusted_interest_income = annual_interest_income * (1 - prepayment_rate - default_rate)
    total_revenue = adjusted_interest_income + annual_fee_revenue

    # Calculate expense components
    funding_costs = effective_loan_amount * average_funding_cost_rate
    provision_for_defaults = total_loan_amount * default_rate
    total_expenses = funding_costs + annual_operational_costs + provision_for_defaults

    # Calculate net income and return on portfolio
    net_income = total_revenue - total_expenses
    return_on_portfolio = (net_income / total_loan_amount) * 100

    # Return results as a dictionary
    return {
        "Total Revenue": total_revenue,
        "Total Expenses": total_expenses,
        "Net Income": net_income,
        "Return on Portfolio (%)": return_on_portfolio
    }


def calculate_credit_card_portfolio_return(
    outstanding_balance, 
    average_apr, 
    days_outstanding, 
    transaction_volume, 
    interchange_rate, 
    annual_fee_revenue, 
    late_fee_revenue, 
    foreign_fee_revenue, 
    cost_of_funds_rate, 
    operational_costs, 
    default_rate
):
    """
    Calculate the return on a portfolio of credit cards.

    Parameters:
    - outstanding_balance: Total outstanding balance ($)
    - average_apr: Average annual percentage rate (as a decimal, e.g., 0.18 for 18%)
    - days_outstanding: Average days outstanding for balances
    - transaction_volume: Total transaction volume ($)
    - interchange_rate: Interchange fee rate (as a decimal, e.g., 0.02 for 2%)
    - annual_fee_revenue: Total annual fee revenue ($)
    - late_fee_revenue: Total late fee revenue ($)
    - foreign_fee_revenue: Total foreign transaction fee revenue ($)
    - cost_of_funds_rate: Cost of funds rate (as a decimal, e.g., 0.05 for 5%)
    - operational_costs: Total operational costs ($)
    - default_rate: Default rate for the portfolio (as a decimal, e.g., 0.02 for 2%)

    Returns:
    - A dictionary containing total revenue, total expenses, net income, and return on portfolio (%).
    """
    # Calculate revenue components
    interest_income = outstanding_balance * average_apr * (days_outstanding / 365)
    interchange_fees = transaction_volume * interchange_rate
    total_fee_revenue = annual_fee_revenue + late_fee_revenue + foreign_fee_revenue
    total_revenue = interest_income + interchange_fees + total_fee_revenue

    # Calculate expense components
    cost_of_funds = outstanding_balance * cost_of_funds_rate
    provision_for_losses = outstanding_balance * default_rate
    total_expenses = cost_of_funds + operational_costs + provision_for_losses

    # Calculate net income and return on portfolio
    net_income = total_revenue - total_expenses
    return_on_portfolio = (net_income / outstanding_balance) * 100

    # Return results as a dictionary
    return {
        "Total Revenue": total_revenue,
        "Total Expenses": total_expenses,
        "Net Income": net_income,
        "Return on Portfolio (%)": return_on_portfolio
    }


def calculate_loan_provision(outstanding_balance, default_rate, loss_given_default):
    """
    Calculate the provision for loan losses.

    Parameters:
    - outstanding_balance: Total outstanding loan balance ($)
    - default_rate: Expected default rate (as a decimal, e.g., 0.02 for 2%)
    - loss_given_default: Loss given default (as a decimal, e.g., 0.50 for 50%)

    Returns:
    - Provision for loan losses ($)
    """
    provision = outstanding_balance * default_rate * loss_given_default
    return provision
