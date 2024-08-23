# 1657 - Medium
## Determine if Two Strings are Close

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
<br/>
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
<br/>
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
<br/><br/>

#### Example 1:

Input: word1 = "abc", word2 = "bca"<br/>
Output: true<br/>
Explanation: You can attain word2 from word1 in 2 operations.<br/>
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"<br/>
<br/>

#### Example 2:

Input: word1 = "a", word2 = "aa"<br/>
Output: false<br/>
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.<br/>
<br/>

#### Example 3:

Input: word1 = "cabbba", word2 = "abbccc"<br/>
Output: true<br/>
Explanation: You can attain word2 from word1 in 3 operations.<br/>
Apply Operation 1: "cabbba" -> "caabbb"<br/>
Apply Operation 2: "caabbb" -> "baaccc"<br/>
Apply Operation 2: "baaccc" -> "abbccc"<br/>
<br/>

#### Constraints:

- 1 <= word1.length, word2.length <= 105
- word1 and word2 contain only lowercase English letters.
