More Distance Based Indexing
============================

today "Near Neighbor Search in Large Metric Spaces" by Sergey Brin

VP Tree
-------

- Binary tree that recursively partition data space using
    - vantage points
    - distances of data points to vantage points
- Internal nodes: (Xvp, M, Rptr, Lptr) where
    - M: median distance amount d(Xvp, Xi)


Near Neighbor Search in VP Trees
--------------------------------

Given a query point q, a distance metric d(.,.) and a tolerance factor r,

- Find all datapoints x such that d(x,q) <= r
    1. if d(q, x) <= r then x is in the answer set
    2. if d(q, x) - r <= M then recursively search the left branch
    3. if d(q, x) + r >= M then recursively search the right branch

all three of these things could be true at once

VP Trees [Yianilos 1993] Summary
--------------------------------

- Construction : recursively
    - break the space up using spherical cuts
    - pick a point called the vantage point
    - consider the median sphere center at the vp
- Benefits and Drawbacks:
    + One distance calculation when visiting a node during a search
    + Automatically balanced tree
    - Extremely asymmetric especially in high-dimensional space
        -> limits the amount of pruing
    - Branching factor of two

GNAT Geometric Near Neighbor Access Tree
----------------------------------------

- Sergey Brin's VLDB 1995
- Data Structure
    - captures the geometry of the data collections
    - hierarchically break it down into regions

Typically a generalization of gh-trees [Uhlmann 1991] and Fukunaga's Method

Generalized Hyperplane Tree (gh-tree)
-------------------------------------

- Construction : recursively
    - at the top node pick two points
    - divide the remain points based on closest distance
- Benefits and Drawbacks:
    - (+) Symmetric division
    - (+) tends to be well balanced in the tree structure
    - (-) Two distance computations at every node during a search
    - (-) Branching factor of two : limited

- improved version of gh-tree: Monotonous Bi-Sector Tree [Bugnion et. all, 1993]
    - Pick one new point at each new node, reuse points from parent node
    - Used for text search especially!

Most Relevant Work but Old
--------------------------

[K. Fukunaga, IEEE Trans. of Comp. 1975]

- Data Structure
    - more than just a metric space (vector space)
    - tree structure with an arbitrary branching factor
- Building a Tree
    - Divid the data points into k groups (left as a parameter of the structure)
    - Computer the mean of each group
    - The farthest distance from the mean to a point in the group
    - Recursively creat the structure for each group

GNAT
----

- A Generalization of Kukunaga's Method and GH-Trees
- Good query performance
    - Exploits the geometery of the data
    - Query time : reduced
- Building time of the data structure
    - sharply increased
    - (relatively negligible if query dominant, ie as many or more queries as data points)
    - Finds the boundary blocks of the group
        - used for pruning
        - reduces query time
- Experimental Results
    - Almost always better performance than
        - vp tree
        - gh tree
    - scales better

Arbitrary Metric space
----------------------

- Assumptions
    - Given a Data set Y, and "black box" dist to computre the distance betweeen member of Y
    - Y can be preprocessed using dist
    - Queries are of the form (x, r): find members of y within istance r of x.
- Distribution of the data set in the metric space
    - : more important than the metric space itself
    - (in constrast to vector spaces ??)
        - in vector space you can use lines parallel to the axes to partition the data
    - in metric spaces
        - you have to take account the shape the of the data
- e.g. Data lies on the 2D surface embedded in 50D space
    - intelligent data structure: query times will behave like in a 2D space

High Dimensional Metric Space
-----------------------------

- The geometry of a given dataset
    - visualizing high-dimensional data == difficult

How to understand the geometry of given data set

- A Simple Measure
    - Distribution of the distance between random points of data
        - helps to determine the range for finding near neighbors
    - Probability Density Function
        - see slides was distracted

GNAT
----

We know the distribution, we know the distance function, and we know sensible query ranges

- Data structure
    - reflects the hierarchiical intrinsic geometry
        - top node : several split points are chosen
        - space is broken into Dirichlet domains based on split points
            - How close the nodes are to the split points
        - rest of the points are assiged to Drichlet domains they fall into.
    Basically, GNAT has hierarchical Dirichlet domain based structure
    - Full use of the distances we calculate
        - Prune branches by storing the ranges of distances

- Construction
    - Choose k split poitns
    - Associate each wof the remain points iwht the closest points
    - blah
    - blah
    - see slides i am loosing the thread of this lecture sorry

- A Search
    - Find all points with distance < r to a give point x
        1. let P represnts the set of split points of the current node and pick point p in P
        2. if dist(x, p) < r add p to the result
        3. fall al points q <= P
            if [dist(x, p) - r, dist(x, p) + r]&range(p, d) is empty
            then remove q from P
        4. BLAH
        5. BLAH
