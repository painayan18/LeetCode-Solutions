# 735 - Medium

## Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning
right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both
are the same size, both will explode. Two asteroids moving in the same direction will never meet.
<br/><br/>

#### Example 1:

Input: `asteroids = [5,10,-5]`<br/>
Output: `[5,10]`<br/>
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.<br/>
<br/>

#### Example 2:

Input: `asteroids = [8,-8]`<br/>
Output: `[]`<br/>
Explanation: The 8 and -8 collide exploding each other.<br/>
<br/>

#### Example 3:

Input: `asteroids = [10,2,-5]`<br/>
Output: `[10]`<br/>
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.<br/>
<br/>

#### Constraints:

- `2 <= asteroids.length <= 104`
- `-1000 <= asteroids[i] <= 1000`
- `asteroids[i] != 0`