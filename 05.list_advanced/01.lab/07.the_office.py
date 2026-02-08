def happiness(employees_happiness, factor):
    improved_happiness = [new * factor for new in employees_happiness]
    average_happiness = sum(improved_happiness) / len(improved_happiness)
    above_or_average = [happy for happy in improved_happiness if happy >= average_happiness]
    if len(above_or_average) >= len(improved_happiness) / 2:
        return f"Score: {len(above_or_average)}/{len(improved_happiness)}. Employees are happy!"
    else:
        return f"Score: {len(above_or_average)}/{len(improved_happiness)}. Employees are not happy!"

employees_happiness_ = list(map(int, input().split()))
factor_ = int(input())
result_ = happiness(employees_happiness_, factor_)
print(result_)