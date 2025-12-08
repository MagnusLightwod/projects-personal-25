

# def main():

#     advent_input = []

#     # open file then conver left and right to negative and positive inputs
#     with open("advent.txt") as advent:
#         for x in advent:
#             if (x[0] == "R"):
#                 x = x.strip()
#                 x = x[1:]
#                 x = int(x)
#                 advent_input.append(x)
#             else:
#                 x = x.strip()
#                 x = x[1:]
#                 x = int(x) * -1
#                 advent_input.append(x)
        
    
#     # convert inputs to integers, can put negative in front of left? 
#     # if input + current exceeds 99 then 
#     # print(advent_input[-1])
#     safe = []
#     for i in range((100)):
#         safe.append(i)

#     # print(advent_input[0][0])
#     start = safe[51]
  
  
#     for i in range(len(advent_input)):
       
#         new_value = start + advent_input[i]
#         diff = 0
#         if ( new_value > 99):
#             diff = new_value - 99
#         if ( new_value < 0):
#             diff = -1(0 - new_value)
        
        
        

# if __name__ == "__main__":
#     main()