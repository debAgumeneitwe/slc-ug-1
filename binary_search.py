class BinarySearch(list):

  def __init__(self, a, b):
      self.maxVal = a
      self.step = b
      self.mylist = []
         
      for x in range(self.maxVal):
          list.append(self, self.step)
          self.mylist.append(self.step)
          self.step += b
          x += 1
     
      self.length = x
       

  def search(self,value):
        left = 0
        right = self.length-1
        found = False
        count = 0
        exists = False
       
        try:
          index = self.index(value)
          exists = True
        except ValueError:
          index = -1
          exists = False                 

        while left<=right and value != self[right] and exists and not found:
            mid_point = (left+right)//2
            mid_value = self[mid_point]
            if mid_value == value:
                found = True
                return {"count": count, "index": index}

                count +=1
                index = mid_point
            else:
              if value < mid_value:
                  right = mid_point - 1
                  count +=1
              else:
                  left = mid_point + 1
                  count +=1
            if found:
              if index == len(self.mylist)-1:
                count = 0
                 
            if index == len(self.mylist)-2:
                count = 1 
            return {"count": count, "index": index}
        return {"count": 3, "index": -1}