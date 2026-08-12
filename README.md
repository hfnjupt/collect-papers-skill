# Collect Papers Skill

面向学术论文检索、作者消歧、元数据核验与 Excel 整理的 Codex skill。它把“搜索到一些结果”变成可追溯、可复核的论文集合，适合通信、网络、多媒体、计算机视觉、人工智能、机器学习、数据挖掘、Web 与系统等方向。

## 能做什么
-主要是解决搜论文，然后确认某些已经下载好的论文文章中是否含代码下载链接，从而大幅缩减大家初筛选论文的时间；

- 按研究方向、关键词、作者、作者 + 单位，或从一篇已知论文扩展作者的成果进行检索。
- 支持发表年份/时间段和期刊/会议筛选；“优先”是软排序，“仅限/只搜索”是严格筛选。
- 对同名作者进行身份消歧，按 confirmed、probable、ambiguous、excluded 标记可信度。
- 用 DOI、规范题名、作者和年份去重，并优先保留正式发表版本。
- 生成带来源链接、英文摘要概述和中文翻译的 Excel。
- 对用户提供的本地 PDF 进行代码链接审查；可先生成报告，再隔离没有明确代码地址的文件。不会自动删除论文。

## 安装

在 Codex 中调用 $skill-installer，并提供本仓库地址：

~~~text
https://github.com/hfnjupt/collect-papers-skill
~~~

安装完成后，在下一轮对话中直接使用 $collect-papers。仓库根目录就是 skill 目录，包含 SKILL.md、references/、scripts/ 与 agents/。

## 常用用法

### 1. 按作者搜索

~~~text
$collect-papers 搜索作者“San Zhang，NUPT”的所有论文，并整理成 Excel。
~~~

skill 会先把 San Zhang 与南京邮电大学（NJUPT/NUPT/南京邮电大学等别名）作为身份线索，结合稳定作者 ID、论文时单位、合作者、研究主题和时间线进行消歧。对于“所有论文”，结果会说明检索来源、日期和覆盖边界，而不会在没有封闭数据库时声称绝对穷尽。

### 2. 按关键词搜索

~~~text
$collect-papers 搜索“semantic communication”方向的代表性论文，优先顶会顶刊。
~~~

引号中的内容按精确短语处理；未加引号的概念会扩展常见别名、相关方法和应用词。结果会区分字面命中与语义相关，并给出每篇论文的核验链接。

### 3. 年限 + 关键词

~~~text
$collect-papers 搜索 2021–2025 年发表、题目或摘要包含“cross-modal communication”的论文，优先 IEEE TMM、IEEE IoT Journal、ACM Multimedia 和 ICME。
~~~

也可以使用严格过滤：

~~~text
$collect-papers 仅限 2023–2025 年 CVPR、ICCV、ECCV 和 WACV 中包含“video saliency”的论文。
~~~

### 4. 从一篇感兴趣的论文扩展作者

~~~text
$collect-papers 以 DOI 10.xxxx/xxxx 为锚点，搜索其中 San Zhang 的全部论文；只保留论文发表时单位为 NJUPT 的记录。
~~~

这种模式会保留锚点论文、作者顺序、单位映射及身份关联证据，并将无法确证的同名记录单列。

### 5. 审查已下载论文中的代码链接

~~~text
$collect-papers 审查 C:\\papers 下的 PDF，筛选出正文或注释中明确提供代码仓库地址的论文；先生成报告，不要删除任何文件。
~~~

只有在用户明确提供本地 PDF 且要求全文审查时，skill 才会核验代码或数据集信息；普通在线检索不会把“网页未显示代码”误判为“论文没有代码”。

## 输出样式

默认先在对话中给出紧凑清单：

| Paper | Year | Venue | Match reason | Contribution | Identifier/link |
|---|---:|---|---|---|---|

作者检索会先给出身份卡片，并为每条记录标记身份判定。需要 Excel 时，默认工作簿包含以下字段：

| 字段 | 说明 |
|---|---|
| 论文题目 | 去重后的正式发表题名 |
| 作者 | 保留原始作者顺序；可核验的一作/通讯作者在同一单元格内标记 |
| 作者单位 | 保留论文印刷的单位及可用的作者—单位映射 |
| 期刊/会议 | 仅保留场刊名称，不额外添加卷期页 |
| 英文摘要 / 英文摘要概述 | 来自权威来源；受版权或访问限制时使用明确标记的概述 |
| 中文摘要翻译 | 忠实翻译或概述翻译，不添加原文没有的结论 |
| 年份 | 发表年份 |
| 来源链接 | 出版社、DOI、会议或权威索引页面 |
| 核验备注 | 元数据冲突、单位映射、访问限制等说明 |
| 身份判定 | 仅作者检索包含，且始终位于最后一列 |

默认在线 Excel **不包含** 单独的一作/通讯作者栏、卷期页、DOI 栏、代码、代码状态、数据集或数据集地址。只有用户明确要求并提供正式全文、补充材料或官方项目页时，才会进行代码/数据集的全文增强核验。

## 内置优先检索期刊与会议

下列列表是“优先检索与排序”配置，不会自动排除其他已核验且相关的论文；只有明确使用“仅限”“只搜索”等措辞时才变成严格范围。

### 期刊

- IEEE Journal on Selected Areas in Communications (JSAC)
- IEEE Transactions on Wireless Communications (TWC)
- IEEE Transactions on Communications (TCOM)
- IEEE Communications Surveys & Tutorials
- IEEE/ACM Transactions on Networking
- IEEE Transactions on Mobile Computing (TMC)
- IEEE Internet of Things Journal
- IEEE Transactions on Network and Service Management (TNSM)
- IEEE Communications Letters
- IEEE Wireless Communications Letters
- IEEE Transactions on Multimedia (TMM)
- IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)
- IEEE Transactions on Image Processing (TIP)
- IEEE Transactions on Signal Processing (TSP)
- IEEE Signal Processing Letters (SPL)

### 通信、网络、多媒体与信号处理会议

IEEE GLOBECOM、IEEE ICC、IEEE INFOCOM、ACM SIGCOMM、ACM MobiCom、IEEE WCNC、IEEE PIMRC、IEEE VTC、IEEE ICME、IEEE ICIP、IEEE ICASSP、ACM Multimedia Systems (MMSys)。

### 计算机视觉会议

CVPR、ICCV、ECCV、WACV。

### 人工智能与机器学习会议

NeurIPS、ICML、ICLR、AAAI、IJCAI。

### 多媒体、数据挖掘、Web 与系统会议

ACM Multimedia、ACM KDD、The Web Conference（WWW）、NSDI、OSDI、SOSP、EuroSys、USENIX ATC。

## 检索与核验原则

- 至少结合两个互补来源进行发现和复核，优先使用出版社、DOI、会议论文集、机构库等权威记录。
- 对单位限制按**论文发表时**的作者单位判断，不用当前主页单位回填早期论文。
- 对“作者全部论文”采用高覆盖、可审计表述；除非有完整封闭数据库和可复现查询，否则不声称绝对全部。
- 不从标题或搜索摘要臆测论文贡献、代码或数据集；缺失信息会明确标为未获得或待核验。
