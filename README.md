# Lysakovskiy_14_4
This repository is created to solve a problem in the practical work 4 of the subject "Introductory Practical Work".

## Dependencies
Make sure you have Python3 installed.
Before using repository, make sure you have installed [npyscreen](https://npyscreen.readthedocs.io) module installed.

## Instalation
1. Fork this repository on your pc;
3. ```git pull``` this directory on your computer.

## Launch 
in CMD opened in project directory write comand:
```
python main.py
```

## Usage
After program's launched you will see the window:
![Main Window](https://github.com/Cnerupb/Lysakovskiy_14_4/blob/main/readme_objs/Main%20Window.png)

Coordinates must be integer!
*x1, y1* - is coordinates of bottom left point of Rectangle;
*x2, y2* - is coordinates of top right point of Rectangle;
This description is working for second Rect.

When you edited all coordinate fields. Press OK button.
You will get 2 new fields at the botom of window, as result of calculation:
![Main Window with Union/Intersection labels](https://github.com/Cnerupb/Lysakovskiy_14_4/blob/main/readme_objs/Main%20Window%20with%20Answers.png)

## Details
### How can we count intersecion and union of 2D objects?
We use this functions:
```
def intersection(self, rect) -> int:
  """Count area of intersection with other rect
  
  Args:
      rect (Rect): Rect object
  
  Returns:
      int: area
  """
  def get_len(c_1_1, c_1_2, c_2_1, c_2_2):
      return max(0, min(c_1_2, c_2_2) - max(c_1_1, c_2_1))
  width = get_len(self.x_1, self.x_2, rect.x_1, rect.x_2)
  height = get_len(self.y_1, self.y_2, rect.y_1, rect.y_2)
  return width * height

def union(self, rect):
  """Count area of union with other rect
  
  Args:
      rect (Rect): Rect object
  
  Returns:
      int: area
  """
  return (self.area + rect.area) - self.intersection(rect)
```
This 2D task can be simplified in 1D solution using ```get len``` function.
It counts width and height of rectangle intersection by x and y coordinates.
Using Area formula:
```
S = width * height
```
We can easilly, firstly, count intersection and, secondly, count union of rectangles.

## Special Thanks
https://github.com/egorgur - for code documentation
