# Global Interpreter Lock (GIL)



## 0. 멀티쓰레딩



​	일반적으로 멀티쓰레딩(multi-threading)은 하나의 프로세스에서 여러 개의 쓰레드를 생성, 병렬 처리를 수행하는 기능을 말한다. 여러 개의 쓰레드를 이용하여 작업을 분할 처리하면 수행시간을 줄일 수 있다. 하지만 항상 그런 건 아니다. 하나의 자원 또는 기능에 여러 개의 쓰레드가 동시에 접근해야 한다면 세마포어, 뮤텍스 등의 동기화 방법을 사용해야 한다. 



​	C++이나 C에서는 세마포어나 뮤텍스 라이브러리가 존재하며, 자바에서는 synchronized 지시자가 따로 존재하여 동기화 작업을 수행할 수 있다. 하지만 파이썬에서는 조금 상황이 다르다.



## 1. 멀티 쓰레딩 - 파이썬



​	파이썬에서는 일반적으로 멀티 쓰레딩이 비효율적인데, 그 이유는 여러 개의 쓰레드를 생성하더라도 특정 시점에서 바라 보았을 때는 여러 개의 쓰레드 중 하나의 쓰레드만 실행된다. 이는 파이썬 언어의 특성 자체에 있다.

![](https://mblogthumb-phinf.pstatic.net/MjAxOTA2MjBfMjYy/MDAxNTYxMDA4MjQ5ODk2.ons6KoRw-1j4HyLaUB4-h6G8z5OseQK4LqRcgZyNAxUg.DKGuizD64O1cwVJo5UcBHdi7FIk-D63eP45Pkd0tVlkg.PNG.alice_k106/gil1.png?type=w2)

​	파이썬은 객체를 관리 감독할 때, reference count를 이용하여 관리한다. 따라서, 객체를 참조하는 다른 객체 또는 위치가 늘어날 수록 해당 객체의 reference count가 증감하게 되며, reference count가 0이 되면 객체는 매모리에서 해제된다. 이것이 바로 파이썬의 가비지 콜렉터(Garbage Collector - GC)기능이다. 따라서, 멀티 쓰레딩 환경에서 각 쓰레드가 특정 객체에 접근할때, C++ 혹은 자바라면 특정 변수에 대해서만 동기화 처리를 수행하면 되지만, 파이썬은 객체의 메모리를 reference count를 이용하여 관리하기 때문에 모든 객체에 락을 걸어야만 reference count가 가능해질 것이다. 



​	이러한 문제를 해결하기 위해 위의 그림처럼 파이썬은 특정 시점에 하나의 쓰레드만 실행되도록 자체적인 락을 걸어 두었는데, GIL이 바로 이러한 기능을 의미한다. 자체적으로 락을 걸어 여러 쓰레드가 동시에 사용하는 공유 자원에 대한 문제는 해결되었지만, 실행 속도가 느려진다는 단점을 가지게 된 것이다.



## 2. 파이썬의 GIL으로 인한 성능 문제



​	파이썬에서 쓰레드를 전환하는 과정은 다음과 같다.



1. 내부 Interpreter을 통해 변환된 파이썬의 바이트 코드가 실행된다.

2. 일정한 틱(양)만큼 바이트코드가 실행될 때마다 다른 쓰레드로의 이동(Context Switching)이 발생한다.

   

Context Switching은 성능 오버헤드의 주범이기 때문에, 빠른 실행속도가 중시되는 환경에서 파이썬을 사용하는 것은 추천되지 않는다.

​	

​	그렇지만 이러한 Context Switching은 이점이 없는 건 아니다. 대표적으로 I/O작업에 의한 Blocking System Call이 있는데, 파일 읽기/쓰기와 같은 I/O작업 도중에는 I/O작업으로 인해 해당 지점에서 Blocking이 걸린다. 따라서 그 시간동안 다른 쓰레드에 실행 제어권을 넘겨 줌으로써 더욱 효율적인 프로세싱이 가능해진다.

![](https://mblogthumb-phinf.pstatic.net/MjAxOTA2MjBfMjA1/MDAxNTYxMDA4NjA3MDAx.2RCzMRC4kuln80wbLMASn8VvoZiejAiflRISIDOUEVsg.82aTojUYlO5znTI8PHI1nnFlK5dFE58sqTfclZSSnhsg.PNG.alice_k106/gil2.png?type=w2)



​	따라서, I/O작업이 많고 Blocking Point가 많을수록 파이썬에서의 멀티 쓰레딩 작업의 효율성이 그나마 올라간다고 볼 수 있고, CPU 작업이 많은 환경에서의 멀티 쓰레딩은 파이썬이 효율적이지 않을 수 있다.



참고 링크

[GIL에 대한 이야기] https://m.blog.naver.com/PostView.naver?blogId=alice_k106&logNo=221566619995&navType=by

[GIL 상당히 자세한 이야기] : http://openlook.org/wp/cb-1136/





