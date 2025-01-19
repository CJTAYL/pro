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
