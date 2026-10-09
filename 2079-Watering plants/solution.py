class Solution(object):
    def wateringPlants(self, plants, capacity):
        steps = 0
        current_water = capacity

        for i, need in enumerate(plants):
            if current_water < need:
                steps += i * 2
                current_water = capacity
            
            steps += 1
            current_water -= need
        
        return steps