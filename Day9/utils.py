#import model
import time
from typing import Callable,Any

#It check how long time function take
def measure_time(func:Callable)->Callable:
    def utils(*args,**kwargs)->Any:
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        return result,round(end_time-start_time,2)
    
    #return wrapper function
    return utils