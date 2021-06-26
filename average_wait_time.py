# Time: O(n)
# Memory: O(1)

class Solution:
    def averageWaitingTime(self, customers) -> float:
        current_time_elapsed =0
        running_wait_time = 0
        
        for i in range(len(customers)):
            customer = customers[i]
            
            arrival_time = customer[0]
            cooking_time = customer[1]
            
            if current_time_elapsed <= arrival_time:
                running_wait_time = running_wait_time +  cooking_time
                current_time_elapsed = arrival_time + cooking_time
            else:
                running_wait_time = running_wait_time  + (current_time_elapsed - arrival_time) + cooking_time
                current_time_elapsed = current_time_elapsed + cooking_time 
                
        return running_wait_time/len(customers)