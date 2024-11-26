import numpy as np
import matplotlib.pyplot as plt

def simulate_stock_prices(initial_price, volatility, time_steps, num_simulations):
  """
  Simulates stock price paths using Geometric Brownian Motion (GBM).

  Args:
    initial_price: The initial stock price.
    volatility: The volatility of the stock price.
    time_steps: The number of time steps to simulate.
    num_simulations: The number of simulations to run.

  Returns:
    A NumPy array of shape (num_simulations, time_steps) containing the simulated stock prices.
  """

  dt = 1 / time_steps
  mu = 0  # Assuming risk-free rate is zero
  
  # Generate random numbers from a standard normal distribution
  z = np.random.randn(num_simulations, time_steps)

  # Calculate the stock price at each time step for each simulation
  stock_prices = np.zeros((num_simulations, time_steps))
  stock_prices[:, 0] = initial_price
  for i in range(1, time_steps):
    stock_prices[:, i] = stock_prices[:, i - 1] * np.exp((mu - 0.5 * volatility**2) * dt + volatility * np.sqrt(dt) * z[:, i])

  return stock_prices

# Example usage:
initial_price = 100
volatility = 0.2
time_steps = 252  # Assuming 252 trading days in a year
num_simulations = 1000

simulated_prices = simulate_stock_prices(initial_price, volatility, time_steps, num_simulations)

# Plot the simulated stock price paths
plt.figure(figsize=(10, 6))
plt.plot(simulated_prices.T)
plt.xlabel("Time Steps")
plt.ylabel("Stock Price")
plt.title("Simulated Stock Price Paths")
plt.show()