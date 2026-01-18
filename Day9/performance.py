#import model
from scanner import scan_website
from scanner.utils import measure_execution_time

#this is measure execution time
@measure_execution_time
def performance_scan(url:str):
    return scan_website(url)

#this test multiple websites
def run_performance_scan():
    websites={
       "Fast website (google.com)": "https://www.google.com",
       "Slow website": "https://example.com",
       "Error website": "https://invalid-test-url.com"
    }

    total_time=0

    #scan each website
    for name,url in websites.items():
        result,scan_time=perform_scan(url)
        total_time +=scan_time
        
        #show result
        print(f"\n{name}")
        print("Result:",result)
        print("Scan time(seconds):",scan_time)

    #it show average time
    average_tiem=round(total_time/len(websites),2)

    print("\nAverage scan time:", average_time)
    print("Estimated memory usage: Low (few MB)")
    print("Main bottleneck: Network request latency")
    
if_name_=="__main__":
    run_performance_tests()
