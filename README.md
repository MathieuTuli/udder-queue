# Udder Queue #

## motivation ##
This project was motivated when I came across a synchronization problem in a multiprocessed/multithreaded system I was building. Essentially, I had a data source. A thread, spawned in a child process from the main 'System' process you could call it, would continuously generate data. From there, there could be any number of 'Feeders' you could call them, that needed to digest that data. Each of these 'Feeders' processed the data at different rates, but what was critical was that each 'feeder' always processed the same data as the others. Meaning, 
