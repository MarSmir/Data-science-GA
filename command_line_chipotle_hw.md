## Homework: Command line Chipotle

#### 1
    head data/chipotle.tsv
    tail data/chipotle.tsv
    
    Each column represents the type of information that is given in tsv files, while each row is an entry for each column.
    
#### 2
    tail -1 data/chipotle.tsv
    
    This gives us the very last row entry of the file. From there we can look at the first column(i.e order_id) to see how many unique orders were made.
    
#### 3
    wc -l data/chipotle.tsv

#### 4
    grep "chicken burrito" -i data/chipotle.tsv | wc -l
    grep "steak burrito" -i data/chipotle.tsv| wc -l
    
    From the commands above we get chicken burrito was the most popular.

#### 5
   grep "chicken burrito" -i data/chipotle.tsv | grep "pinto beans" -i | wc -l
   grep "chicken burrito" -i data/chipotle.tsv | grep "black beans" -i | wc -l
   
   Black Beans are the most popular

#### 6
   grep -r  *.{csv, tsv} .
   
#### 7
    grep -r "dictionary" -i . | wc - l
    