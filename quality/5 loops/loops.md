# Loops

As a programmer you have both the luxury and the burden of choosing just what tools you use to solve a particular problem. For instance, what loop do I use? Choosing the right type at the right time will make your code easier to understand. In general we suggest these guidelines but use your best judgement in a given situation:

- Prefer a for-loop to a while-loop when there is an obvious loop variable, or if you know in advance just how many times you want the loop to iterate.
- Prefer a while-loop to a for-loop when there is no obvious loop variable.
- Prefer a while-loop to a do-while-loop when you can check the condition before entering the loop.

In case of a for-loop, do not modify the loop variable inside the loop. That way you can deduce how many times a for-loop iterates by looking at its signature, and not its body. 
