def company(profit, performance):
    avg = sum(performance) / len(performance)

    if profit >= 90 and avg >= 80:
        return "Peak"
    elif profit >= 75 and avg >= 60:
        return "Healthy"
    elif profit >= 60 and avg >= 40:
        return "Margin"
    else:
        return "Failing"


details = [
    {"Company": "A", "profit": 95, "performance": [80, 85, 90]},
    {"Company": "B", "profit": 70, "performance": [45, 60, 55]},
    {"Company": "C", "profit": 50, "performance": [30, 35, 40]},
]

for s in details:
    label = company(s["profit"], s["performance"])
    print(s["Company"], label)