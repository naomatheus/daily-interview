# This problem was recently asked by Microsoft

# An IP Address is in the format of A.B.C.D, where A,B,C,D are all integers between 0 to 255.
# Given a string of numbers, return possible IP addresses you can make with that string by splitting into 4 parts of A,B,C,D

# Keep in mind that integers can't start with a 0! (except for 0)

# Input: 1592551013 
# Output: ['159.255.101.3', '159.255.10.13']
part_a = []
def first_check(str):
      ## convert string portion to int
    
    for i in str:
        ip_int = int(i, base=10)
        
        # print(ip_int)
        if ip_int < 2 and ip_int != 0:
            # this is the IP fail condition, if a list like this cannot be created, then a final IP is not possible
            part_a.append(ip_int)
            print(part_a)
        if len(part_a) == 0:
            return 'IP address could not be made'
    return str

# print(first_check('1592551013'))
# print(first_check('9569459694569'))

## ip addresses takes in a verified string, verified to ensure it can become an ip address, else returns cannot be made


def ip_addresses(ip_str, ip_parts=[]):
    # Fill this in. print ip_addresses('1592551013') 
    # parts a, b, c, ,d 
    print(ip_str,'<-- passed')
    ## append another number to each index in the part_a, if that number will not exceed value of 255.
    for j in part_a:
        j = str(j)
        
        print(type(j))
        
    part_b = [k + j for k in ip_str]
    print(part_b, '<-- part b')
    # for i in ip_str:
    #     if i >= 0:
            
        # https://www.geeksforgeeks.org/python-concatenate-two-lists-element-wise/


#####    ## IF part_b goes beyond length of 4, start the loop over and reconcat the #s 

    # # >>> ['159.255.101.3', '159.255.10.13']
    return ip_str


print(ip_addresses(first_check('1592551013')))