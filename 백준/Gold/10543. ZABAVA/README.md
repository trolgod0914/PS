# [Gold II] ZABAVA - 10543 

[문제 링크](https://www.acmicpc.net/problem/10543) 

### 성능 요약

메모리: 114124 KB, 시간: 288 ms

### 분류

다이나믹 프로그래밍, 수학

### 제출 일자

2024년 1월 5일 23:00:19

### 문제 설명

<p>A new student dorm has been opened! It consists of M buildings, labeled with integers from 1 to M. the dorm is initially empty, but soon N students will be moving in at a rate of exactly one student per day.</p>

<p>Each time a new student moves in a building, a big party is being held inside that building. The noise of the party is equal to the number of students located inside the building. The dorm management is not particularly fond of noise, so they will occasionally empty a certain building to keep the parties at a reasonable noise level. They do this by moving all its residents to a completely different student dorm. The management can decide to do this after any day, but they realized that it doesn't pay off to do it more than K times.</p>

<p>Help the management! Knowing which buildings are being moved in by students, determine the minimal possible total noise level (the sum of noise levels of all N parties) that can be achieved with emptying some of the building at most K times.</p>

### 입력 

 <p>The first line of input contains the integers N (1 ≤ N ≤ 1 000 000), M (1 ≤ M ≤ 100) and K (1 ≤ K ≤ 500) from the task description.</p>

<p>The i<sup>th</sup> line, out of N in total, contains an integer from the interval [1,M]: the label of the building where a student is moving in on the i<sup>th</sup> day.</p>

### 출력 

 <p>The first and only line of output must contain the required minimal possible total noise level.</p>

