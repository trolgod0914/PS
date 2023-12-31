# [Gold III] 생태학 - 13257 

[문제 링크](https://www.acmicpc.net/problem/13257) 

### 성능 요약

메모리: 113576 KB, 시간: 180 ms

### 분류

조합론, 다이나믹 프로그래밍, 수학, 확률론

### 제출 일자

2023년 11월 27일 17:01:04

### 문제 설명

<p>생태학에서 주어진 영역의 개체수를 추정하는 방법은 여러 가지가 있다. 이번 문제에서는 새의 개체수를 구해볼 것이고 다음과 같은 방법을 사용할 것이다.</p>

<p>먼저, 데이터 수집은 D일동안 진행된다. 초기에 모든 새에 측정기를 부착되어있지 않다. 데이터 수집이 진행되는 동안 매일 매일 C마리의 새를 잡을 것이다. 그 다음, C마리의 새 중에 측정기가 부착되어 있지 않은 새에는 측정기를 부착할 것이고, 이미 부착되어 있는 새는 그냥 놔둘 것이다. 그 다음 하루가 끝날 때, 모든 새를 다시 풀어준다.</p>

<p>데이터 수집 기간이 끝나면, 측정기가 부착되어 있지 않은 새를 이용해서 새의 개체수를 측정할 것이다.</p>

<p>데이터를 수집한 영역의 새의 개체수가 N마리라고 가정했을 때, 데이터 수집 기간이 끝난 후에 측정기가 부착되어 있는 새의 수가 M마리일 확률을 구하는 프로그램을 작성하시오. 데이터 수집이 진행되는 동안, 매일 매일 모든 새를 잡을 확률은 같다.</p>

### 입력 

 <p>첫째 줄에 N, C, D, M이 주어진다. (1 ≤ N ≤ 20, 1 ≤ C ≤ 20, 1 ≤ D ≤ 5, 0 ≤ M ≤ N)</p>

### 출력 

 <p>데이터를 수집한 영역의 새의 개체수가 N마리라고 가정했을 때, 데이터 수집 기간이 끝난 후에 측정기가 부착되어 있는 새의 수가 M마리일 확률을 출력한다. 정답과의 절대/상대 오차는 10<sup>-9</sup>까지 허용한다.</p>

