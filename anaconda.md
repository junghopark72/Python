## Anaconda Setup

### Anaconda를 이용한 환경설정

#### 1. 환경 생성
```
$ conda create -n env4stock python=3
$ conda info --envs
```
#### 2. 활성화
```
$ activate env4stock
```
#### 3. 필요한 라이브러리 설치
```
(env4stock) $ conda install numpy pandas matplotlib
(env4stock) $ conda install jupyter notebook
```
#### 4. 환경 삭제
```
(env4stock) $ deactivate
$ conda env remove -n env4stock
```
