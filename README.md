# Nordic AI & Open Data Hackathon (18-19 of March 2022)

### Intelligent Real-time Accident Warning System (IRAWS)

The project uses transfer learning (base model: EfficientNetB1) with deep learning to train a model to detect unusual events (skids, vehicles off-street, and on the wrong lane). To this end, images from the cameras of the Nordic countries' highways provided in the dataset were used. The team generated fake images from these real ones to simulate the unusual events. The last layer of the base model (classes) was eliminated, and the model was retrained to identify roads with normal flow and unusual events.

## [Code](https://colab.research.google.com/drive/1JdVmQ0kCw9Bqq_jKEYyZOD5ZCLBaZJMP#scrollTo=TJOoSNR1wQK8) [Pitch](https://www.canva.com/design/DAE7X42Qc-A/zB6M_xdH8WDGLdmbv8dRoA/view?utm_content=DAE7X42Qc-A&utm_campaign=designshare&utm_medium=link&utm_source=sharebutton) [MVP](https://image2alarm.herokuapp.com/)

## Team:

[Matheus Correia](https://github.com/matheusgomesms) (transportation specialist)  
[Minh Anh Huynh](https://github.com/MarcX23) (full stack dev/speaker)  
[Tiago Tamagusko](https://github.com/tamagusko) (backend dev/transportation specialist)  

## Problem

Identify vehicles that have slipped, veered off the road, or are on the wrong lane.

## Concept

![Concept](https://github.com/tamagusko/nordicaiopendataimages/raw/main/img/concept.png)

## MVP
[image2alarm.herokuapp.com/](https://image2alarm.herokuapp.com/)  
![MVP](https://github.com/tamagusko/nordicaiopendataimages/raw/main/img/mvp.gif)  
[Youtube](https://youtu.be/xKLlYaEs0Bc)

---

Codes and data are protected. Please see [LICENSE](LICENSE) for details.
