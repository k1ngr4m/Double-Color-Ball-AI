# 双色球 & 大乐透 AI 预测数据展示系统

> 在线访问：[https://double-color-ball-ai.vercel.app](https://double-color-ball-ai.vercel.app)

<img src="images/image1.jpg" width="70%">

一个现代化的彩票数据展示系统，同时支持**双色球**和**大乐透**的历史开奖数据查看与多模型 AI 预测展示。

## ✨ 主要特性

- 🎨 现代化 UI 设计，支持亮色/暗色主题切换
- 📊 双色球 & 大乐透历史开奖数据展示
- 🤖 多 AI 模型预测结果对比（GPT-5 / Claude 4.5 / Gemini 2.5 / DeepSeek R1）
- 🎯 自动计算预测命中情况
- 📱 完全响应式设计，支持移动端
- ⚡ 优雅的动画效果和交互体验
- 🔄 GitHub Actions 自动抓取数据 & 自动生成 AI 预测

<details>
<summary><h2>🚀 快速开始</h2></summary>

### 方法一：使用启动脚本（推荐）

#### macOS/Linux:
```bash
# 进入项目目录
cd Double-Color-Ball-AI

# 运行启动脚本
./start_server.sh
```

#### Windows:
```cmd
# 双击运行 start_server.bat
# 或在命令行中运行
start_server.bat
```

然后在浏览器中打开：http://localhost:8000

### 方法二：手动启动服务器

```bash
# 使用 Python 启动 HTTP 服务器
python3 -m http.server 8000

# 或使用 Python 2
python -m SimpleHTTPServer 8000
```

然后在浏览器中打开：http://localhost:8000


</details>

## 🔮 AI 预测策略

每个 AI 模型会生成 5 组预测，分别采用不同策略（双色球 & 大乐透通用）：

| 策略 | 说明 |
|------|------|
| 热号追随者 | 选择最近 30 期高频号码，追踪热门趋势 |
| 冷号逆向者 | 选择最近 30 期低频号码，期待均值回归 |
| 平衡策略师 | 综合奇偶比、大小比、和值、连号等多维度平衡 |
| 周期理论家 | 选择短期频率上穿长期频率的号码 |
| 综合决策者 | 融合以上所有策略的综合方案 |

> 双色球为 6+1（6 红球 + 1 蓝球），大乐透为 5+2（5 前区 + 2 后区），策略逻辑一致但号码范围不同。

## 📁 项目结构

```
Double-Color-Ball-AI/
├── index.html                                  # 双色球主页面
├── sport_lottery_index.html                    # 大乐透主页面
├── css/
│   └── style.css                               # 样式文件
├── js/
│   ├── app.js                                  # 主应用逻辑
│   ├── data-loader.js                          # 数据加载模块
│   └── components.js                           # UI 组件
├── data/
│   ├── lottery_history.json                    # 双色球历史开奖数据
│   ├── ai_predictions.json                     # 双色球 AI 预测数据
│   ├── predictions_history.json                # 双色球历史预测对比
│   ├── sports_lottery_data.json                # 大乐透历史开奖数据
│   ├── sport_lottery_ai_predictions.json       # 大乐透 AI 预测数据
│   └── sport_lottery_predictions_history.json  # 大乐透历史预测对比
├── fetch_history/
│   ├── fetch_lottery_history.py                # 双色球数据爬取脚本
│   ├── fetch_sports_lottery_history.py         # 大乐透数据爬取脚本
│   └── *.json                                  # 原始爬取数据
├── doc/
│   ├── prompt2.0.md                            # 双色球 AI Prompt 模板
│   └── sport_lottery_prompt2.0.md              # 大乐透 AI Prompt 模板
├── generate_ai_prediction.py                   # 双色球 AI 预测自动生成脚本
├── sport_lottery_generate_ai_prediction.py     # 大乐透 AI 预测自动生成脚本
├── .github/workflows/
│   ├── update-lottery-data.yml                 # 双色球数据自动更新
│   ├── generate-ai-prediction.yml              # 双色球 AI 预测自动生成
│   ├── update-sport-lottery-data.yml           # 大乐透数据自动更新
│   └── generate-sport-lottery-ai-prediction.yml# 大乐透 AI 预测自动生成
├── start_server.sh                             # 启动脚本 (macOS/Linux)
├── start_server.bat                            # 启动脚本 (Windows)
├── AI_PREDICTION_GUIDE.md                      # AI 预测自动化指南
├── DATA_UPDATE_GUIDE.md                        # 数据更新指南
├── DEPLOYMENT.md                               # 部署指南
└── README.md                                   # 项目说明
```

## 🔄 更新数据

### 更新历史开奖数据

#### 双色球

```bash
cd fetch_history
python3 fetch_lottery_history.py
```

#### 大乐透

```bash
cd fetch_history
python3 fetch_sports_lottery_history.py
```

脚本会：
- 自动从 500 彩票网爬取最新数据
- 与现有数据合并（去重）
- 创建带时间戳的备份文件
- 自动同步到 `data/` 目录对应的 JSON 文件
- 自动计算下期开奖信息

### 自动生成 AI 预测数据

#### 双色球

```bash
python3 generate_ai_prediction.py
```

#### 大乐透

```bash
python3 sport_lottery_generate_ai_prediction.py
```

脚本功能：
- 🤖 自动调用 4 个 AI 模型（GPT-5, Claude 4.5, Gemini 2.5, DeepSeek R1）
- 📊 基于历史数据生成 5 种策略预测
- ✅ 自动验证预测数据格式（双色球 6+1 / 大乐透 5+2）
- 💾 自动备份现有预测
- 🎯 自动获取下期期号和日期
- 📦 自动归档已开奖预测到历史记录

**首次使用需配置 API**：

1. 安装依赖：
```bash
pip install openai
```

2. 设置环境变量：
```bash
export AI_API_KEY="your-api-key"
export AI_BASE_URL="https://your-api-endpoint.com/v1"  # 可选，有默认值
```

或创建 `.env` 文件（参考 `.env.example`）。

3. 如使用 GitHub Actions 自动运行，需在仓库 Settings > Secrets and variables > Actions 中添加：
   - `AI_API_KEY` — 你的 API Key
   - `AI_BASE_URL` — API 端点地址（可选）

详细说明：[AI_PREDICTION_GUIDE.md](./AI_PREDICTION_GUIDE.md)

### GitHub Actions 自动化

项目配置了 4 个 GitHub Actions 工作流，实现全自动化：

| 工作流 | 触发时间 | 说明 |
|--------|----------|------|
| Update Lottery Data | 每天 22:00 (北京时间) | 自动抓取双色球最新开奖数据 |
| Generate AI Prediction | 每周一/三/五 08:00 (北京时间) | 自动生成双色球 AI 预测 |
| Update Sport Lottery Data | 每天 22:30 (北京时间) | 自动抓取大乐透最新开奖数据 |
| Generate Sport Lottery AI Prediction | 每周二/四/日 08:00 (北京时间) | 自动生成大乐透 AI 预测 |

所有工作流均支持手动触发（Actions 页面 > Run workflow）。

### 手动更新 AI 预测数据

如果需要手动编辑，可以直接修改对应的 JSON 文件：

#### 双色球 `data/ai_predictions.json`
```json
{
  "prediction_date": "2025-10-21",
  "target_period": "25121",
  "models": [
    {
      "model_id": "model-id",
      "model_name": "模型名称",
      "predictions": [
        {
          "group_id": 1,
          "strategy": "策略名称",
          "red_balls": ["01", "02", "03", "04", "05", "06"],
          "blue_ball": "07",
          "description": "策略描述"
        }
      ]
    }
  ]
}
```

#### 大乐透 `data/sport_lottery_ai_predictions.json`
```json
{
  "prediction_date": "2025-10-21",
  "target_period": "25121",
  "models": [
    {
      "model_id": "model-id",
      "model_name": "模型名称",
      "predictions": [
        {
          "group_id": 1,
          "strategy": "策略名称",
          "red_balls": ["01", "02", "03", "04", "05"],
          "blue_balls": ["01", "02"],
          "description": "策略描述"
        }
      ]
    }
  ]
}
```

## 🎨 主题切换

点击右上角的主题切换按钮（太阳/月亮图标）可以在亮色和暗色主题之间切换。主题偏好会自动保存到浏览器本地存储。

## 📝 数据格式说明

### 双色球 lottery_history.json
```json
{
  "last_updated": "2025-10-21T10:00:00Z",
  "data": [
    {
      "period": "25120",
      "date": "2025-10-19",
      "red_balls": ["01", "02", "04", "07", "13", "32"],
      "blue_ball": "07"
    }
  ]
}
```

### 双色球 ai_predictions.json
```json
{
  "prediction_date": "2025-10-21",
  "target_period": "25121",
  "models": [...]
}
```

### 大乐透 sports_lottery_data.json
```json
{
  "last_updated": "2025-10-21T10:00:00Z",
  "data": [
    {
      "period": "25120",
      "date": "2025-10-20",
      "red_balls": ["03", "11", "18", "25", "33"],
      "blue_balls": ["04", "10"]
    }
  ]
}
```

### 大乐透 sport_lottery_ai_predictions.json
```json
{
  "prediction_date": "2025-10-21",
  "target_period": "25121",
  "models": [
    {
      "model_id": "DLT-Team-001",
      "model_name": "GPT-5",
      "predictions": [
        {
          "group_id": 1,
          "strategy": "增强型热号追随者",
          "red_balls": ["03", "11", "18", "25", "33"],
          "blue_balls": ["04", "10"],
          "description": "..."
        }
      ]
    }
  ]
}
```

## ⚠️ 重要提示

**浏览器安全限制**:
- ❌ 不能直接双击 `index.html` 打开（会遇到 CORS 错误）
- ✅ 必须通过 HTTP 服务器访问

这是因为浏览器的同源策略限制，使用 `file://` 协议无法加载本地 JSON 文件。

## 🛠️ 技术栈

- **前端**: 纯 JavaScript (ES6+)
- **样式**: 现代 CSS (CSS Variables, Flexbox, Grid)
- **AI 预测**: Python 3 + OpenAI SDK（兼容多模型 API）
- **数据爬取**: Python 3 + BeautifulSoup（500 彩票网）
- **自动化**: GitHub Actions（数据更新 + AI 预测生成）
- **设计风格**: shadcn/ui inspired

## 📄 免责声明

本网站展示的 AI 预测数据仅供参考和研究使用，不构成任何购彩建议。彩票开奖结果具有随机性，任何预测都无法保证中奖。请理性购彩，量力而行。

## 🌐 部署到 Vercel

本项目已配置好 Vercel 部署（双色球 & 大乐透均支持），详细步骤请查看 [DEPLOYMENT.md](./DEPLOYMENT.md)

### 快速部署

1. 安装 Vercel CLI: `npm install -g vercel`
2. 登录: `vercel login`
3. 部署: `vercel`

**不会有跨域问题！** Vercel 提供标准的 HTTP 服务，所有资源都从同一域名加载。

### 特性

- ✅ 免费部署
- ✅ 自动 HTTPS
- ✅ 全球 CDN 加速
- ✅ 自动部署（连接 GitHub）
- ✅ 支持自定义域名

详细说明: [DEPLOYMENT.md](./DEPLOYMENT.md)

## 📧 反馈与支持

如有问题或建议，欢迎提交 Issue 或 Pull Request。
