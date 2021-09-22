# CS2450-001-Fall2021-Team2
 Repository for Team 2 Now. Primarily code, and its associated documentation. Repository name will not be changed, as I cannot be bothered to.

# How to Run
  Navigate to the folder CS2450-001-Fall2021-Team2 in the console. `python main.py` will output the payroll to the console, and to the file "payroll.txt" in the folder.

# Coding Design
  Code is done in Python, following the PEP-8 standard, and uses the
  [Model-View-Controller]{https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller}
   design pattern. It is important to note that models are simply the objects.
   The controllers will handle all our "Repositories" which we've separated for
   easier designing.

## Seems like a lot of effort!
  It is! However this design pattern helps us abstract the data easier, while
  also helping up all improve our understanding of a critical design pattern.

## OOP or Functional?
  The "backend" will primarily be functional, this provides the easiest testing
  ability. We see this approach in the controller level. Where we treat them as
  simply functions that we can import to use*

  *Singleton approach to the Repositories will aid this, needs implementation.

## Credits
  Original Source Code is based on the source code provided on the Canvas Page.
  That code was designed and made by both Dana Doggett and Chuck Allison. With
  additional code provided by Craig Sharp (Professor).
