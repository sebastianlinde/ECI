# Economic Complexity Index (ECI)
The ECI package allows you to comute the economic complexity index for any bi-partite network configuration.  This code was used in the project: **Li, Linde and Shimao (2018), *Major to Occupation Networks: The Importance of Specificity*, Mimeo.**  If you use this package we ask that you please cite the above work. 

![ECI_flow.pdf](ECI_flow.png)

## Usage example

Suppose you have an adjacency matrix linking the number of students from a given major (rows) that end up in a particular occupation (columns) as seen below.  Here, for example, we see that there were a total of 10 students with Mathematics as their major--5 of these ended up working as a Theorist, 3 as Accountants, while 1 became a Journalist and 1 went into a service occupation. 

|Major \ Occupation| Occ1:Theorist| Occ2:Accountant| Occ3:Journalist| Occ4:Service |
|--------------------|:----------:|:--------------:|:--------------:|:------------:|
|Major 1: Mathematics|     5      |        3       |         1      |      1       |
|Major 2: Accounting |     0      |        10      |         0      |      0       |   
|Major 3: English    |     0      |        0       |         8      |      2       |   
|Major 4: Arts       |     0      |        0       |         0      |      10      |
|Major 5: Economics  |     1      |        2       |         2      |      5       | 

The ECI package takes adjacency matrices like this and uses it to calculate the ECI on both the major and the occupation sides. It works both in cases where we want to estimate the weighted ECI or the unweighted ECI (using a simple binary adjacency matrix).  

Looking at the case where we want a ***binary input matrix*** we can use the following Python code:

```python
iterations = 24
AdjData = np.array([[ 5,  3,  1,  1],[ 0, 10,  0,  0],[ 0,  0,  8,  2],[ 0,  0,  0, 10],[ 1,  2,  2,  5]],dtype='f')
[ECI_Maj_All, ECI_Occ_All] = ECI.eci_compute((AdjData>0)*1,iterations)
```

To obtain the results for the ***weighted ECI case*** we instead use:
```python
iterations = 24
AdjData = np.array([[ 5,  3,  1,  1],[ 0, 10,  0,  0],[ 0,  0,  8,  2],[ 0,  0,  0, 10],[ 1,  2,  2,  5]],dtype='f')
[ECI_Maj_All, ECI_Occ_All] = ECI.eci_compute((AdjData>0)*1,iterations)
```
```
	|0|	2	|4	|6|	8|
|:---:|:---:|:---:|:---:|:---:|
|Math	|2	|1	|1|	1	|1|
Account	|5	|5	|5	|4	|4|
Eng	|3	|2	|2	|2	|2|
Arts|	|5	|4	|4	|5|	5|
Econ|	2|	3	|3	|3	|3

```


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
The economic complexity index was first put forth in the context of country-trade data by Hidalgo and Hausmann (). See and reference 
Hidalgo and Hausmann, 2009, *The building blocks of economic complexity*, Proceedings of the National Academy of Sciences Jun 2009, 106 (26) 10570-10575; DOI: 10.1073/pnas.0900943106
