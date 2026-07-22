class AppSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.currency = "ETB"
        return cls._instance


# Create two instances
settings1 = AppSettings()
settings2 = AppSettings()

# Print the currency
print("Currency:", settings1.currency)

# Confirm they are the same object
print("Are they the same object?", settings1 is settings2)