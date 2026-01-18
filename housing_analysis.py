"""
Housing Price Data Analysis

This script analyzes a housing dataset (Housing.csv) and answers three questions:
1) How does the number of bedrooms affect average price?
2) Do houses with air conditioning cost more on average?
3) What is the relationship between area and price (visualized)?

It also prints helpful dataset context and summary statistics to justify results.
"""

from __future__ import annotations

import os
from typing import Tuple

import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------
# Configuration
# -----------------------------
DATA_FILE = "Housing.csv"
FIGURE_FILE = "area_vs_price.png"


# -----------------------------
# Utility / Helper Functions
# -----------------------------
def load_data(path: str) -> pd.DataFrame:
    """Load the dataset from a CSV file and return a DataFrame."""
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Could not find '{path}'. Make sure Housing.csv is in the same folder as this script."
        )

    df = pd.read_csv(path)
    return df


def print_dataset_overview(df: pd.DataFrame) -> None:
    """Print basic dataset info and a quick preview."""
    print("=== Dataset Overview ===")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("\nColumn names:")
    print(list(df.columns))

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nMissing values per column:")
    print(df.isna().sum())
    print()


def validate_columns(df: pd.DataFrame, required: list[str]) -> None:
    """Ensure the required columns exist."""
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise KeyError(f"Missing required columns: {missing}")


def format_currency(value: float) -> str:
    """Format a number like currency (no currency symbol to keep it generic)."""
    return f"{value:,.2f}"


# -----------------------------
# Analysis Functions
# -----------------------------
def avg_price_by_bedrooms(df: pd.DataFrame) -> pd.Series:
    """
    Question 1:
    Compute average price grouped by number of bedrooms.
    """
    grouped = df.groupby("bedrooms")["price"].mean().sort_index()
    return grouped


def compare_air_conditioning(df: pd.DataFrame) -> Tuple[float, float, float]:
    """
    Question 2:
    Compare average price for homes with vs without air conditioning.
    Returns (avg_with_ac, avg_without_ac, difference).
    """
    with_ac = df.loc[df["airconditioning"] == "yes", "price"].mean()
    without_ac = df.loc[df["airconditioning"] == "no", "price"].mean()
    diff = with_ac - without_ac
    return with_ac, without_ac, diff


def area_price_correlation(df: pd.DataFrame) -> float:
    """
    Extra justification:
    Compute correlation between area and price (Pearson correlation).
    """
    return df["area"].corr(df["price"])


def plot_area_vs_price(df: pd.DataFrame, save_path: str | None = None) -> None:
    """
    Question 3:
    Create a scatter plot for area vs price.
    Optionally save the plot to a file.
    """
    plt.figure()
    plt.scatter(df["area"], df["price"])
    plt.xlabel("Area (sq ft)")
    plt.ylabel("Price")
    plt.title("House Area vs Price")

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
        print(f"Saved plot to: {save_path}")

    plt.show()


# -----------------------------
# Main Program Flow
# -----------------------------
def main() -> None:
    # Load and validate data
    df = load_data(DATA_FILE)
    validate_columns(df, ["bedrooms", "price", "airconditioning", "area"])

    # Helpful context for your video/README explanation
    print_dataset_overview(df)

    # Question 1 output
    print("=== Question 1: Average price by number of bedrooms ===")
    by_bedrooms = avg_price_by_bedrooms(df)
    print(by_bedrooms)
    print("\n(Formatted)")
    for bedrooms, avg_price in by_bedrooms.items():
        print(f"{int(bedrooms)} bedroom(s): {format_currency(avg_price)}")
    print()

    # Question 2 output
    print("=== Question 2: Air conditioning vs price ===")
    with_ac, without_ac, diff = compare_air_conditioning(df)
    print(f"Average price WITH air conditioning:  {format_currency(with_ac)}")
    print(f"Average price WITHOUT air conditioning: {format_currency(without_ac)}")
    print(f"Difference (with - without):          {format_currency(diff)}")
    print()

    # Extra justification: correlation (supports your “positive relationship” claim)
    print("=== Extra: Correlation (Area vs Price) ===")
    corr = area_price_correlation(df)
    print(f"Pearson correlation between area and price: {corr:.4f}")
    print()

    # Question 3 output: graph
    print("=== Question 3: Plot (Area vs Price) ===")
    plot_area_vs_price(df, save_path=FIGURE_FILE)


if __name__ == "__main__":
    main()
