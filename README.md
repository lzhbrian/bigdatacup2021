# README



### ideas 

*   tta

    -   [x] 把同一个sess的物品打乱，然后分别过网络，再做平均（可带来大约 0.002 的提升，不太稳定）

        | aug  | buy real acc2                                                |      |
        | ---- | ------------------------------------------------------------ | ---- |
        | no   | 0.36028                                                      |      |
        | 2    | 0.36281, 0.36089, 0.35997, 0.36178, 0.36204, 0.36063, 0.36304, 0.36158, 0.36086, 0.36292 |      |
        | 3    | 0.36500, 0.36465, 0.36319, 0.36074, 0.36143, 0.36139, 0.36508, 0.36342, 0.36139, 0.36342, 0.36081, 0.36419, 0.36350, 0.36170, |      |
        | 5    | 0.36217, 0.36400, 0.36350, 0.36431, 0.36347, 0.36224, 0.36158, 0.36231, 0.36216 |      |
        | 10   | 0.36020, 0.36262, 0.36258, 0.36201, 0.36216, 0.36216, 0.36208 |      |
        | 216  | 太多了，不试了                                               |      |

*   data aug

    -   [x] 把同一个sess的物品打乱（没有明显的提升，但还是默认加上了）

*   feature

    -   [x] 价格分桶，然后每个桶做 emb（貌似提升了一小点，不明显）
    -   [ ] 预测 sess 多一个三个 sess (mean, sum, ...) pooling 后的 feature

    -   [ ] userclick pooling time decay (越接近权重越大)

    *   [ ] **考虑时间也作为feature（可能需要先做个 EDA），数据描述里说：The training data is collected across three months and includes several sales campaigns (release new items).**
    *   [ ] **用user_emb来搞？让testset也做一个click的train，然后学到的emb去predict buy。**
    *   [ ] 似乎一个user会有多条记录（3条？），然后用上面的思路来学user_emb

*   模型：

    *   [x] Transformer（大概0.36 -> 0.365 的提升，还行，估计还能再升点，没继续训了，因为去搞multitask click了）
        *   [ ] **Transformer 搞一个小一点的模型看看效果会不会下降**
    *   [ ] GNN（网易fuxi有发一篇paper做bundle recommendation 用gnn的，和这个场景有一丢丢类似）
    *   [x] 预测 click 数据，丰富了item之间的交互做 multitask（0.362->0.365； 加上augorder3：0.365 -> 0.368 左右）
        *   [ ] **使得 click 的 neg sample 更合理（现在是随机，可能采集到正样本）**
    *   [ ] DIN 的 elementwise attention
    *   [ ] 现在是分别预测buy和sess，然后两者合并输出；是否可以直接将两者合并，e2e 来 backpropagate优化？
    *   [ ] ~~预测 sess 时，现在：1000，0100，0010，0001；改成：1000，0100，0110，0111；
        incremental 的预测 sess（这个初步试验了一下，貌似没啥用）~~

*   Loss：

    -   [ ] reweight loss（4种行为）：
        -   [x] [0.5, 1.0, 1.0, 0.5] weight，0.365 -> 0.388 提升显著（没augorder）
    -   [ ] reweight pos and neg

*   trick：

    -   [x] 2epoch0.001adam -> 10epoch0.001adam+10epoch0.0001adam：0.33->0.36
    -   [ ] batchsize调大？ lr调大？ 优化器？





### 一些模型分析



*   看一下，如果sess直接用gt，分数能有多少。
    *   如果 sess 有 gt（知道 0, 1, 2, 3）
        *   acc 会从 0.337 -> 0.435；新模型：0.36 -> 0.46
        *   单点的 acc 从 0.809 -> 0.908
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

