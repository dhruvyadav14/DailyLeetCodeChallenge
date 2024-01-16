def halvesAreAlike(self, s: str) -> bool:
    vowelSet = set(['a','e','i','o','u'])
    return sum(1 for char in s[:len(s)//2] if char.lower() in vowelSet) == sum(1 for char in s[len(s)//2:] if char.lower() in vowelSet)
