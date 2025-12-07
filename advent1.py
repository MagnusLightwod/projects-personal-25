

def main():

    advent_input = []

    with open("advent.txt") as advent:
        for x in advent:
            advent_input.append(x)
    
    # convert inputs to integers, can put negative in front of left? 
    # if input + current exceeds 99 then 
    # print(advent_input[-1])
    safe = []
    for i in range((100)):
        safe.append(i)

    # print(advent_input[0][0])
    print(safe[-1])

if __name__ == "__main__":
    main()