def abctract(one:str)->int:
    result = 0
    one = int(one)
    if one > 0:
        if one <= 100_000:
            result = one - one * 0.05
            return result
        elif one <= 1_000_000:
            result = one - one * 0.08
            return result
        else:
            result = one - one * 0.15 
            return result
    else:
        return "no profit"        
        
         


print(abctract("100_000_000")) 
                             
        
        


