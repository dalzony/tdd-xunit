- **테스트 메서드 호출하기**
- setUp 호출하기
- 나중에 tearDown호출하기
- 테스트 메서드가 실패하더라도 tearDown 호출하기
- 여러 개의 테스트 실행하기
- 수집된 결과를 출력하기

```markdown
테스트 메서드가 호출되면 true
그렇지 않으면 false
부트 스트랩 테스트를 하려면(아마도 자동화된 테스트?)
플래그를 가지고 있는 테스트 케이스를 만들어야 함 (wasRun)
assert test.wasRun

```