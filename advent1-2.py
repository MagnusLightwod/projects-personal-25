import sys

def main():

    start = 50
    ans = 0
    print("test")
    for lines in open("advent.txt").read().strip().splitlines(): # read in lines, strip \n, make list of each line. 
        
        diff = int(lines[1:]) # find the value we are turning
        if lines[0] == "L": # if left we go backwards or negative 
            diff*=-1
        start = (start + diff) % 100 
        ans += start == 0
        
        # if it goes over or under the end values the modulo 100 should emulate wrapping around a combo lock.        
        
   
    print(ans)

if __name__ == "__main__":
    main()