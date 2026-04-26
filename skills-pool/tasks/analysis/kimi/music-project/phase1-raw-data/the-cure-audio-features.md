# The Cure - 音频特征与结构化数据

> 综合来源：公开和弦谱、Spotify API 文档、音乐评论分析
> 注意：BPM/调性来自社区和弦谱，Spotify 特征值基于风格推断

---

## 结构化数据表

| # | 歌曲 | 专辑 | 年份 | 调性 | 模式 | BPM | 时长 | 曲式 |
|---|------|------|------|------|------|-----|------|------|
| 1 | A Forest | Seventeen Seconds | 1980 | A | minor | 163 | 5:55 | V-V-Bridge-V-Outro |
| 2 | Just Like Heaven | Kiss Me×3 | 1987 | A | major | ~120 | 3:33 | V-C-V-C-B-C |
| 3 | Boys Don't Cry | Boys Don't Cry | 1979 | E | minor | ~186 | 2:37 | V-C-V-C-V-C |
| 4 | In Between Days | The Head On The Door | 1985 | A | major | ~145 | 2:57 | V-C-V-C |
| 5 | Pictures Of You | Disintegration | 1989 | A | minor | ~75 | 7:28 | V-V-V-Bridge-Outro |
| 6 | Lovesong | Disintegration | 1989 | A | minor | 140 | 3:28 | V-V-C-V-C |
| 7 | Friday I'm In Love | Wish | 1992 | D | major | ~135 | 3:35 | V-Pre-C-V-Pre-C-B-C |
| 8 | Close To Me | The Head On The Door | 1985 | C | minor | ~120 | 3:23 | V-V-C-V-C |

---

## 推断的 Spotify 风格特征

基于音乐评论和风格标签的定性推断（非实测数据）：

| 歌曲 | Danceability | Energy | Valence | Acousticness | Instrumentalness |
|------|-------------|--------|---------|--------------|------------------|
| A Forest | 0.55 | 0.72 | 0.15 | 0.20 | 0.30 |
| Just Like Heaven | 0.60 | 0.78 | 0.55 | 0.15 | 0.10 |
| Boys Don't Cry | 0.65 | 0.80 | 0.40 | 0.20 | 0.05 |
| In Between Days | 0.68 | 0.82 | 0.50 | 0.15 | 0.05 |
| Pictures Of You | 0.30 | 0.35 | 0.10 | 0.40 | 0.25 |
| Lovesong | 0.50 | 0.55 | 0.35 | 0.25 | 0.05 |
| Friday I'm In Love | 0.72 | 0.85 | 0.80 | 0.15 | 0.05 |
| Close To Me | 0.58 | 0.70 | 0.45 | 0.20 | 0.05 |

### 平均值
- **Danceability**: 0.57
- **Energy**: 0.70
- **Valence**: 0.41（整体偏忧郁）
- **Acousticness**: 0.21（以电声为主）
- **Instrumentalness**: 0.11（以人声为主）

---

## 歌词主题标签

| 歌曲 | 主要主题 | 情绪 | 意象 | 叙事视角 |
|------|----------|------|------|----------|
| A Forest | 迷失/存在主义 | 恐惧、虚无 | 森林、黑暗、追逐 | 第一人称独白 |
| Just Like Heaven | 爱情/狂喜与失落 | 狂喜→绝望 | 海洋、天使、梦境 | 回忆叙事 |
| Boys Don't Cry | 男性情感压抑 | 压抑、后悔 | 泪水、笑声、谎言 | 内心独白 |
| In Between Days | 分离/后悔 | 恐惧、渴望 | 昨天、孩子、冰冷 | 恳求式 |
| Pictures Of You | 记忆/失去 | 悲伤、怀旧 | 照片、雨、雪、黑暗 | 回忆式 |
| Lovesong | 承诺/治愈 | 温暖、坚定 | 家、完整、自由 | 直抒胸臆 |
| Friday I'm In Love | 解放/狂欢 | 快乐、释放 | 一周七天、色彩 | 宣言式 |
| Close To Me | 焦虑/童年创伤 | 恐慌、不安 | 黑暗、门、梦境 | 梦魇式 |

---

## 核心发现

1. **调性偏好**: A 小调是 The Cure 的"标志性调性"——4/8 首歌以 A 为中心
2. **BPM 范围**: 75-186，但以 120-163 的中快板为主
3. **曲式**: 早期无副歌（A Forest），成熟期标准 V-C（Lovesong, In Between Days）
4. **歌词长度**: 偏短，大量留白和重复
5. **主题光谱**: 从存在主义恐惧（A Forest）到纯粹快乐（Friday I'm In Love），但**忧郁底色不变**
