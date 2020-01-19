# The 급식 programming language
**저는 한국어를 사랑합니다.**

GeubsikPy는 Python 으로 작성된, [급식어](https://github.com/GeubsikLang/GeubsikLangSpec) 의 소스 간 컴파일러입니다.

컴파일 결과로 Python 코드가 출력됩니다.

`너가만든거.기모띠`
```text
헬로월드는 "Hello, world!"인거 ㅇㅈ? ㅇㅇㅈ~
앙 헬로월드띠~
```

```text
$python ㄱㄱ.py run 너가만든거.기모띠
Hello, world!
$python ㄱㄱ.py build 너가만든거.기모띠
...
```

더 많은 예제는  [테스트 폴더](https://github.com/GeubsikLang/GeubsikPy/tree/master/tests)에서 찾을 수 있습니다.

또는 [콜라츠 추측](https://ko.wikipedia.org/wiki/%EC%BD%9C%EB%9D%BC%EC%B8%A0_%EC%B6%94%EC%B8%A1) 을 구현한 예가
아래에 있으니 참고하세요.

## 콜라츠 추측의 구현

![콜라츠 추측의 함수 표현](https://wikimedia.org/api/rest_v1/media/math/render/svg/ecc542a0a334586327e54f3e2501ca9832434245)
```
대상숫자 이거 ㄹㅇ ㅆㅎㅌㅊ 인거 ㅇㅈ? ㅇㅇㅈ~ㅋ
횟수는 0인거 ㅇㅈ?ㅇㅇㅈ

와 방금 개꿀잼 시나리오 생각해냄 대상숫자 != 1?
대상숫자 % 2 == 0일 때 시청자들이 역으로 몰카하는거임
대상숫자는 대상숫자 / 2인거 ㅇㅈ?ㅇㅇㅈ~
그런데 갑자기 분위기 싸해지는거임
대상숫자는 (대상숫자 * 3) + 1인거 ㅇㅈ?ㅇㅇㅈ~ㅋ
유튭각 ㅇㅈ?
횟수는 횟수+1인거 ㅇㅈ?ㅇㅇㅈ
방금 상상한건데 스토리 ㅍㅌㅊ?

앙 횟수, "번 만에 성공!!"띠~ㅋ
```

## 써보고싶어요?
그러지 마세요

## 해야 할 것들
 - [x] 조건문
 - [ ] 삼항연산자
 - [ ] 형변환
 - [ ] 대입연산자
 - [x] 표준입력 (형변환 지원되지 않음)
 - [x] 함수 미정인자
 - [ ] return/break/continue
 - [x] 반복문
 - [x] 표준출력
 - [x] 변수
 
 # License
Licensed under the MIT License

Copyright 2019 Donghyeok Tak
