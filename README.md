# SVGedit


myarea for the time being works only on curves containing cubic brezier curves and line elements. 

it has two fucntions. 
Both take input in the format of, whatever goes inside the 'd' of your path element, i.e 
'M int int c int int int int int int'

curvy returns a list of lists where the input has been converted from relative to absolute and has been split into individual cubic brezier curves, including the lines. 

areacal takes that list of lists and calculates the area under the curve for each brezier curve in that list. Thus, it can calculate the area under a set of cubic brezier curves forming a closed curve. 
