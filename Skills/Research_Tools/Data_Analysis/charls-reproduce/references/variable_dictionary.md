# CHARLS Harmonized 完整变量速查

按功能分组，仅列出论文复现中常用的变量。

## 人口学

| 变量 | 类型 | 值 | Wave1 缺失 |
|------|------|-----|-----------|
| `ID` | string | 受访者唯一标识 | 0 |
| `householdID` | string | 家庭标识 | 0 |
| `communityID` | string | 社区标识 | 0 |
| `wave` | category | wave1-wave5 | 0 |
| `age` | float | 11-101 | 140 |
| `ragender` | category | 男性/女性 | 2 |
| `rabyear` | float | 出生年份 | 140 |
| `rabmonth` | float | 出生月份 | 239 |
| `raeduc_c` | category | 未完成小学/小学/中学/高中及以上 | 15 |
| `raeducl` | category | 低于初中学历/高中和职业培训/高等教育 | 15 |
| `marry` | category | 已婚/已婚但不住在一起/丧偶/离异/分居/从未结婚/同居 | 33 |
| `hrural` | category | 农村/城市 (户籍) | 0 |
| `rural2` | category | 农村/城市 (居住地) | 45 |
| `hukou` | category | 户口类型 | 35 |
| `province` | string | 省份 | 0 |
| `city` | string | 城市 | 0 |
| `region` | string | 地区 | 0 |

## 认知功能

| 变量 | 类型 | 范围 | Wave1 缺失 | 说明 |
|------|------|------|-----------|------|
| `imrc` | float | 0-10 | 3505 | 即时回忆 |
| `dlrc` | float | 0-10 | 3626 | 延迟回忆 |
| `recall` | float | 0-10 | 3698 | = (imrc+dlrc)/2 |
| `ser7` | float | 0-5 | 3425 | Serial 7 (连续减7) |
| `orient` | float | 0-4 | 2571 | 日期定向 = dw+dy+mo+yr |
| `draw` | float | 0-1 | 1880 | 画图 |
| `ds` | float | 0-1 | 2098 | 季节 (不在orient中) |
| `dw` | float | 0-1 | 2571 | 星期几 |
| `dy` | float | 0-1 | 2571 | 日 |
| `mo` | float | 0-1 | 2571 | 月 |
| `yr` | float | 0-1 | 2571 | 年 |
| `total_cognition` | float | 0-21 | 2381 | 总认知分(计算方式不明) |
| `memory_z` | float | z-score | 3698 | 记忆标准化分 |
| `orient_z` | float | z-score | 2571 | 定向标准化分 |
| `z_ser7` | float | z-score | 3425 | Serial7标准化分 |
| `z_tr20` | float | z-score | 3698 | tr20标准化分 |
| `slfmem` | category | — | 1665 | 自评记忆力 |
| `memrye` | category | — | 201 | 记忆问题 |
| `cog_status` | category | — | 0 | 认知状态分级 |

## 抑郁/心理健康

| 变量 | 类型 | 范围 | Wave1 缺失 |
|------|------|------|-----------|
| `cesd10` | float | 0-30 | 1671 |
| `depresl` | float | — | 1848 |

## 社会活动

| 变量 | 类型 | Wave1 缺失 | 说明 |
|------|------|-----------|------|
| `socwk` | category(是/否) | 1484 | 是否参加任何社会活动 |
| `act_1` - `act_8` | category(是/否) | 1484 | 8类具体活动 |
| `social1` - `social11` | category(是/否) | 1484 | 11类社交活动 |
| `freq_act_1` - `freq_act_8` | float(1-4) | ~1485 | 活动频率 |
| `freq_social1` - `freq_social11` | float(1-4) | ~1485 | 社交频率 |
| `hobby` | category | 1484 | 是否有爱好 |

freq 编码: 1=几乎每天, 2=几乎每周, 3=不经常, 4=从不

## 家庭/子女

| 变量 | 类型 | Wave1 缺失 | 说明 |
|------|------|-----------|------|
| `hchild` | int | 0 | 子女数量 |
| `hson` | int | 0 | 儿子数量 |
| `hdau` | int | 0 | 女儿数量 |
| `kcnt` | category(是/否) | 449 | 是否与子女有联系 |
| `kcntf` | category(是/否) | 447 | 是否面对面联系 |
| `kcntpm` | category(是/否) | 4649 | 是否电话/邮件联系 |
| `hcoresd` | category(是/否) | 480 | 是否与子女同住 |
| `hlvnear` | category(是/否) | 480 | 子女是否住在附近 |
| `sati_child` | category | 17708(w1) | 对子女满意度(仅部分波次) |
| `family_size` | int | 0 | 家庭规模 |

## 慢性病

| 变量 | 类型 | Wave1 缺失 | 说明 |
|------|------|-----------|------|
| `hibpe` | category(是/否) | 238 | 高血压(医生告知) |
| `hibpe_self` | category(是/否) | 4436 | 高血压(自评) |
| `diabe` | category(是/否) | 300 | 糖尿病 |
| `hearte` | category(是/否) | 241 | 心脏病 |
| `stroke` | category(是/否) | 182 | 脑卒中 |
| `cancre` | category(是/否) | 222 | 癌症 |
| `arthre` | category(是/否) | 184 | 关节炎 |
| `lunge` | category(是/否) | 212 | 肺病 |
| `livere` | category(是/否) | 270 | 肝病 |
| `kidneye` | category(是/否) | 256 | 肾病 |
| `digeste` | category(是/否) | 191 | 消化系统疾病 |
| `psyche` | category(是/否) | 218 | 精神疾病 |
| `asthmae` | category(是/否) | 211 | 哮喘 |
| `dyslipe` | category(是/否) | 495 | 血脂异常 |
| `chronic_num` | float | 131 | 慢性病数量 |

## 体格/生理测量

| 变量 | 类型 | Wave1 缺失 |
|------|------|-----------|
| `bmi` | float | 4077 |
| `mheight` | float | 4013 |
| `mweight` | float | 3980 |
| `mwaist` | float | 3939 |
| `systo` / `systo1-3` | float | ~3968 |
| `diasto` / `diasto1-3` | float | ~3969 |
| `pulse` / `pulse1-3` | float | ~3974 |
| `gripsum` | float | 4135 |

注意: `bmi` 有异常值(max=2755)，使用前需过滤到 10-60 范围。

## 生活习惯

| 变量 | 类型 | Wave1 缺失 |
|------|------|-----------|
| `smokev` | category(是/否) | 149 | 曾经吸烟 |
| `smoken` | category(是/否) | 801 | 当前吸烟 |
| `smokef` | float | 2034 | 每天吸几支 |
| `drinkev` | category(是/否) | 167 | 曾经饮酒 |
| `drinkl` | category(是/否) | 156 | 过去一年饮酒 |
| `sleep_night` | float | 1617 | 夜间睡眠时长 |
| `sleep_nap` | float | 1523 | 午睡时长 |

## 功能障碍 (ADL/IADL)

| 变量 | 说明 |
|------|------|
| `batha` | 洗澡困难 |
| `dressa` | 穿衣困难 |
| `eata` | 进食困难 |
| `beda` | 上下床困难 |
| `toilta` | 上厕所困难 |
| `urina` | 控制大小便困难 |
| `iadl` | IADL 总分 |

## 经济/保险

| 变量 | 说明 |
|------|------|
| `income_total` | 总收入 |
| `ins` | 是否有保险 |
| `pension` | 是否有养老金 |
| `work` | 是否工作 |
| `retire` | 是否退休 |
