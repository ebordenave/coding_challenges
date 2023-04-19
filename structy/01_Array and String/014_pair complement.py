def pair_product(numbers, target_product):
    prev = {}
    
    for key, value in enumerate(numbers):
        complement = target_product // value
        
        if complement in prev:
            return (key, prev[complement])
        
        prev[value] = key