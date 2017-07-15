>>> movie = 'SupermanII', 1980, 'Batman', 1989			# create 'tuple'
>>> type(movie)
<class 'tuple'>
>>> movie
('SupermanII', 1980, 'Batman', 1989)

>>> movie[0] = 'SupermanI'					# tuple is 'immutable' type
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    movie[0] = 'SupermanI'
TypeError: 'tuple' object does not support item assignment

>>> movie_list = list(movie)					# tuple -> list : type conversion
>>> movie_list
['SupermanII', 1980, 'Batman', 1989]

>>> movie_list[1] = 1981					# list is 'mutable'
>>> movie_list
['SupermanII', 1981, 'Batman', 1989]

>>> tuple(movie_list)						# list -> tuple : type conversion
('SupermanII', 1981, 'Batman', 1989)

2017-07-01 Python Study Resumed
