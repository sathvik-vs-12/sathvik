class book: 
  def __init__(self,tittle,quantity,author,price):
    self.tittle=tittle
    self.quantity=quantity
    self.author=author
    self.price=price
  def _repr__(self):
    return f"book:{self.tittle},quantity:{self.quantity},author:{self.author}"
  
book1=book("book 1",12,"author",120)
book2=book("book 2",18,"author",130)
book3=book("book 3",19,"author",150)

print(book1)
print(book2)
print(book3)