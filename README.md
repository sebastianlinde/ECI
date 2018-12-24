# Economic Complexity Index (ECI)
The ECI package allows you to comute the economic complexity index for any bi-partite network configuration.  This code was used in the project: **Li, Linde and Shimao (2018), *Major to Occupation Networks: The Importance of Specificity*, Mimeo.**  If you use this package we ask that you please cite the above work. 

![ECI_flow.pdf](ECI_flow.png)

## Usage example

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

_For more examples and usage, please refer to the [Wiki][wiki]._


|Major \ Occupation| Occ1:Theorist| Occ2:Accountant| Occ3:Journalist| Occ4:Service |
|--------------------|:----------:|:---_----------:|:--------------:|:------------:|
|Major 1: Math       |     5      |        3       |         1      |      1       |
|Major 2: Accounting |     0      |        10      |         0      |      0       |   
|Major 3: English    |     0      |        0       |         8      |      2       |   
|Major 4: Arts       |     0      |        0       |         0      |      10      |
|Major 5: Economics  |     1      |        2       |         2      |      5       | 


```
|Major \ Occupation|                   Occ1:Theorist Occ2:Accountant Occ3:Journalist Occ4:Service

 Major 1: Math            5              3                1            1
 Major 2: Accounting      0              10               0            0          
 Major 3: English         0              0                8            2          
 Major 4: Arts            0              0                0            10
 Major 5: Economics       1              2                2            5 


########
# Part1: Using BINARY Adjacency matrix:
########
```

```python
iterations = 24
AdjData = np.array([[ 5,  3,  1,  1],[ 0, 10,  0,  0],[ 0,  0,  8,  2],[ 0,  0,  0, 10],[ 1,  2,  2,  5]],dtype='f')
[ECI_Maj_All, ECI_Occ_All] = ECI.eci_compute((AdjData>0)*1,iterations)
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
The economic complexity index was first put forth in the context of country-trade data by Hidalgo and Hausmann (). See and reference 
Hidalgo and Hausmann, 2009, *The building blocks of economic complexity*, Proceedings of the National Academy of Sciences Jun 2009, 106 (26) 10570-10575; DOI: 10.1073/pnas.0900943106
