# AI_Uninformed_and_Informed_Searches
(Fall 2024 AI Assignment 1)

## Description:

Use **`A* algorithm and one uninformed search algorithm (BFS)`** of your choice to search for a path given a pair of source and destination cities.

We assume that connected cities have a straight path between them.

- The coordinates of the cities are provided in cities.csv
  
- Download cities.csv and open this document with ReadSpeaker docReader, while the connectivity between the cities is provided in roads.csv
  
- Download roads.csv and open this document with ReadSpeaker docReader.
  
- You should expect these two files to be in the same folder as your code.

 ##

For A*, use the haversine distance(which can be ruled out from the longitudes and latitudes) between the cities as the heuristic function.

Use kilometers as the unit of distance and cost.

##

Your program is expected to take two arguments, the first is the source city and the second is the destination.

In order words, we will run your program like this:

```bash
python [YourCode].py city_name_1 city_name_2
```

##

The output of your program should include the path found and the corresponding total distance of the path, in the following format (Say we are going from Dalhart to San Antonio):

```bash
Dalhart - Amarillo - Lubbock - San Angelo - San Antonio

Total Distance - [Some Number]
```
 

In case no path is found (If you are implementing an incomplete searching algorithm), your program should output:

```bash
Path not found!
```
