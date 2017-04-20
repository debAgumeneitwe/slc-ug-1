def find_missing(list1, list2):
    missing_number = []

    if list1 == list2:
        return 0
    
    elif list1 == [] and list2 == []:
        return 0

    else:
        for num in list1:
            if not num in list2:
                missing_number.append(num)
             
        for num in list2:
            if not num in list1:
                missing_number.append(num)
        return missing_number[0]
                
    

    
    
     
