# binary-search-app
CISC 121 Final Project

# Algorithm Name 
 Binary Search Interactive App 

# Demo Vid / Screenshot of Test

Click to view screen recording demo of how it works : https://raw.githubusercontent.com/claireleeyan/binary-search-app/main/demo.mp4

# Problem Breakdown and Computational Thinking

  1. Decomposition: What smaller steps form your algorithm?
    Take a sorted list for the input, either in increasing or decreasing order.
    Ask the user for a target number to search for. 
    Set “low” to the start of the list, “high” to the end.
    Check the middle value of the list (using floor division to find the middle).
    If target < middle, search the left half of the list only. 
    If target > middle, search the right half of the list only. 
    If target = middle, target is found. 
    Repeat until target is found, or search space becomes empty (target not in list). 
  
  2. Pattern Recognition: How does it repeatedly compare or swap values?
    The algorithm halves the data repeatedly and also repeatedly compares each step’s target value to the midpoint value. 
    After each step/comparison, half of the list is no longer under consideration, making binary search a fast algorithm, especially for larger datasets. 
  
  3. Abstraction: What details are simplified for the user?
    User only needs to enter a sorted list as well as a singular target value. 
    All inner workings and steps, e.g low/high pointers, loops, indexing, etc are hidden.
    App just returns the index at which the target is found, or “value not found”, making the experience simple and user friendly.
  
  4. Algorithm Design: How will input → processing → output flow?
    Input (sorted numbers and target value).
    Processing (binary search will repeatedly halve list to find value).
    Output (displays whether the number exists, as well as the index). 

   5. Why Binary Search?
I chose to implement binary search because of its efficiency and relevance to the real world. It is a searching algorithm that is able to quickly narrow down results (e.g as opposed to linear search, which needs to check every element one at a time). This makes it very useful when working with large, organized datasets. As someone interested in the world of finance, this type of algorithm is useful for data driven industries and work such as searching financial records, tracking product inventory, etc, where speed and accuracy matter. I believe it could very easily, possibly, and usefully be implemented into versatile industries and is extremely applicable to everyday jobs, and doing a deeper dive on it through this project gave me the opportunity to see how such computational tools can support business processes. Overall, binary search stood out to me as an excellent technical choice, as well as one that aligns with my future professional interests. 

# Steps to Run 

1. Open the app on Hugging Face (link provided below)
2. In the first text box, enter a list of integers, and make sure to seperate them by commas
3. Enter the target value you want to look for
4. Hit "submit"
5. The program output will show the steps of binary search it is performing, and play a positive sound effect if the target is found!

# Hugging Face Link

https://huggingface.co/spaces/claireleeyan/binary-search

# Author 
Claire Leeyan, 20462779. 
CISC 121 - 001 

  
