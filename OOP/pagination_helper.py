class PaginationHelper:
  '''The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. 
  The types of values contained within the array are not relevant. '''

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
    self.collection, self.items_per_page = collection, items_per_page
        
  
  # returns the number of items within the entire collection
  def item_count(self):
      return len(self.collection)
  
  # returns the number of pages
  def page_count(self):
    from math import ceil
    return ceil(self.item_count() / self.items_per_page)
      
    
  # returns the number of items on the current page. page_index is zero based
  # this method returns -1 for page_index values that are out of range
  def page_item_count(self, page_index):
    self.count = self.item_count()
    self.pages = {}
    for i in range(0, self.page_count()):
        if self.count >= self.items_per_page:
            self.pages[i] = self.items_per_page
            self.count -= self.items_per_page
        else:
            self.pages[i] = self.count
    return self.pages.get(page_index, -1)        
  
  # determines what page an item is on. Zero based indexes.
  # this method returns -1 for item_index values that are out of range
  def page_index(self, item_index):
    if 0 <= item_index <= self.item_count()-1:
        return int(item_index / self.items_per_page)
    else:
        return -1


# Example
# helper = PaginationHelper(['a','b','c','d','e','f'], 4)   

# helper.page_count() == 2
# helper.item_count() == 6
# helper.page_item_count(0) == 4
# helper.page_item_count(1) == 2
# helper.page_item_count(2) == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
# helper.page_index(5) == 1 (zero based index)
# helper.page_index(2) == 0
# helper.page_index(20)== -1
# helper.page_index(-10) == -1 because negative indexes are invalid