#Liste af muligheder for at gøre det mere nøjagtigt

weekly_mean = data.rolling(7).mean()
quarterly_mean = data.rolling(90).mean()
annual_mean = data.rolling(365).mean()
weekly_trend = data.shift(1).rolling(7).mean()["Target"]
data["weekly_mean"] = weekly_mean["Close"] / data["Close"]
data["quarterly_mean"] = quarterly_mean["Close"] / data["Close"]
data["annual_mean"] = annual_mean["Close"] / data["Close"]

data["annual_weekly_mean"] = data["annual_mean"] / data["weekly_mean"]
data["annual_quarterly_mean"] = data["annual_mean"] / data["quarterly_mean"]
data["weekly_trend"] = weekly_trend

data["open_close_ratio"] = data["Open"] / data["Close"]
data["high_close_ratio"] = data["High"] / data["Close"]
data["low_close_ratio"] = data["Low"] / data["Close"]


full_predictors = predictors + ["weekly_mean", "quarterly_mean", "annual_mean", "annual_weekly_mean", "annual_quarterly_mean", "open_close_ratio", "high_close_ratio", "low_close_ratio", "weekly_trend"]
predictions = backtest(data.iloc[365:], model, full_predictors)

precision_score(predictions["Target"], predictions["Predictions"])

#Improve the algorithm suggestions
#Run with a reduced step size! This will take longer, but increase accuracy
#Try discarding older data (only keeping data in a certain window)
#Try a different machine learning algorithm
#Tweak random forest parameters, or the prediction threshold
#Add in more predictors
#Account for activity post-close and pre-open
#Early trading
#Trading on other exchanges that open before the NYSE (to see what the global sentiment is)
#Economic indicators
#Interest rates
#Other important economic news
#Key dates
#Dividends
#External factors like elections
#Company milestones
#Earnings calls
#Analyst ratings
#Major announcements
#Prices of related stocks
#Other companies in the same sector
#Key partners, customers, etc.