def increment_counter(current_value: int) -> int:
    """Pure logic. Can be tested easily."""
    return current_value + 1

def create_user(username: str):
    # Imagine database logic here
    print(f"Saved {username} to DB")
    return True
