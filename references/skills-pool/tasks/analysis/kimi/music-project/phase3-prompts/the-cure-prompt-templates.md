# The Cure 风格 - Suno/Udio Prompt 模板

> Phase 3 产物：基于 Phase 2 风格配方的可直接使用 Prompt
> 工具: Suno (suno.ai) 或 Udio (udio.com)
> 日期: 2026-04-24

---

## 使用说明

### 模板语法
- `[变量]` : 需要替换的内容
- `|选项1|选项2|` : 多选一
- `(可选)` : 可省略的部分

### 生成策略
1. **先用基础模板生成**，听效果
2. **记录差距**：哪里像？哪里不像？
3. **迭代调整**：替换变量，添加/删除描述词
4. **保存成功版本**到个人配方库

---

## 模板 1: The Cure 通用基础版

### 音乐风格描述 (Style of Music)
```
1980s British post-punk and alternative rock, The Cure style. 
Prominent melodic bassline, chorused and flanged electric guitars with heavy reverb, 
1980s electronic drums with tom fills, icy synth pads. 
[|A minor|D minor|E minor|], [medium-fast|fast] tempo around [120-160] BPM.
[Melancholic yet catchy|Bittersweet and dreamy|Dark but danceable] atmosphere.
Emotive British tenor vocals with slight nasal quality.
```

### 歌词主题 (Lyrics Theme)
```
[|Love and loss|Memory and time|Existential longing| bittersweet romance|].
[|Short, poetic lines|Conversational verses|Abstract imagery|].
Mood shifts from [|hope to despair|intimacy to distance|calm to anxiety|].
```

### 完整 Prompt 示例

#### 示例 A: A Forest 风格（阴郁/存在主义）
```
Style: 1980s British post-punk, The Cure "A Forest" style. 
A minor, 160 BPM, driving mechanical rhythm. 
Prominent melodic bass riff, chorused guitar with heavy reverb, 
minimal icy synth pads, tom-heavy electronic drums. 
No traditional chorus, verse-based structure with gradual intensity build.
Atmospheric, haunting, existential mood.

Lyrics: A first-person narrative about being lost in a forest at night, 
chasing someone who isn't there. Short, stark lines. 
Themes: emptiness, repetition, the void. 
Key words to include: dark, trees, lost, alone, again, never, running.
```

#### 示例 B: Lovesong 风格（治愈/承诺）
```
Style: 1980s British alternative rock, The Cure "Lovesong" style. 
A minor verse to F major chorus, 140 BPM. 
Galloping melodic bassline, clean chorused guitar, warm synth pad, 
steady post-punk drums. Standard verse-chorus structure.
Warm, sincere, gently melancholic but hopeful mood.

Lyrics: A straightforward love declaration, repetitive structure. 
"Whenever I'm alone with you..." format. 
Themes: healing, wholeness, unconditional commitment. 
Key words: always, home, whole, free, clean, love, again.
```

#### 示例 C: Just Like Heaven 风格（狂喜/梦幻）
```
Style: 1980s British alternative pop, The Cure "Just Like Heaven" style. 
A major, 120 BPM, bright and driving. 
Distinctive opening guitar riff, energetic bass, ethereal keyboard melody, 
bouncy drums with reverb. Verse-chorus with instrumental bridge.
Dreamy, euphoric, romantic but tinged with sadness.

Lyrics: Surreal romantic imagery, dialogue format. 
Themes: love as transcendence, dreams vs reality, the fleeting nature of bliss. 
Key words: dream, heaven, angels, ocean, alone, far away, drowned.
```

#### 示例 D: Friday I'm In Love 风格（快乐/解放）
```
Style: 1990s British alternative pop, The Cure "Friday I'm In Love" style. 
D major, 135 BPM, upbeat and jangly. 
Jangly bright guitars, bouncy bass, handclaps, cheerful synth accents, 
pop drums. Infectious verse-chorus with wordplay bridge.
Joyful, carefree, celebratory mood.

Lyrics: Playful lyrics about escaping weekly drudgeon through love. 
Days of the week personified. Themes: liberation, everyday magic. 
Key words: Friday, love, blue, grey, smile, surprise, never hesitate.
```

#### 示例 E: Pictures Of You 风格（悲伤/怀旧）
```
Style: 1980s British gothic rock ballad, The Cure "Pictures Of You" style. 
A minor, 75 BPM, extremely slow and spacious. 
Minimal instrumentation: icy sustained synth chords, gentle flanged guitar, 
subtle bass, sparse drums. Funeral-paced, atmospheric.
Deeply melancholic, nostalgic, mournful mood.

Lyrics: Memories triggered by photographs, longing for someone lost. 
Long, image-rich lines. Themes: time, regret, the unreliability of memory. 
Key words: pictures, remembering, lost, cold, dark, breaking apart, if only.
```

---

## 模板 2: 参数化万能公式

### 步骤 1: 选择基础情绪
```
[阴郁/Existential] → 用小调 (Am/Em), 140+ BPM, 驱动节奏
[苦乐/Bittersweet] → 用小调转大调, 120-140 BPM, 流行结构  
[明亮/Bright] → 用大调 (D/A), 120-135 BPM, 弹跳节奏
[悲伤/Slow] → 用小调, <80 BPM, 极简编曲
```

### 步骤 2: 填入乐器描述
```
Bass: [driving melodic|galloping|subtle minimal]
Guitar: [jangly bright|chorused ethereal|flanged dreamy|muted tense]
Drums: [tom-heavy post-punk|bouncy pop|sparse minimal|electronic 80s]
Synth: [icy pads|bright accents|circling arpeggios|none]
```

### 步骤 3: 填入歌词指令
```
Theme: [your theme here]
Structure: [V-C-V-C-B-C | V-V-Bridge-V-Outro | freeform]
Tone: [first-person confession | dialogue | abstract imagery | narrative]
Mood arc: [build up | up-down-up | steady | fade down]
Required words: [word1, word2, word3]
Forbidden words: [baby, oh yeah, club, party] (The Cure 从不用这些)
```

---

## 模板 3: 纯歌词生成 Prompt（用于 Suno 的 Custom Lyrics 模式）

### The Cure 风格歌词生成器 Prompt

将此 Prompt 输入 Claude/GPT，生成歌词后粘贴到 Suno 的 Custom Lyrics：

```
你是一位像 Robert Smith（The Cure 主唱）那样的歌词创作者。

请创作一首 [3-4] 分钟的歌词，主题为：[用户主题]。

必须遵循以下规则：
1. 整体情绪: [| bittersweet melancholy | dark romanticism | existential longing | euphoric sadness |]
2. 使用 [| A minor | D minor | E minor |] 的调性暗示（歌词情绪匹配）
3. 诗句每行 6-10 个英文单词
4. 必须包含以下 The Cure 式高频词中的至少 3 个: always, never, again, away, close, dark, dream, eyes, fear
5. 使用以下至少 2 种修辞手法:
   - 矛盾/反讽 (如 "boys don't cry")
   - 感官隐喻 (如 "daylight licked me into shape")
   - 重复+递进 (如 "home again, whole again, free again")
   - 条件句遗憾 (如 "if only I'd thought of the right words")
   - 身体化情感 (如 "it froze me deep inside")
6. 结构:
   - Verse 1: 4-6 行，场景/叙述
   - Chorus: 2-4 行，情绪核心，重复
   - Verse 2: 4-6 行，深入/转折
   - Chorus
   - [Bridge: 2-4 行，意象转换 (可选)]
   - Chorus/Outro
7. 禁用词: baby, oh yeah, club, party, dj, drop, lit, vibes (这些词不属于 The Cure 世界)
8. 整体感觉要像 1980s 英国后朋克/另类摇滚，不是美国摇滚，不是现代流行

输出格式：标注 Verse/Chorus/Bridge。
```

---

## 模板 4: 快速 Suno 标签版

如果你只想要最精简的 Prompt（Suno 的 Style 栏）：

```
# 阴郁型
The Cure, post-punk, gothic rock, A minor, 1980s, melodic bass, chorused guitar, ethereal, melancholic, British vocals

# 流行型
The Cure, alternative rock, jangly pop, bright guitars, 1980s, emotive vocals, bittersweet, catchy bassline

# 慢速型
The Cure, gothic ballad, slow tempo, atmospheric, icy synth, minimal drums, haunting, spacious, A minor

# 快乐型
The Cure, alternative pop, upbeat, jangly guitars, bouncy bass, handclaps, joyful, 1990s British pop
```

---

## 迭代记录表（Phase 3 核心实践工具）

| 轮次 | 使用的 Prompt | 生成结果评价 | 差距分析 | 调整方向 |
|------|--------------|-------------|----------|----------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| ... | | | | |

### 常见差距与对策

| 问题 | 可能原因 | 调整方案 |
|------|----------|----------|
| "不像 The Cure，像 generic indie" | 缺少 1980s 音色描述 | 添加 "1980s", "chorused guitar", "electronic drums" |
| "太现代了" | 缺少时代限定 | 明确添加 "1980s British", 禁用现代制作词汇 |
| "太快乐了，没有忧郁感" | 大调+快速 BPM | 切换到小调，添加 "melancholic", "bittersweet" |
| "歌词太 generic" | 缺少 The Cure 词汇约束 | 在歌词 Prompt 中指定高频词和禁用词 |
| "贝斯不够突出" | 缺少 bass 描述 | 添加 "prominent melodic bassline", "Simon Gallup style" |
| "吉他音色不对" | 缺少效果器描述 | 添加 "heavy reverb", "chorus effect", "flanged" |

---

*本模板基于 Phase 2 风格配方，可直接用于 Suno/Udio 生成。建议每轮生成后填写迭代记录表，逐步逼近目标风格。*
