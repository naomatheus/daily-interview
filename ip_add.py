# This problem was recently asked by Microsoft

# An IP Address is in the format of A.B.C.D, where A,B,C,D are all integers between 0 to 255.
# Given a string of numbers, return possible IP addresses you can make with that string by splitting into 4 parts of A,B,C,D

# Keep in mind that integers can't start with a 0! (except for 0)

# Input: 1592551013 
# Output: ['159.255.101.3', '159.255.10.13']

def first_check(str):
      ## convert string portion to int
    part_a = []
    for i in str:
        ip_int = int(i, base=10)
        
        # print(ip_int)
        if ip_int < 2 and ip_int != 0:
            # this is the IP fail condition, if a list like this cannot be created, then a final IP is not possible
            part_a.append(ip_int)
            # print(part_a)
        if len(part_a) == 0:
            return 'IP address could not be made'
    return part_a

        
print(first_check('1592551013'))
print(first_check('9569459694569'))

def ip_addresses(first_check, ip_parts=[]):
    # Fill this in. print ip_addresses('1592551013') 
    # parts a, b, c, ,d 
    ip = []
    part_a = []
    for i in str:
        ip_int = int(i, base=10)
        if ip_int < 2 and ip_int != 0:
            part_a.append(ip_int)
            print(part_a)
 
    # # >>> ['159.255.101.3', '159.255.10.13']

# ip_addresses('1592551013')

