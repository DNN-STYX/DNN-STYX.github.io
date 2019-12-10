---
layout: default
---

**STYX** is a general mutation framework to improve the robustness of DNN. The framework is used to improve the DNN’s robustness under different adversarial attacks. We instantiate Styx to image classification DNNs and a set of general pixel-level mutation rules is proposed. We also compared the three different training methods: mutation training, traditional training and adversarial training, showing that our method is effective. 

* * *

*   [**Installation**](install)

*   [**Tutorial**](tutorials)

*   [**API Documentation**](api)

*   [**Docker Image**](https://1drv.ms/u/s!Amd07GCbYt_zbQZm2w2MBbXI6Zo)

*   [**Manual for the Docker Image**](dockerManual)

*   [**Github Repo**](https://github.com/DNN-STYX/DNN-STYX)

* * *


# [](#header-1)**Video**

<iframe width="560" height="315"
 src="./video/test.mp4" frameborder="0" allowfullscreen>

 </iframe>

* * *

# [](#header-1)**Setup**

Environment Requirement:

*   <font color="#0000FF" size="4">Ubuntu 16.04</font>
*   <font color="#0000FF" size="4">CUDA=10.1</font>
*   <font color="#0000FF" size="4">cuDNN=7.6</font>
*   <font color="#0000FF" size="4">gcc＝4.8</font>


* * *
# [](#header-1) **Get Start with STYX**

Examples of using STYX can be found in [**Github Repo**](https://github.com/DNN-STYX/DNN-STYX.github.io/tree/master/demo). It provides an example for training the MLP models w.r.t. MNIST benchmark under three different methods (traditional training, mutation training, and adversarial training) and then making the robustness evaluation. The example can be run with the following command, which takes about 15 mins:

```
cd Examples
bash run_example.sh
```
In more detail, we consider that in three steps:

## [](#header-1) 1.model's description

```
cd STYX/traditional_training
```
First we need to provide the model's structure like [**Train\_mnist\_MLP.py**](https://www.baidu.com/)  in the current folder. 


## [](#header-1) 2.model's generation
Given the paramters like model\_name="mnist\_MLP" and train\_epoch=20. Next we use the following command to generate the models by different training method.

### [](#header-1) (1) traditional_training

```
cd STYX/traditional_training
python traditional_training.py $model_name $train_epoch
```
### [](#header-1) (2) mutation_training

```
cd STYX/mutation_training
python mutation_training.py $model_name $train_epoch 
```
### [](#header-1) (3) adversarial_training

```
cd STYX/adversarial_training
python adversarial_training.py $model_name $train_epoch
```

## [](#header-1) 3.model's evaluation
After that, we use the following command to evaluate the models by different attacking method. Take the attacking method "FGM" as example:

```
cd STYX/evaluation  
python evaluation.py ["FGM"]
```

And the evaluation result is stored in evaluation.xls under evaluation folder.

