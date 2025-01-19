def sharpe_ratio(investment_returns, market_returns):
  """
  Financial metric used to evaluate the risk-adjusted return of an investment. It measures how much excess return (or return above the risk-free rate) an investor earns for each unit of risk they take on. 
  """
  excess_returns = investment_returns - market_returns
  mean_excess_return = np.mean(excess_returns)
  investment_std = np.std(investment_returns)
  sharpe_ratio = mean_excess_return / investment_std
  
  return sharpe_ratio
  
  
def investment_beta(investment_returns, market_returns):
  """
  An investment's beta is its sensitivity to movements in the overall market. It indicates how much the investment's price is expected to change in response to changes in the market. 
  """
  covariance = np.cov(investment_returns, market_returns)
  market_variance = np.var(market_returns)
  beta = covariance / market_variance 
  
  return beta


def traynor_ratio(investment_returns, market_returns, investment_beta):
  """
  A financial metric used to evaluate the risk-adjusted margin of an investment or portfolio. It is similar to the Sharpe ratio, except it uses systematic risk (measured by beta) in the denominator of the ratio. It measures how much excess return an investment generates for each unit of market risk. 
  """
  excess_returns = investment_returns - market_returns
  mean_excess_return = np.mean(excess_returns)
  beta = investment_beta(investment_returns, market_returns)
  traynor_ratio = mean_excess_return / investment_std
  
  return traynor_ratio


def mortgage_annualized_ROI(loan_principal, loan_term, origination_fee_rate, monthly_payments, servicing_fee):
    """
    Calculate the annualized ROI for a fixed term mortgage loan.
    :param loan_principal: The principal amount of the loan.
    :param loan_term: The term of the loan in years.
    :param origination_fee_rate: The rate of the origination fee.
    :param monthly_payments: The monthly payment amount.
    :param serving_fee: Annual cost to service the loan.
    """
    total_payments = loan_term * 12 * monthly_payments
    origination_fee = origination_fee_rate * loan_principal
    serv_costs = servicing_fee * loan_term
    costs = loan_principal + serv_costs

    ROI = ((total_payments + origination_fee - costs) / loan_principal) * 100

    return ROI/loan_term
