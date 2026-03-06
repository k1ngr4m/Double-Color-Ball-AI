# AI 预测自动生成指南

## 功能说明

本项目提供两个 AI 预测自动生成脚本：

| 脚本 | 彩种 | 输出文件 |
|------|------|----------|
| `generate_ai_prediction.py` | 双色球（6+1） | `data/ai_predictions.json` |
| `sport_lottery_generate_ai_prediction.py` | 大乐透（5+2） | `data/sport_lottery_ai_predictions.json` |

两个脚本均可自动调用多个 AI 模型生成预测数据，并在生成新预测前自动归档已开奖的旧预测。

## 前置要求

### 1. 安装依赖

```bash
pip install openai
```

### 2. 配置 API

通过环境变量设置 API 配置：

```bash
export AI_API_KEY="your-api-key"
export AI_BASE_URL="https://aihubmix.com/v1"  # 可选，有默认值
```

或创建 `.env` 文件（参考 `.env.example`）。

## 使用方法

### 运行脚本

**双色球**:
```bash
python3 generate_ai_prediction.py
```

**大乐透**:
```bash
python3 sport_lottery_generate_ai_prediction.py
```

### 执行流程

两个脚本的执行流程一致：

1. **归档旧预测** - 如果旧预测的目标期号已开奖，自动归档到历史记录并计算命中结果
2. **加载历史数据** - 读取最近 30 期开奖数据
3. **获取下期信息** - 从 `next_draw` 字段获取预测目标期号和日期
4. **调用 AI 模型** - 逐个调用配置的 AI 模型生成预测
5. **验证预测数据** - 检查返回的 JSON 格式是否正确（双色球 6+1 / 大乐透 5+2）
6. **创建备份** - 备份现有预测文件
7. **保存预测** - 将新预测保存到对应的 JSON 文件

### 输出示例

**双色球**:
```
==================================================
🤖 双色球 AI 预测自动生成
==================================================

📊 加载历史开奖数据...
🎯 目标期号: 25124
📅 开奖日期: 2025年10月28日
...
🎉 预测生成完成！
```

**大乐透**:
```
==================================================
🤖 大乐透 AI 预测自动生成
==================================================

🎯 目标期号: 25124
📅 开奖日期: 2025年10月27日
...
🎉 大乐透预测生成完成！
```

## 生成的数据格式

### 双色球（6 红球 + 1 蓝球）

```json
{
  "prediction_date": "2025-10-27",
  "target_period": "25124",
  "models": [
    {
      "prediction_date": "2025-10-27",
      "target_period": "25124",
      "model_id": "SSB-Team-001",
      "model_name": "GPT-5",
      "predictions": [
        {
          "group_id": 1,
          "strategy": "热号追随者",
          "red_balls": ["09", "16", "17", "24", "25", "31"],
          "blue_ball": "13",
          "description": "选择最近高频号码，排除上一期号码"
        }
      ]
    }
  ]
}
```

### 大乐透（5 前区 + 2 后区）

```json
{
  "prediction_date": "2025-10-27",
  "target_period": "25124",
  "models": [
    {
      "prediction_date": "2025-10-27",
      "target_period": "25124",
      "model_id": "DLT-Team-001",
      "model_name": "GPT-5",
      "predictions": [
        {
          "group_id": 1,
          "strategy": "增强型热号追随者",
          "red_balls": ["03", "11", "18", "25", "33"],
          "blue_balls": ["04", "10"],
          "description": "聚焦近期高频前区号，区间分布合理；后区选择近20期活跃号码。"
        }
      ]
    }
  ]
}
```

## 预测策略说明

每个 AI 模型会生成 5 组预测，分别采用不同策略：

1. **热号追随者** - 选择最近 30 期高频号码（排除上一期）
2. **冷号逆向者** - 选择最近 30 期低频号码（奇偶比 3:3）
3. **平衡策略师** - 多维度平衡（奇偶/大小/和值/连号）
4. **周期理论家** - 短期频率上穿长期频率的号码
5. **综合决策者** - 融合以上所有策略

## 数据验证

脚本会自动验证生成的预测数据：

### 双色球
- ✓ 必需字段完整性（prediction_date, target_period, model_id, model_name, predictions）
- ✓ 预测组数量正确（5 组）
- ✓ 红球数量正确（6 个）
- ✓ 红球号码已排序
- ✓ 蓝球不为空

### 大乐透
- ✓ 必需字段完整性（prediction_date, target_period, model_id, model_name, predictions）
- ✓ 预测组数量正确（5 组）
- ✓ 前区数量正确（5 个，范围 01-35）
- ✓ 前区号码已排序
- ✓ 后区数量正确（2 个，范围 01-12）
- ✓ 后区号码已排序

## 注意事项

### 1. API 调用限制

- 脚本会依次调用 4 个模型，请确保 API 有足够的调用配额
- 每次调用的 timeout 设置为 180 秒（3 分钟）
- 如果某个模型调用失败，会跳过该模型继续执行

### 2. 数据备份

- 每次运行脚本都会创建备份文件
- 备份文件命名格式：`ai_predictions_backup_YYYYMMDD_HHMMSS.json`
- 备份文件与原文件在同一目录

### 3. Prompt 优化

- Prompt 模板位于脚本中的 `PROMPT_TEMPLATE` 常量
- 可根据需要修改策略说明和要求
- 参考文档：`doc/prompt.md`

### 4. 模型配置

如需添加/修改模型：

```python
MODELS = [
    {
        "id": "模型 API ID",           # API 调用时使用的模型 ID
        "name": "显示名称",            # 前端显示的模型名称
        "model_id": "数据标识"         # JSON 中的 model_id 字段
    }
]
```

## 与现有工作流集成

### GitHub Actions 自动化（已配置）

项目已配置 4 个 GitHub Actions 工作流，实现全自动化：

| 工作流 | 文件 | 触发时间 |
|--------|------|----------|
| Update Lottery Data | `update-lottery-data.yml` | 每天 22:00 (北京时间) |
| Generate AI Prediction | `generate-ai-prediction.yml` | 每周一/三/五 08:00 (北京时间) |
| Update Sport Lottery Data | `update-sport-lottery-data.yml` | 每天 22:30 (北京时间) |
| Generate Sport Lottery AI Prediction | `generate-sport-lottery-ai-prediction.yml` | 每周二/四/日 08:00 (北京时间) |

所有工作流均支持手动触发（Actions 页面 > Run workflow）。

### 手动自动化流程

如需在本地手动执行完整流程：

**双色球**:
```bash
# 1. 更新历史数据
cd fetch_history && python3 fetch_lottery_history.py && cd ..

# 2. 生成新预测
python3 generate_ai_prediction.py

# 3. 提交更改
git add data/lottery_history.json data/ai_predictions.json data/predictions_history.json
git commit -m "chore: update SSQ lottery data and AI predictions"
git push
```

**大乐透**:
```bash
# 1. 更新历史数据
cd fetch_history && python3 fetch_sports_lottery_history.py && cd ..

# 2. 生成新预测
python3 sport_lottery_generate_ai_prediction.py

# 3. 提交更改
git add data/sports_lottery_data.json data/sport_lottery_ai_predictions.json data/sport_lottery_predictions_history.json
git commit -m "chore: update DLT lottery data and AI predictions"
git push
```

## 故障排查

### 问题：JSON 解析失败

**原因**：AI 返回的内容包含额外的说明文字

**解决**：
- 脚本已自动处理 ```json 标记
- 如仍有问题，请检查 Prompt 是否强调"只返回 JSON"
- 可调整 `extract_json_from_response` 函数

### 问题：验证失败

**原因**：返回的数据格式不符合要求

**解决**：
- 查看错误提示的具体字段
- 检查红球是否排序、数量是否正确
- 确认所有必需字段是否存在

### 问题：API 调用超时

**原因**：网络延迟或模型响应慢

**解决**：
- 增加 timeout 参数（默认 180 秒）
- 检查网络连接
- 分批运行（注释掉部分模型）

## 相关文件

### 双色球
- `generate_ai_prediction.py` — 预测生成脚本
- `doc/prompt2.0.md` — Prompt 模板
- `data/lottery_history.json` — 历史开奖数据（输入）
- `data/ai_predictions.json` — AI 预测数据（输出）
- `data/predictions_history.json` — 历史预测归档

### 大乐透
- `sport_lottery_generate_ai_prediction.py` — 预测生成脚本
- `doc/sport_lottery_prompt2.0.md` — Prompt 模板
- `data/sports_lottery_data.json` — 历史开奖数据（输入）
- `data/sport_lottery_ai_predictions.json` — AI 预测数据（输出）
- `data/sport_lottery_predictions_history.json` — 历史预测归档

## 许可证

本脚本仅供学习交流使用，不构成任何投资建议。
