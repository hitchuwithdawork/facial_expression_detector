# facial_expression_detector

### 프로젝트 소개
웹캠을 통해 사용자의 얼굴을 인식하고 모델이 분류한 표정을 바탕으로 사용자에게 특정한 표정에 맞는 음성 메시지를 출력하는 프로그램 구현 프로젝트.

### 사용 데이터
FER2013 dataset + Google image 크롤링 (Asian)
약 3만개 이미지
https://www.kaggle.com/datasets/msambare/fer2013

### 사용 기술
- 전처리, 시각화 : Pandas, Numpy, Matplotlib
- 모델링 : Keras - CNN

---
### 참고 논문
*  Byung Joo Kim .Improved Deep Learning Algorithm.JOURNAL OF ADVANCED INFORMATION TECHNOLOGY AND CONVERGENCE,8(2),119-127. 2018
*  Viola, Paul, and Michael Jones. "Rapid object detection using a boosted cascade of simple features." Proceedings of the 2001 IEEE computer society conference on computer vision and pattern recognition. CVPR 2001. Vol. 1. Ieee, 2001.

### 참고 링크
* https://github.com/leblancfg/autocrop
* https://github.com/JustinhoCHN/keras-image-data-augmentation
