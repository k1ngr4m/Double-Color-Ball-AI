#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测试大乐透 AI 预测数据文件格式"""

import json


def test_prediction_file() -> None:
    print("=" * 50)
    print("测试 大乐透 AI 预测数据文件")
    print("=" * 50 + "\n")

    with open("data/sport_lottery_ai_predictions.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    assert "prediction_date" in data, "缺少 prediction_date 字段"
    assert "target_period" in data, "缺少 target_period 字段"
    assert "models" in data, "缺少 models 字段"

    print("✅ 基本字段完整")
    print(f"   预测日期: {data['prediction_date']}")
    print(f"   目标期号: {data['target_period']}\n")

    models = data["models"]
    print(f"✅ 模型数量: {len(models)}")

    for model in models:
        model_name = model.get("model_name", "未知")
        predictions = model.get("predictions", [])
        assert len(predictions) == 5, f"{model_name} 预测组数量不正确: {len(predictions)}"

        for pred in predictions:
            red_balls = pred.get("red_balls", [])
            blue_balls = pred.get("blue_balls", [])

            assert len(red_balls) == 5, f"{model_name} 前区数量不正确"
            assert red_balls == sorted(red_balls), f"{model_name} 前区未排序"
            assert len(blue_balls) == 2, f"{model_name} 后区数量不正确"
            assert blue_balls == sorted(blue_balls), f"{model_name} 后区未排序"

        print(f"   ✓ {model_name}: 5 组预测，格式正确")

    print("\n" + "=" * 50)
    print("✅ 所有测试通过！")
    print("=" * 50)


if __name__ == "__main__":
    test_prediction_file()
