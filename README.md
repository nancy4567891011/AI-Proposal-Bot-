好的 ✅ 我帮你整理了一份 **旅游定制行程自动生成器的需求文档（MD 格式）**，内容完整、结构清晰，包含功能、输入输出、UI 展示和美观要求，方便你直接使用或扩展。

---

# 旅游定制行程自动生成器 - 需求文档

## 一、项目背景

随着个性化旅游需求的增长，用户希望在输入少量条件（预算、人数、目的地）后，快速获得一份初步定制行程方案。
本项目目标是开发一个自动生成 **HTML 格式的旅游行程方案** 的工具，帮助客户快速感受到专业性与消费吸引力。

---

## 二、目标用户

* 对旅游定制有需求的个人或小团体
* 旅行社销售团队（可直接将方案发送给客户）
* 自助出行规划用户

---

## 三、输入参数

用户需要提供以下基本条件：

1. **预算**（如：5000 元 / 人，或团队总预算）
2. **人数**（如：2 人，5 人）
3. **目的地**（如：日本东京、云南大理、法国巴黎）

---

## 四、输出结果

系统自动生成一份 **HTML 格式的初步旅游行程方案**，包括以下内容：

1. **封面区域**

   * 目的地大图（吸引眼球）
   * 标题（如：“东京 5 日深度游 · 定制方案”）
   * 简要介绍（烘托氛围，突出特色）

2. **行程概览**

   * 预算说明（总预算 / 人均预算）
   * 出行天数建议（由系统根据预算和目的地自动推荐，如 3 天、5 天、7 天）
   * 人数对应的方案建议（小团体 / 家庭 / 情侣）

3. **每日行程安排（表格 / 卡片式）**

   * 日期 / 天数
   * 上午活动（含推荐景点 + 图片）
   * 下午活动（含推荐景点 + 图片）
   * 晚间活动（含餐饮/演出/自由活动）
   * 交通和住宿提示

4. **附加推荐**

   * 当地特色美食（带图片）
   * 必买手信/纪念品
   * 特色体验项目（如温泉、演唱会、户外活动）

5. **联系方式/引导消费**

   * “立即预订”按钮（跳转至旅行社咨询/客服）
   * “联系我们”区域（电话、微信二维码）

---

## 五、功能要求

1. **自动生成逻辑**

   * 根据预算和目的地匹配推荐景点与餐饮
   * 按天生成行程，确保预算分配合理
   * 美观且有消费引导性

2. **输出形式**

   * 自动输出 HTML 文件（含图片、卡片式排版）
   * 可直接嵌入官网 / 微信 H5

3. **美观设计**

   * 使用响应式卡片设计（PC / 手机自适应）
   * 图片为目的地高清图（可调用图库 API）
   * 色彩风格：清新明亮，带有旅行氛围（蓝色 / 橙色 / 绿色为主）

---

## 六、示例 HTML 结构（简化版）

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>东京5日游 · 定制方案</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
    header { background: url('tokyo.jpg') no-repeat center; background-size: cover; height: 300px; color: white; display:flex; align-items:center; justify-content:center; font-size:2em; font-weight:bold; }
    section { padding: 20px; }
    .day-card { border:1px solid #ddd; border-radius:10px; margin-bottom:20px; padding:15px; box-shadow:0 2px 5px rgba(0,0,0,0.1);}
    .cta { text-align:center; margin:30px 0; }
    .cta button { background:#ff6600; color:white; padding:10px 20px; font-size:1.2em; border:none; border-radius:8px; cursor:pointer; }
  </style>
</head>
<body>
  <header>东京 5 日深度游 · 定制方案</header>
  <section>
    <h2>行程概览</h2>
    <p>预算：¥5000/人 | 人数：2人 | 推荐天数：5天</p>
  </section>
  <section>
    <h2>每日行程</h2>
    <div class="day-card">
      <h3>Day 1: 抵达东京</h3>
      <p>上午：抵达东京，入住酒店</p>
      <p>下午：浅草寺 · 晴空塔</p>
      <p>晚上：银座购物 & 寿司晚餐</p>
    </div>
  </section>
  <div class="cta">
    <button>立即预订</button>
  </div>
</body>
</html>
```

---

## 七、项目实现说明

本仓库基于上述需求文档实现了一个可直接生成 HTML 行程方案的 **`itinerary_generator`** Python 包。核心特性如下：

* 预置东京、云南大理、巴黎等热门目的地的主题活动、图片和美食/伴手礼/体验推荐，并提供通用目的地兜底方案。
* 根据预算、人数自动推算推荐天数和预算分配，生成包含封面、行程概览、每日活动卡片、贴心提示及联系方式的精美 HTML。
* 提供命令行工具与 Python API，方便旅行顾问、销售或个人用户快速产出可发送给客户的初步方案。

### 目录结构

```
src/
  itinerary_generator/
    data.py            # 目的地静态资料与图片
    generator.py       # 行程计算与预算分配逻辑
    renderer.py        # HTML 模板与样式渲染
    cli.py             # 命令行入口
tests/
  test_generator.py    # 核心功能单元测试
```

### 安装与运行

1. 确保本地 Python ≥ 3.10。
2. 在仓库根目录执行（可选）创建虚拟环境并安装依赖：

```bash
python -m venv .venv
source .venv/bin/activate  # Windows 使用 .venv\Scripts\activate
pip install -r requirements.txt  # 如无需额外依赖可跳过
pip install -e .                 # 可编辑安装，便于直接调用 CLI
```

> 项目仅依赖标准库运行测试时需安装 `pytest`（见下方测试章节）。

### 命令行示例

```bash
python -m itinerary_generator "日本东京" 24000 2 --output tokyo.html
```

*第一个参数为目的地，第二个为预算（默认视作总预算），第三个为人数。可选参数：*

* `--per-person` 表示输入预算为人均金额；
* `--currency-symbol` 设置货币符号；
* `--contact-phone / --contact-wechat / --contact-email / --contact-company` 自定义联系信息；
* `--cta-link / --cta-label` 自定义“立即预订”按钮。

执行后会在指定路径生成一份响应式 HTML 文件，可直接发送给客户或嵌入网页、H5 页面。

### 作为 Python 库调用

```python
from itinerary_generator import TravelItineraryGenerator, render_itinerary_html

generator = TravelItineraryGenerator()
itinerary = generator.generate_itinerary("云南大理", budget=12000, travellers=3)
html = render_itinerary_html(itinerary)

with open("dali.html", "w", encoding="utf-8") as fp:
    fp.write(html)
```

### 测试

项目使用 `pytest` 进行单元测试验证行程生成、别名解析和 HTML 渲染：

```bash
pip install pytest
pytest
```

---


