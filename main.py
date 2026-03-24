import pandas as pd
from pathlib import Path


pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

# ============================
# ЧТЕНИЕ ВЫПИСКИ ИЗ CSV
# ============================

# путь к файлу выписки
file_path = Path("data/input/январь_26.csv")

print("Открываем файл:", file_path)

# читаем CSV файл
df = pd.read_csv(
    file_path,
    sep="\t",  # разделитель — табуляция
    encoding="cp1251",  # кодировка (часто у банков)
    dtype=str,  # читаем всё как строки
)
# ============================
# ОСТАВЛЯЕМ НУЖНЫЕ КОЛОНКИ
# ============================

needed_columns = ["text70", "pol_name", "sum_rur"]

df = df[needed_columns]
# убираем первую строку (она не данные)
df = df.iloc[1:]

print("\nОставили только нужные колонки:")
print(df.head())

# приводим сумму к числу
df["sum_rur"] = (
    df["sum_rur"]
    .str.replace(",", ".")  # 1. меняем запятую на точку
    .astype(float)  # 2. превращаем в число
    .round(0)  # 3. округляем
    .astype(int)  # 4. делаем целым числом
)
