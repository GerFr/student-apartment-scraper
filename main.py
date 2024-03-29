from fizz import rooms_available as fizz_available
from ilive import rooms_available as ilive_available

URL_FIZZ  = "https://www.the-fizz.com/search/?searchcriteria=BUILDING:THE_FIZZ_HAMBURG_STUDENTS;AREA:HAMBURG" 
URL_ILIVE = "https://www.urban-living-hamburg.de/mieten"

print(fizz_available(URL_FIZZ))
print(ilive_available(URL_ILIVE))
