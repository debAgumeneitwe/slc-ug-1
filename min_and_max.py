def find_max_min(array):
    while isinstance(array, list):
        x = min(array)
        y = max(array)
        min_max = []
        if x == y:
            return [len(array)]
        else:
            min_max = [x,y]
            return min_max
        break
        
        
