# Given all three lists, write a function to check that my service is first-come, first-served. All food should come out in the same order customers requested it.

# My Solution

def first_come_first_serve(dine_in, take_out, served):
    dine_in_idx = 0
    take_out_idx = 0
    served_orders_idx = 0

    for order in served:
        if dine_in_idx <= len(dine_in) - 1 and dine_in[dine_in_idx] == served[served_orders_idx]:
            dine_in_idx += 1
        
        elif take_out_idx <= len(take_out) - 1 and take_out[take_out_idx] == served[served_orders_idx]:
            take_out_idx += 1
        
        else:
            return False
    
    return True