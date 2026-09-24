import copy

class Book:
  def __init__(self, title, author, year):
    self.title = title
    self.author = author
    self.year = year

  # 1. __str__: מגדירה איך האובייקט ייצג את עצמו כמחרוזת (למשל כשמדפיסים אותו)
  def __str__(self):
    return f"'{self.title}' מאת {self.author} ({self.year})"

  # 2. __eq__: מגדירה מתי שני ספרים נחשבים שווים בתוכן שלהם ולא רק בכתובת הזיכרון
  def __eq__(self, other):
    if isinstance(other, Book):
      # ספרים שווים אם יש להם אותו שם ואותו מחבר
      return self.title == other.title and self.author == other.author
    return False

  # 3. __copy__: מגדירה איך ליצור העתק שטחי (Shallow Copy) של האובייקט
  def __copy__(self):
    return Book(self.title, self.author, self.year)



# ==========================================

# הרצת הקוד והדגמת כל אחת מהמתודות

# ==========================================


book1 = Book("אלגוריתמים בפייתון", "ישראל ישראלי", 2024)

book2 = Book("אלגוריתמים בפייתון", "ישראל ישראלי", 2024)

book3 = Book("מבני נתונים", "דנה לוי", 2022)


print("--- 1. הדגמת __str__ ---")

# ברקע נקראת המתודה book1.__str__()

print(book1)

# פלט: 'אלגוריתמים בפייתון' מאת ישראל ישראלי (2024)


print("\n--- 2. הדגמת __eq__ ---")

# השוואה בעזרת == מפעילה את המתודה __eq__

print(f"האם book1 שווה ל-book2? {book1 == book2}")  # פלט: True

print(f"האם book1 שווה ל-book3? {book1 == book3}")  # פלט: False


print("\n--- 3. הדגמת __class__ ---")

# גישה לתכונה __class__ מחזירה את סוג המחלקה בזמן ריצה

print(f"הסוג של book1 הוא: {book1.__class__}")

print(f"שם המחלקה הוא: {book1.__class__.__name__}")

# פלט: שם המחלקה הוא: Book


print("\n--- 4. הדגמת __copy__ ---")

# השימוש במודול copy מפעיל את המתודה __copy__ שרשמנו במחלקה

book_copy = copy.copy(book1)


print(f"הספר המועתק: {book_copy}")

print(

    f"האם התוכן שווה? {book1 == book_copy}"

)  # True (ה-__eq__ בודק שוויון תוכן)

print(

    f"האם אלו שני אובייקטים שונים בזיכרון? {book1 is not book_copy}"

)  # True (כתובות זיכרון שונות)