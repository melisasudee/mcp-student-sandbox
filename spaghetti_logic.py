"""
Data processing module with clean code principles.
Separates concerns: calculation, formatting, and logging.
"""

from typing import List
import logging

# Configure logging
logging.basicConfig(
    filename="process_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


# Constants
PRICE_INCREASE_RATE = 1.15  # 15% increase
DECIMAL_PLACES = 2
CURRENCY_SYMBOL = "USD"


def apply_price_increase(original_price: float) -> float:
    """
    Calculate price with percentage increase.
    
    Args:
        original_price: Original price amount
        
    Returns:
        Price after applying PRICE_INCREASE_RATE
        
    Raises:
        ValueError: If price is negative
    """
    if original_price < 0:
        raise ValueError("Price cannot be negative")
    
    return original_price * PRICE_INCREASE_RATE


def format_price(price: float, decimal_places: int = DECIMAL_PLACES) -> str:
    """
    Format price as string with specified decimal places.
    
    Args:
        price: Price amount to format
        decimal_places: Number of decimal places (default: 2)
        
    Returns:
        Formatted price string
    """
    return f"{price:.{decimal_places}f}"


def log_processing_result(original_prices: List[float], 
                         processed_prices: List[float]) -> None:
    """
    Log the data processing results.
    
    Args:
        original_prices: List of original prices
        processed_prices: List of processed prices
    """
    total_processed = sum(processed_prices)
    count = len(processed_prices)
    average_price = total_processed / count if count > 0 else 0
    
    log_message = (
        f"Processed {count} items | "
        f"Total: {format_price(total_processed)} {CURRENCY_SYMBOL} | "
        f"Average: {format_price(average_price)} {CURRENCY_SYMBOL}"
    )
    logging.info(log_message)


def process_prices(prices: List[float], verbose: bool = False) -> List[float]:
    """
    Process a list of prices by applying price increase.
    Separates calculation from side effects (logging).
    
    Args:
        prices: List of prices to process
        verbose: If True, print each processed price
        
    Returns:
        List of processed prices
        
    Raises:
        ValueError: If any price is negative
        TypeError: If prices contain non-numeric values
    """
    if not prices:
        logging.warning("No prices provided for processing")
        return []
    
    try:
        processed_prices = []
        for original_price in prices:
            # Validate input
            if not isinstance(original_price, (int, float)):
                raise TypeError(f"Expected number, got {type(original_price).__name__}")
            
            # Calculate new price
            new_price = apply_price_increase(original_price)
            processed_prices.append(new_price)
            
            # Optional verbose output
            if verbose:
                formatted = format_price(new_price)
                print(f"  {original_price} → {formatted} {CURRENCY_SYMBOL}")
        
        # Log results
        log_processing_result(prices, processed_prices)
        
        return processed_prices
        
    except (ValueError, TypeError) as e:
        logging.error(f"Error processing prices: {e}")
        raise


def main():
    """Main function to demonstrate price processing."""
    sample_prices = [100.0, 50.0, 75.50, 200.0]
    
    print(f"Processing {len(sample_prices)} prices with {(PRICE_INCREASE_RATE - 1) * 100:.0f}% increase:")
    print("-" * 50)
    
    processed = process_prices(sample_prices, verbose=True)
    
    print("-" * 50)
    print(f"✓ Processed prices saved and logged")
    
    return processed


if __name__ == "__main__":
    main()
