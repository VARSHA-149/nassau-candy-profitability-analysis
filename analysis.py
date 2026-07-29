import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Load the dataset
df = pd.read_csv("data/Nassau Candy Distributor.csv")

# Display the first 5 rows
print("First 5 Rows:")
print(df.head())

# Display the dataset shape
print("\nDataset Shape:")
print(df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())


print("\n========== DATA CLEANING ==========")

# Shape before cleaning
print("Shape before cleaning:", df.shape)

# Remove rows where Sales is less than or equal to 0
df = df[df["Sales"] > 0]

# Remove rows where Cost is negative
df = df[df["Cost"] >= 0]

# Remove rows where Gross Profit is negative
df = df[df["Gross Profit"] >= 0]

# Remove extra spaces from text columns
df["Division"] = df["Division"].str.strip()
df["Product Name"] = df["Product Name"].str.strip()

# Shape after cleaning
print("Shape after cleaning:", df.shape)



print("\n========== FEATURE ENGINEERING ==========")

# Convert date columns to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)

# Gross Margin (%)
df["Gross Margin (%)"] = (df["Gross Profit"] / df["Sales"]) * 100

# Profit per Unit
df["Profit per Unit"] = df["Gross Profit"] / df["Units"]

# Revenue Contribution (%)
df["Revenue Contribution (%)"] = (
    df["Sales"] / df["Sales"].sum()
) * 100

# Profit Contribution (%)
df["Profit Contribution (%)"] = (
    df["Gross Profit"] / df["Gross Profit"].sum()
) * 100

# Shipping Days
df["Shipping Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

print("\nNew Columns Created Successfully!")

print(df[[
    "Gross Margin (%)",
    "Profit per Unit",
    "Revenue Contribution (%)",
    "Profit Contribution (%)",
    "Shipping Days"
]].head())


print("\n========== TOP 10 MOST PROFITABLE PRODUCTS ==========\n")

top_products = (
    df.groupby("Product Name")
      .agg({
          "Sales": "sum",
          "Gross Profit": "sum",
          "Gross Margin (%)": "mean"
      })
      .sort_values(by="Gross Profit", ascending=False)
      .head(10)
)

print(top_products)


# ==========================
# TOP 10 PROFITABLE PRODUCTS CHART
# ==========================

import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

top_products["Gross Profit"].plot(kind="bar", color="green")

plt.title("Top 10 Most Profitable Products")
plt.xlabel("Product Name")
plt.ylabel("Gross Profit")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.show()


print("\n========== HIGH SALES - LOW MARGIN PRODUCTS ==========\n")

high_sales_low_margin = (
    df[["Product Name", "Sales", "Gross Margin (%)"]]
    .sort_values(by="Sales", ascending=False)
)

print(high_sales_low_margin.head(10))



plt.figure(figsize=(10,6))

plt.scatter(
    df["Sales"],
    df["Gross Margin (%)"],
    alpha=0.6
)

plt.title("Sales vs Gross Margin")
plt.xlabel("Sales")
plt.ylabel("Gross Margin (%)")

plt.grid(True)

plt.show()



print("\n========== DIVISION PERFORMANCE ==========\n")

division_summary = (
    df.groupby("Division")
      .agg({
          "Sales": "sum",
          "Gross Profit": "sum",
          "Gross Margin (%)": "mean",
          "Units": "sum"
      })
      .sort_values(by="Gross Profit", ascending=False)
)

print(division_summary)




plt.figure(figsize=(8,5))

division_summary["Sales"].plot(kind="bar", color="skyblue")

plt.title("Sales by Division")
plt.xlabel("Division")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))

division_summary["Gross Profit"].plot(kind="bar", color="green")

plt.title("Gross Profit by Division")
plt.xlabel("Division")
plt.ylabel("Gross Profit")

plt.tight_layout()
plt.show()


plt.figure(figsize=(8,5))

division_summary["Gross Margin (%)"].plot(kind="bar", color="orange")

plt.title("Average Gross Margin by Division")
plt.xlabel("Division")
plt.ylabel("Gross Margin (%)")

plt.tight_layout()
plt.show()




# ==========================================================
# PARETO ANALYSIS (80/20 RULE)
# ==========================================================

print("\n========== PARETO ANALYSIS ==========\n")

pareto = (
    df.groupby("Product Name")["Gross Profit"]
      .sum()
      .sort_values(ascending=False)
      .reset_index()
)

pareto["Cumulative Profit"] = pareto["Gross Profit"].cumsum()

pareto["Cumulative %"] = (
    pareto["Cumulative Profit"] /
    pareto["Gross Profit"].sum()
) * 100

print(pareto)

plt.figure(figsize=(12,6))

plt.bar(
    pareto["Product Name"],
    pareto["Gross Profit"],
    color="steelblue"
)

plt.plot(
    pareto["Product Name"],
    pareto["Cumulative %"],
    color="red",
    marker="o"
)

plt.axhline(
    y=80,
    color="green",
    linestyle="--",
    label="80% Profit"
)

plt.xticks(rotation=45, ha="right")

plt.title("Pareto Analysis (80/20 Rule)")
plt.ylabel("Gross Profit")

plt.legend()

plt.tight_layout()

plt.show()



# ==========================================================
# COST STRUCTURE DIAGNOSTICS
# ==========================================================

print("\n========== COST STRUCTURE DIAGNOSTICS ==========\n")

plt.figure(figsize=(10,6))

plt.scatter(
    df["Cost"],
    df["Sales"],
    c=df["Gross Margin (%)"],
    cmap="viridis",
    alpha=0.7
)

plt.colorbar(label="Gross Margin (%)")

plt.xlabel("Cost")

plt.ylabel("Sales")

plt.title("Cost vs Sales")

plt.grid(True)

plt.show()



# ==========================================================
# REGIONAL PERFORMANCE
# ==========================================================

print("\n========== REGIONAL PERFORMANCE ==========\n")

region_summary = (
    df.groupby("Region")
      .agg({
          "Sales":"sum",
          "Gross Profit":"sum",
          "Gross Margin (%)":"mean"
      })
      .sort_values(by="Gross Profit", ascending=False)
)

print(region_summary)

plt.figure(figsize=(8,5))

region_summary["Gross Profit"].plot(
    kind="bar",
    color="purple"
)

plt.title("Gross Profit by Region")

plt.ylabel("Gross Profit")

plt.tight_layout()

plt.show()



# ==========================================================
# REGIONAL PERFORMANCE
# ==========================================================

print("\n========== REGIONAL PERFORMANCE ==========\n")

region_summary = (
    df.groupby("Region")
      .agg({
          "Sales":"sum",
          "Gross Profit":"sum",
          "Gross Margin (%)":"mean"
      })
      .sort_values(by="Gross Profit", ascending=False)
)

print(region_summary)

plt.figure(figsize=(8,5))

region_summary["Gross Profit"].plot(
    kind="bar",
    color="purple"
)

plt.title("Gross Profit by Region")

plt.ylabel("Gross Profit")

plt.tight_layout()

plt.show()




# ==========================================================
# MONTHLY TREND
# ==========================================================

print("\n========== MONTHLY SALES TREND ==========\n")

df["Month"] = df["Order Date"].dt.month_name()

monthly = (
    df.groupby("Month")
      .agg({
          "Sales":"sum",
          "Gross Profit":"sum"
      })
)

print(monthly)

monthly.plot(
    figsize=(12,6),
    marker="o"
)

plt.title("Monthly Sales and Profit Trend")

plt.ylabel("Amount")

plt.grid(True)

plt.show()




# ==========================================================
# MACHINE LEARNING - GROSS PROFIT PREDICTION
# ==========================================================

print("\n========== MACHINE LEARNING ==========\n")

# Copy the dataset
ml_df = df.copy()

# Encode categorical variables
encoder = LabelEncoder()

categorical_columns = ["Division", "Region", "Ship Mode"]

for col in categorical_columns:
    ml_df[col] = encoder.fit_transform(ml_df[col])

# Select features
X = ml_df[[
    "Sales",
    "Cost",
    "Units",
    "Division",
    "Region",
    "Ship Mode"
]]

# Target
y = ml_df["Gross Profit"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ==========================
# Linear Regression
# ==========================

lr = LinearRegression()
lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)

print("----- Linear Regression -----")
print("MAE :", round(mean_absolute_error(y_test, lr_pred), 2))
print("RMSE:", round(np.sqrt(mean_squared_error(y_test, lr_pred)), 2))
print("R²  :", round(r2_score(y_test, lr_pred), 4))

# ==========================
# Random Forest
# ==========================

rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

print("\n----- Random Forest -----")
print("MAE :", round(mean_absolute_error(y_test, rf_pred), 2))
print("RMSE:", round(np.sqrt(mean_squared_error(y_test, rf_pred)), 2))
print("R²  :", round(r2_score(y_test, rf_pred), 4))



