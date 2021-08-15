# README

### 2021.8.16 讨论

*   emsemble
    *   把同一个sess的物品打乱，然后分别过网络，再ensemble
*   data aug
    *   把同一个sess的物品打乱
*   feature
    *   价格分桶，然后每个桶做 emb
    *   预测 sess 多一个三个 sess (mean, sum, ...) pooling 后的 feature
    *   userclick pooling time decay (越接近权重越大)
*   模型：
    *   FM
    *   预测 click 数据，丰富了item之间的交互 （multitask, pretrain）
*   Loss：
    *   reweight loss (4种行为)





### 一些模型分析



*   看一下，如果sess直接用gt，分数能有多少
    *   如果 sess 有 gt（知道 0, 1, 2, 3），那么 acc 会从 0.337 -> 0.435。并且，这个修正会使得 单点的 acc 从 0.809 -> 0.908
    *   ![image-20210816013843205](source/image-20210816013843205.png)

*   sess prediction Confusion Matrix
    *   ![image-20210816014202087](source/image-20210816014202087.png)
*   cnt prediction confusion matrix
    *   ![image-20210816014150833](source/image-20210816014150833.png)
*   per item confusion numbers
    *   <img src="source/image-20210816014121337.png" alt="image-20210816014121337" style="zoom:67%;" />





### 一些信息

看起来是对应到了这里描述的“神秘商店”：[基于玩家实时交互的游戏道具推荐 - 伏羲实验室用户画像组开放课题 (gitbook.io)](https://fuxi-up-research.gitbook.io/open-project/research_topics/rl_based_recommendation)

<img src="source/image-20210713163121342.png" alt="image-20210713163121342" style="zoom: 33%;" />

<img src="source/image-20210713163216578.png" alt="image-20210713163216578" style="zoom:33%;" />

