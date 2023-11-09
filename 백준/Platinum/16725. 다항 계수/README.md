# [Platinum V] 다항 계수 - 16725 

[문제 링크](https://www.acmicpc.net/problem/16725) 

### 성능 요약

메모리: 112576 KB, 시간: 224 ms

### 분류

조합론, 다이나믹 프로그래밍, 수학, 누적 합

### 제출 일자

2023년 11월 9일 23:54:03

### 문제 설명

<p><strong>다항 정리</strong>(multinomial theorem)는 다항식의 거듭제곱을 전개하는 정리이며, 전개식의 계수를 <strong>다항 계수</strong>(multinomial coefficient)라고 한다. 우리가 다룰 다항식은 모든 항의 계수가 1인 경우이고, 아래는 그 예시이다.</p>

<p style="text-align: center;">(1 + x + x<sup>2</sup>)<sup>3</sup> = 1 + 3x + 6x<sup>2</sup> + 7x<sup>3</sup> + 6x<sup>4</sup> + 3x<sup>5</sup> + x<sup>6</sup></p>

<p>다항정리를 일반화 하면, 다음과 같이 나타낼 수 있다.</p>

<p style="text-align: center;">(1 + x + ... + x<sup>n</sup>)<sup>m</sup> = a<sub>0</sub>x<sup>0</sup> + a<sub>1</sub>x<sup>1</sup> + ... + a<sub>nm</sub>x<sup>nm</sup></p>

<p>어떤 수 k(0 ≤ k ≤ n × m)가 주어졌을 때 x<sup>k</sup>의 계수 a<sub>k</sub>를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫 번째 줄에 음이 아닌 정수 n(0 ≤ n ≤ 500), m(1 ≤ m ≤ 500), k가 주어진다.</p>

### 출력 

 <p>첫 번째 줄에 x<sup>k</sup>의 계수를 출력한다. 단, 수가 커질 수 있으므로 1,000,000,009로 나눈 나머지를 출력한다.</p>

