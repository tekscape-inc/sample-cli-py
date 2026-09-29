def greet(name: str, *, shout: bool = False) -> str:
    greeting = f"Hello, {name}!"
    return greeting.upper() if shout else greeting
